"""Scraper for ftcstats.org"""
import httpx
from bs4 import BeautifulSoup


def get(year: int):
    data = ""
    with httpx.stream("GET", 'https://ftcstats.org/2023/index.html') as r:
        for text in r.iter_text():
            print(text)
    return data


soup = BeautifulSoup(get(2023), 'html.parser')
rankings_table = soup.find("table", id="opr")
print(rankings_table.format())
