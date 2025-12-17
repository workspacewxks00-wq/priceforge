import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_target(target):
    try:
        response = requests.get(target["url"], timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        price_el = soup.select_one(target["price_selector"])

        if not price_el:
            return None

        price = price_el.get_text(strip=True)

        return {
            "name": target["name"],
            "url": target["url"],
            "price": price,
            "currency": target.get("currency", ""),
            "timestamp": datetime.utcnow().isoformat()
        }

    except Exception as e:
        print(f"Error scraping {target['url']}: {e}")
        return None
