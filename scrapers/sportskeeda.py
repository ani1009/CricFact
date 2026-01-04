import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def search_text(query):
    try:
        url = f"https://www.sportskeeda.com/search?q={query}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return ""
        return BeautifulSoup(r.text, "lxml").get_text(" ")
    except:
        return ""
