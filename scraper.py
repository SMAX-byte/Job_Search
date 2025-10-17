import requests
from bs4 import BeautifulSoup
def main():
    print("\n\nHello, World from scraper.py!\n\n")


url = "https://www.xula.edu/about/mission-values.html"
resp = requests.get(url)
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