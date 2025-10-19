import requests
from bs4 import BeautifulSoup
import csv

def main():
    print("\n\n💻 Hello from scraper.py!\n")
    scrape_xula()
    scrape_indeed()

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
                print(text[idx:idx + 300], "...\n")
            else:
                print("⚠️ Could not find 'founded by Saint' in mission text.\n")
        else:
            print("❌ No div.editorarea found.\n")
    except Exception as e:
        print("❌ XULA scrape failed:", e)

def scrape_indeed():
    print("\n💼 Scraping Indeed for job listings...\n")

    url = "https://www.indeed.com/jobs?q=software+developer&l=New+Orleans%2C+LA"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        job_cards = soup.find_all("div", class_="job_seen_beacon")

        with open("indeed_jobs.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Job Title", "Company", "Location", "Date Posted"])

            for card in job_cards:
                title_elem = card.find("h2", class_="jobTitle")
                company_elem = card.find("span", class_="companyName")
                location_elem = card.find("div", class_="companyLocation")
                date_elem = card.find("span", class_="date")

                title = title_elem.text.strip() if title_elem else "N/A"
                company = company_elem.text.strip() if company_elem else "N/A"
                location = location_elem.text.strip() if location_elem else "N/A"
                date_posted = date_elem.text.strip() if date_elem else "N/A"

                writer.writerow([title, company, location, date_posted])

        print("✅ Job data saved to indeed_jobs.csv\n")

    except Exception as e:
        print("❌ Indeed scrape failed:", e)

if __name__ == "__main__":
    main()
