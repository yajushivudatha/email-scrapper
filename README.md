# 📧 Email Scrapper

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A Python-based email extraction tool built using Selenium to scrape email addresses from websites, including dynamic pages rendered with JavaScript. 

---

## 🚀 Features

* **Automated Extraction:** Extract emails from target websites seamlessly.
* **Dynamic Content Support:** Handles JavaScript-heavy pages using Selenium WebDriver.
* **Flexible Interface:** Supports both GUI (Chrome-based) and CLI usage.
* **Developer Friendly:** Simple, modular code structure that is easy to modify.
* **Quick Setup:** Straightforward installation and execution process.

## 🧠 How It Works

The tool launches a browser session using Selenium, navigates to the specified URL, and allows the page (and any dynamic JS scripts) to fully load. It then scans the page's source content using Regular Expressions (Regex) pattern matching to identify and extract valid email addresses.

## 🏗️ Tech Stack

* **Language:** Python
* **Browser Automation:** Selenium WebDriver
* **Parsing:** Regular Expressions (Regex)
* **Target Browser:** Google Chrome

## 📂 Project Structure
```text
email-scrapper/
│── hunter.py          # Main execution script
│── requirements.txt   # Project dependencies
│── README.md          # Project documentation
📦 Installation
1. Clone the Repository

Bash
git clone [https://github.com/yajushivudatha/email-scrapper.git](https://github.com/yajushivudatha/email-scrapper.git)
cd email-scrapper
2. Create a Virtual Environment (Recommended)

Bash
python -m venv venv
3. Activate the Virtual Environment

Windows:

DOS
venv\Scripts\activate
Mac/Linux:

Bash
source venv/bin/activate
4. Install Dependencies

Bash
pip install -r requirements.txt
▶️ Usage
Run the main script from your terminal:

Bash
python hunter.py
⚠️ Important Notes
Privileges: Run the program as an Administrator for better compatibility and fewer permission restrictions.

Browser Requirement: The GUI is specifically designed to work with Google Chrome only.

Path Configuration: Ensure Chrome is installed in its default directory:
C:\Program Files\Google\Chrome

Troubleshooting: If Chrome is located in C:\Program Files (x86), please copy the Google folder over to the standard Program Files directory to ensure the script can locate the executable.

🚫 Limitations
Anti-Bot Protections: May fail on websites utilizing CAPTCHA, Cloudflare, or advanced anti-bot protections.

Scraping Blocks: Some websites actively monitor and block automated scraping behavior.

Dependencies: Requires a Selenium-compatible ChromeDriver version that matches your installed Chrome browser.

🔒 Disclaimer
This project is for educational purposes only.
The developers assume no liability for the misuse of this tool. Please ensure you have explicit permission to scrape a website and always comply with the Terms of Service (ToS) of the target domains.

🤝 Contributing
Contributions, issues, and feature requests are welcome!

Fork the repository

Create a new branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
This project is licensed under the MIT License.