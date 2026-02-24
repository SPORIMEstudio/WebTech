# Web Tech

<p align="center">
  <b>Web Tech</b><br>
  Ethical Web Technology Scanner for Developers & Security Researchers
</p>

---

## 🔎 About

Web Tech is a professional CLI tool that detects technologies used by websites.

It identifies:

- Web Server (Apache, Nginx, IIS)
- Backend Language (PHP, Node.js, ASP.NET)
- CMS (WordPress, Joomla, Drupal)
- Frontend Frameworks (React, Vue, Angular)
- Libraries (jQuery + version detection)
- CSS Frameworks (Bootstrap)
- Meta generator tags
- X-Powered-By headers

This tool is built for:

- Bug bounty hunters
- Security researchers
- Web developers
- Ethical hackers

---

## 🚀 Installation

### Install from PyPI

```bash
pip install sporime-webtech
```
## Install from GitHub

```bash
pip install git+https://github.com/SPORIMEstudio/WebTech.git
```
## Clone & Install   

```bash
git clone https://github.com/SPORIMEstudio/WebTech.git
cd webtech
pip install . 
```
## ⚡ Usage

### Basic Scan:

```bash
webtech example.com
```
### Scan with JSON output:

```bash
webtech example.com --json result.json
```
## 🖥 Example Output
```bash
Web Tech
Ethical Web Technology Scanner

[+] Target: https://example.com
[+] Starting scan...

========== Scan Results ==========

[+] Server: nginx/1.18.0
[+] Backend: PHP
[+] CMS: WordPress
[+] WordPress Version: 6.2.1
[+] jQuery Version: 3.6.0
[+] CSS Framework: Bootstrap

==================================
```
## 📦 Requirements
* Python 3.7+
* requests
* beautifulsoup4
* colorama

## ⚠️ Disclaimer
This tool is intended for educational and authorized security testing purposes only.

The developer is not responsible for any misuse or illegal activity performed using this tool.

Always scan websites you own or have permission to test.

## ⭐ Support
If you find this project useful, please consider giving it a star on GitHub.
