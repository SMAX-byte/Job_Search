import requests
from bs4 import BeautifulSoup
def main():
    print("\n\nHello, World from scraper.py!\n\n")


url = "https://www.xula.edu/about/mission-values.html"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",

}
resp = requests.get(url,  headers=headers)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")
div = soup.find("div", class_="editorarea")

if div:
    text = div.get_text(separator=" ", strip=True)
    idx = text.find("founded by Saint")
    if idx != -1:
        print(text[idx:])
    else:
        print("Could not find 'founded by Saint' in the text.")
else:
    print("No div.editorarea found.")


if __name__ == "__main__":
    main()