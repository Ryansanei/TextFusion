import re
from datetime import datetime

class RegexExtractor:
    """
    A class to perform regex-based validation for common patterns
    such as URLs, phone numbers, emails, and dates.
    """

    def __init__(self):
        """
        Initialize patterns for URL, phone number, email, and date validation.
        """
        self.url_pattern = (
            r'(https?:\/\/)?(www\.)?([a-zA-Z0-9._-]+)\.(com|org|net|info|biz|co|io|me|tech|store|design|online|blog|website|site|app|tv|dev|us|xyz)(\/[^\s]*)?'
        )

        self.phone_pattern = (
            r'(\+1\s?)?(\(?\d{3}\)?[-.\s]?)(\d{3})[-.\s]?(\d{4})'
        )

        self.email_pattern = (
            r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        )

        self.date_pattern = (
            r'(?:0[1-9]|[12][0-9]|3[01])[-/](?:0[1-9]|1[0-2])[-/](?:19|20)\d{2}|'
            r'(?:0[1-9]|1[0-9])[-/](?:0[1-9]|[12][0-9]|3[01])[-/](?:19|20)\d{2}'
        )

    def is_valid_url(self, url):
        """Validate URL format"""
        return re.match(self.url_pattern, url) is not None

    def is_valid_phone(self, phone):
        """Validate USA phone number"""
        return re.match(self.phone_pattern, phone) is not None

    def is_valid_email(self, email):
        """Validate Email address"""
        return re.match(self.email_pattern, email) is not None

    def is_valid_date(self, date_str):
        """
        Validate Date in DD-MM-YYYY or MM-DD-YYYY formats and check for leap years.
        """
        if re.match(self.date_pattern, date_str):
            try:
                datetime.strptime(date_str, '%d-%m-%Y')
                return True
            except ValueError:
                try:
                    datetime.strptime(date_str, '%m-%d-%Y')
                    return True
                except ValueError:
                    return False
        return False

    def extract_data(self, text):
        """
        Extract all valid emails, URLs, phone numbers, and dates from the provided text.
        Also classify URLs based on their TLD.
        """
        emails = re.findall(self.email_pattern, text)
        urls = re.findall(self.url_pattern, text)
        phones = re.findall(self.phone_pattern, text)
        dates = re.findall(self.date_pattern, text)

        # Rebuild the phone numbers with the correct country code if missing
        full_phones = ['+1 ' + ''.join(phone).strip() if not phone[0] else ''.join(phone) for phone in phones]

        # Extract and filter complete URLs
        filtered_urls = [''.join([url[0] or '', url[1] or '', url[2], '.', url[3], url[4] or '']) for url in urls]

        # Remove URLs that match email domains
        filtered_urls = [url for url in filtered_urls if not any(email.split('@')[1] in url for email in emails)]

        # Map URLs to purposes based on TLD
        url_purposes = {}
        tld_purposes = {
            "com": "Commercial businesses",
            "org": "Non-profit organizations",
            "net": "Network services",
            "info": "Informational sites",
            "biz": "Business",
            "co": "Companies and organizations",
            "io": "Technology startups and software companies",
            "me": "Personal websites",
            "tech": "Technology-related sites",
            "store": "E-commerce",
            "design": "Design websites",
            "online": "Online presence",
            "blog": "Blogs",
            "website": "General websites",
            "site": "General sites",
            "app": "Applications",
            "tv": "Entertainment",
            "dev": "Developer-oriented",
            "us": "US-based",
            "xyz": "General use"
        }

        for url in filtered_urls:
            tld_match = re.search(r'\.(\w+)$', url)
            if tld_match:
                tld = tld_match.group(1)
                url_purposes[url] = tld_purposes.get(tld, "Unknown")

        return {
            "emails": emails,
            "urls": filtered_urls,
            "phones": full_phones,
            "dates": dates,"url_purposes": url_purposes
        }