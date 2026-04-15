import re
import asyncio
from collections import defaultdict

class ContactScraper:
    def __init__(self, text):
        self.text = text

    async def extract_emails(self):
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, self.text)
        return list(set(emails))  # Remove duplicates

    async def extract_phone_numbers(self):
        phone_pattern = r'(?:(?:\+?\d{1,3}[ -]?)(?:\(?\d{1,4}?\)?[ -]?)?\d{1,4}[ -]?\d{1,4}[ -]?\d{1,9})'
        phone_numbers = re.findall(phone_pattern, self.text)
        return list(set(phone_numbers))  # Remove duplicates

    async def extract_names(self):
        # Simulating name extraction with a simple pattern (this could be refined)
        name_pattern = r'([A-Z][a-z]+(?: [A-Z][a-z]+)*)'
        names = re.findall(name_pattern, self.text)
        return list(set(names))  # Remove duplicates

    async def contact_stats(self):
        emails = await self.extract_emails()
        phone_numbers = await self.extract_phone_numbers()
        names = await self.extract_names()
        return {
            'email_count': len(emails),
            'phone_number_count': len(phone_numbers),
            'name_count': len(names),
            'emails': emails,
            'phone_numbers': phone_numbers,
            'names': names,
        }

# Example usage:
# scraper = ContactScraper(text)
# asyncio.run(scraper.contact_stats())
