# %%
import requests
from bs4 import BeautifulSoup
import re
import argparse

# Parser degli argomenti
parser = argparse.ArgumentParser(description="Crawl the web for emails")
parser.add_argument("-d", "--depth", dest ='depth', help="Depth of the crawling", required=True)
parser.add_argument("-q", "--query", dest ='query', help="Query to search", required=True)

args = parser.parse_args()
print(args.depth)
args.query = "https://www.google.com/search?q=" + args.query.replace(" ", "+")


def find_emails(soup):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", soup.text, re.I)
    return emails


def crawl(url, depth):
    if depth == 0:
        return []

    cookies = {
        "CONSENT": "PENDING+987",
        "SOCS": "CAESHAgBEhJnd3NfMjAyMzA4MTAtMF9SQzIaAmRlIAEaBgiAo_CmBg",
    }

    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    emails = find_emails(soup)

    for link in soup.find_all("a"):
        try:
            href = link.get("href")
            if href and href.startswith("/url?q="):
                print(href.split("=")[1].split("&sa")[0])
                emails.extend(crawl(href.split("=")[1].split("&sa")[0], depth - 1))
        except:
            continue

    return emails


# Utilizzo del crawler
emails = crawl(args.query, int(args.depth))
print(emails)
