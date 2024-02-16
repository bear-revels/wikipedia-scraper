import requests
from bs4 import BeautifulSoup
import re
import json
import threading

class WikipediaScraper:
    def __init__(self):
        # Initialize the WikipediaScraper object with base URL and endpoints.
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "countries"
        self.leaders_endpoint = "leaders"
        self.cookies_endpoint = "cookie"
        self.leaders_data = {}
        self.cookie = None

    def refresh_cookie(self):
        # Refresh the cookie by calling the cookie endpoint.
        req_cookie = requests.get(f"{self.base_url}/{self.cookies_endpoint}")
        self.cookie = req_cookie.cookies

    def get_countries(self):
        # Get the list of supported countries from the API.
        countries_url = f"{self.base_url}/{self.country_endpoint}"
        response = requests.get(countries_url, cookies=self.cookie)
        return response.json()

    def get_leaders(self):
        # Retrieve the list of country codes
        countries = self.get_countries()
        # Initialize a dictionary to store leaders per country
        leaders_per_country = {}
        # Define a function to fetch leaders for a given country code
        def fetch_leaders(country_code):
            self.refresh_cookie()  # Refresh the cookie
            leaders_url = f"{self.base_url}/{self.leaders_endpoint}"
            leaders_per_country[country_code] = requests.get(leaders_url, params={'country': country_code}, cookies=self.cookie).json()
        # Create and start threads for each country code
        threads = []
        for country_code in countries:
            thread = threading.Thread(target=fetch_leaders, args=(country_code,))
            thread.start()
            threads.append(thread)
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        # Store the leaders data in the instance attribute
        self.leaders_data = leaders_per_country

    def get_first_paragraph(self, wikipedia_url):
        # Extract the first paragraph from the Wikipedia page URL.
        response = requests.get(wikipedia_url)
        soup = BeautifulSoup(response.content, "html.parser")
        first_paragraph = ""
        for paragraph in soup.find_all("p"):
            text = paragraph.get_text().strip()
            if text and paragraph.find("b"):
                first_paragraph = text
                break
        sanitized_first_paragraph = re.sub(r'\xa0—*|\[[^\]]*\]', ' ', first_paragraph)
        return sanitized_first_paragraph

    def to_json_file(self, filepath):
        # Store the data structure into a JSON file.
        with open(filepath, 'w') as file:
            json.dump(self.leaders_data, file)

    def get_leaders_data(self):
        # Get the leaders data retrieved from the API.
        return self.leaders_data
