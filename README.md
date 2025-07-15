# DeepPatrol-Dark_Web_Monitoring_and_Crime_Detection_Automation


# 🕵️ Dark Web Intelligence Crawler & Visualizer

This project enables automated dark web intelligence gathering using a powerful integration of:

- **Tor + Selenium-based crawler**
- **Hunchly** for forensic logging
- **Maltego** for link analysis and visualization
- **Custom Python transforms** for threat intelligence enrichment

---

## 📦 Features

- 🔍 **Keyword-based Crawling** on popular dark web search engines (Ahmia, Not Evil, Torch, Phobos)
- 💾 **Evidence Preservation** with Hunchly for each visited .onion page
- 🧠 **Entity Extraction**: IPs, Emails, Onion URLs, and more
- 🌐 **Maltego Integration** for visualizing connections between threat actors, entities, and infrastructure

---

## 🛠️ Setup Instructions

### Step 1: 🔐 Install Tor Browser

1. [Download Tor](https://www.torproject.org/download/)
2. Go to the following directory:

   C:\Users\<YourUsername>\Desktop\Tor Browser\Browser\TorBrowser\Tor


       
<img width="686" height="38" alt="Screenshot 2025-07-15 221129" src="https://github.com/user-attachments/assets/2f2d0105-7ca4-4da9-b5d6-220988d2ffc8" />


    

4. Run `tor.exe` — keep the CLI window open during crawling.

  
<img width="792" height="143" alt="Screenshot 2025-07-15 221158" src="https://github.com/user-attachments/assets/9e1eb7b8-9926-46e5-8c15-aa885d08f0b5" />


---

### Step 2: 🧩 Install Dependencies

- ✅ **Python 3.8+**
- ✅ **Install Selenium**

  pip install selenium

- ✅ **Install Google Chrome**
- ✅ **Install [Hunchly](https://www.hunch.ly/)** and its Chrome extension
- ✅ **Install [Maltego](https://www.maltego.com/)** (Community or Pro)

---

### Step 3: 🔗 Integrate Hunchly with Maltego

We **do not include the Hunchly-Maltego integration code** in this repo due to licensing and redistribution restrictions.

➡️ Instead, follow the official instructions:

📎 **[Hunchly-Maltego Integration GitHub Repository](https://github.com/hunchly/hunchly-maltego.git)**

> ℹ️ This external repo is not maintained by us. Refer to the license and usage guidelines before modifying or redistributing it.

You may clone it for **personal or investigative use**:

git clone https://github.com/hunchly/hunchly-maltego.git


---

## 🚀 Running the Dark Web Crawler

### ✅ Before Running
- Close all Chrome windows
- Ensure `tor.exe` is running
- Ensure Hunchly is active

### 🏃 How to Run

Run the crawler:

python tor_crawler.py


### 🔧 Inputs Required:

You’ll be prompted for:

- Chrome user data directory (e.g., `C:\Users\YourName\AppData\Local\Google\Chrome\User Data`)
- Chrome profile name (e.g., `Profile 1`)
- Chrome path
- Keywords (or use default)
- After-date for filtering results (e.g., `2025-04-20`)
- Number of results to fetch

The script will:
- Crawl `.onion` results from each dark web search engine
- Log pages using Hunchly
- Extract key entities (emails, IPs, URLs)
- Store matched results in a SQLite database


![Recording 2025-07-15 235023 (2)](https://github.com/user-attachments/assets/587d5bb5-e8ff-4c94-8dc4-7799033a9216)

---

## 📁 Outputs

- 📄 `hunchly_integration/pages/` – Full page HTML dumps
- 🗃️ `classified_results.db` – SQLite DB with URLs and entities
- 🧠 Maltego Graph (via transforms) showing:
  - 📧 Emails
  - 🌐 IP Addresses
  - 🔗 Hidden links
  - 💸 (Future) Bitcoin wallet traces
 
- 
    ![Recording 2025-07-16 000044 (3)-min-min-min](https://github.com/user-attachments/assets/22e9eb3e-84b0-46c2-93d2-2b3b89fcf3c0)


---


## 🔮 Future Scope

- 💰 **Bitcoin Wallet Extraction**
  - Scrape and analyze BTC addresses in forums/marketplaces

- 🔗 **On-chain Analysis**
  - Trace transaction chains to detect mixing or laundering

- 📈 **Dynamic Visual Graphs**
  - Real-time intelligence updates inside Maltego


---

## 🧑‍💻 Authors & Contributors

This project is built for investigators, cybersecurity researchers, and digital forensic professionals.

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## ❗Disclaimer

This tool is for **educational, cybersecurity research, and lawful investigative purposes only**.  
Using this tool to access, extract, or act upon illegal content is strictly prohibited and may be a criminal offense in your jurisdiction.
