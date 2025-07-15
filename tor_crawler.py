import requests
from bs4 import BeautifulSoup
import os
import time
import subprocess
from urllib.parse import unquote, urlparse, parse_qs
from datetime import datetime

# === Configuration ===
TOR_PROXIES = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}
AHMIA_ONION = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/"
USER_DATA_DIR = input("Enter the path to your Chrome user data directory (e.g., 'C:\\Users\\YourUsername\\AppData\\Local\\Google\\Chrome\\User Data'):\n")
PROFILE_DIR = input("Enter your Chrome profile name (e.g., 'Profile 1', 'Profile 36'):\n")
CHROME_PATH = input("Enter our chrome path executable (e.g., 'C:\Program Files\Google\Chrome\Application\chrome.exe")

default_keywords = [
    "india drugs", "fake passport", "hacked database",
    "child trafficking", "illegal guns"
]
default_after_date = "2025-04-20"


user_input_keywords = input("Enter keywords (comma-separated) or press Enter to use defaults: ").strip()
if user_input_keywords:
    KEYWORDS = [kw.strip() for kw in user_input_keywords.split(',')]
else:
    KEYWORDS = default_keywords

user_input_date = input("Enter 'after' date in YYYY-MM-DD format (or press Enter to use default): ").strip()
after_date = user_input_date if user_input_date else default_after_date

LIMIT = int(input("Enter number of results per keyword (default is 5): ").strip() or 5)


OUTPUT_FILE = "found_onion_links.txt"


def search_ahmia_and_extract_redirects(keyword, limit=10):
    found_links = set()
    query = f"{AHMIA_ONION}?q={keyword.replace(' ', '+')}&after=2025-04-20"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        print(f"[+] Searching: {keyword}")
        resp = requests.get(query, headers=headers, proxies=TOR_PROXIES, timeout=30)
        soup = BeautifulSoup(resp.text, "html.parser")
        redirects = 0

        for a in soup.find_all("a", href=True):
            href = a["href"]
            if "/search/redirect?" in href and "redirect_url=" in href:
                parsed = parse_qs(urlparse(href).query)
                redirect_url = parsed.get("redirect_url", [None])[0]
                if redirect_url and ".onion" in redirect_url:
                    redirect_url = unquote(redirect_url)
                    domain = urlparse(redirect_url).netloc
                    if domain not in {urlparse(u).netloc for u in found_links}:
                        found_links.add(redirect_url)
                        print(f"[>] Found: {redirect_url}")
                        redirects += 1
            if redirects >= limit:
                break

    except Exception as e:
        print(f"[!] Error: {e}")
    return list(found_links)

def save_links_to_txt(links, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")
    print(f"[✓] Saved {len(links)} links to {filename}")

def open_links_in_chrome(links):
    for link in links:
        subprocess.Popen([
            CHROME_PATH,
            f'--user-data-dir={USER_DATA_DIR}',
            f'--profile-directory={PROFILE_DIR}',
            link
        ])
        time.sleep(1)

if __name__ == "__main__":
    all_links = []

    for kw in KEYWORDS:
        links = search_ahmia_and_extract_redirects(kw, LIMIT)
        all_links.extend(links)

    # Deduplicate again (just in case)
    all_links = list(set(all_links))

    if all_links:
        save_links_to_txt(all_links, OUTPUT_FILE)
        print("[~] Opening links in Chrome...")
        open_links_in_chrome(all_links)
    else:
        print("[!] No links found.")
