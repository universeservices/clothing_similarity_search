import requests
from bs4 import BeautifulSoup


def scrape_clothing_descriptions():
    clothing_descriptions = []

    # Example: Scraping from a single website
    url = "https://www.myntra.com/men-tshirts"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Example: Extracting clothing descriptions from HTML elements
        description_elements = soup.find_all("div", class_="clothing-description")
        for element in description_elements:
            description = element.text.strip()
            clothing_descriptions.append(description)

    except requests.exceptions.RequestException as e:
        print("Error occurred during web scraping:", e)

    return clothing_descriptions
