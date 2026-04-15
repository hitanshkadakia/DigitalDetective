import requests
import re
from bs4 import BeautifulSoup

class ContactScraper:
    def __init__(self, url):
        self.url = url
        self.names = []
        self.emails = []
        self.phone_numbers = []

    def scrape(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.extract_contacts(response.text)
        else:
            print(f'Failed to retrieve {self.url}')

    def extract_contacts(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        # Extract names (simple regex for demonstration)
        self.names += re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', soup.get_text())

        # Extract emails
        self.emails += re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', soup.get_text())

        # Extract phone numbers (simple pattern for demo)
        self.phone_numbers += re.findall(r'\+?[0-9][0-9\s()-]{7,}[0-9]', soup.get_text())

    def get_contacts(self):
        return {'names': self.names, 'emails': self.emails, 'phone_numbers': self.phone_numbers}

# Example usage
# scraper = ContactScraper('https://example.com')
# scraper.scrape()
# print(scraper.get_contacts())