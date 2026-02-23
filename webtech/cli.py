#!/usr/bin/env python3
import requests
import re
import sys
import json
import argparse
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

init(autoreset=True)

class WebTechScanner:

    def __init__(self, url):
        if not url.startswith("http"):
            url = "http://" + url
        self.url = url
        self.headers = {}
        self.html = ""
        self.soup = None
        self.results = {}

    def banner(self):
        print(Fore.CYAN + Style.BRIGHT + """
██╗    ██╗███████╗██████╗     ████████╗███████╗ ██████╗██╗ 
██║    ██║██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝██╔════╝██║ 
██║ █╗ ██║█████╗  ██████╔╝       ██║   █████╗  ██║     ██████ 
██║███╗██║██╔══╝  ██╔══██╗       ██║   ██╔══╝  ██║     ██╔═██╗ 
╚███╔███╔╝███████╗██████╔╝       ██║   ███████╗╚██████╗██║ ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝        ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚╝ 
        """)

        print(Fore.YELLOW + Style.BRIGHT + "        Web Tech - Ethical Web Technology Scanner\n")
        print(Fore.GREEN + "[+] Target:", self.url)
        print(Fore.GREEN + "[+] Starting scan...\n")

    def fetch(self):
        try:
            response = requests.get(self.url, timeout=10)
            self.headers = response.headers
            self.html = response.text
            self.soup = BeautifulSoup(self.html, "html.parser")
        except Exception as e:
            print(Fore.RED + "[-] Error:", e)
            sys.exit()

    def detect_server(self):
        server = self.headers.get("Server")
        if server:
            self.results["Server"] = server

    def detect_powered_by(self):
        powered = self.headers.get("X-Powered-By")
        if powered:
            self.results["X-Powered-By"] = powered

    def detect_backend(self):
        powered = self.headers.get("X-Powered-By", "").lower()

        if "php" in powered:
            self.results["Backend"] = "PHP"

        if "asp.net" in powered:
            self.results["Backend"] = "ASP.NET"

        if "express" in powered or "node" in powered:
            self.results["Backend"] = "Node.js"

    def detect_cms(self):
        html = self.html.lower()

        if "wp-content" in html:
            self.results["CMS"] = "WordPress"
            version = re.search(r'content="wordpress\s([\d.]+)"', html)
            if version:
                self.results["WordPress Version"] = version.group(1)

        elif "joomla" in html:
            self.results["CMS"] = "Joomla"

        elif "drupal" in html:
            self.results["CMS"] = "Drupal"

    def detect_frameworks(self):
        html = self.html.lower()

        if "react" in html:
            self.results["Frontend"] = "React.js"

        if "vue" in html:
            self.results["Frontend"] = "Vue.js"

        if "angular" in html:
            self.results["Frontend"] = "Angular"

        jquery = re.search(r'jquery[.-]([\d.]+)\.js', html)
        if jquery:
            self.results["jQuery Version"] = jquery.group(1)

        if "bootstrap" in html:
            self.results["CSS Framework"] = "Bootstrap"

    def detect_generator(self):
        meta = self.soup.find("meta", attrs={"name": "generator"})
        if meta:
            self.results["Generator"] = meta.get("content")

    def display_results(self):
        print(Fore.CYAN + "\n========== Scan Results ==========\n")
        if not self.results:
            print(Fore.RED + "[-] No technologies detected.")
        else:
            for key, value in self.results.items():
                print(Fore.GREEN + f"[+] {key}: " + Fore.WHITE + str(value))
        print(Fore.CYAN + "\n==================================\n")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.results, f, indent=4)
        print(Fore.YELLOW + f"[+] Results saved to {filename}")

    def run(self):
        self.banner()
        self.fetch()
        self.detect_server()
        self.detect_powered_by()
        self.detect_backend()
        self.detect_cms()
        self.detect_frameworks()
        self.detect_generator()
        self.display_results()


def main():
    parser = argparse.ArgumentParser(description="Web Tech - Ethical Web Technology Scanner")
    parser.add_argument("url", help="Target website URL")
    parser.add_argument("--json", help="Save output as JSON file")

    args = parser.parse_args()

    scanner = WebTechScanner(args.url)
    scanner.run()

    if args.json:
        scanner.save_to_file(args.json)


def run():
    main()

if __name__ == "__main__":
    run()