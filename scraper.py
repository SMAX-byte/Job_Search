import requests
from bs4 import BeautifulSoup
def main():
    print("\n\nHello, World from scraper.py!\n\n")
if __name__ == "__main__":
    main()
def scrape_xula():
    print("\n🏫 Scraping XULA mission statement...\n")

    url = "https://www.xula.edu/about/mission-values.html"
    headers = {
"User-Agent": (
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
"AppleWebKit/537.36 (KHTML, like Gecko) "
"Chrome/118.0.0.0 Safari/537.36"
    )
}

try:
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    div = soup.find("div", class_="editorarea")
    if div:
        text = div.get_text(separator=" ", strip=True)
        idx = text.find("founded by Saint")
        if idx != -1:
            print("✅ Found mission statement section:\n")
            print(text[idx:idx + 300], "...\n")# print snippet
            else:
            print("⚠️ Could not find 'founded by Saint' in mission text.\n")
    else:
        print("❌ No div.editorarea found.\n")
except Exception as e:
    print("❌ XULA scrape failed:", e)