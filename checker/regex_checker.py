import re
from datetime import datetime


class RegexChecker:
    """
    A class to validate various types of inputs such as URLs, phone numbers,
    email addresses, and dates using regular expressions.
    """

    def __init__(self):
        # URL pattern to match common URL formats (http, https, with or without 'www')
        self.url_pattern = (
            r'^(https?:\/\/)?'                 # Optional protocol (http or https)
            r'(([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,})' # Domain name
            r'(:\d+)?'                        # Optional port number
            r'(\/[^\s]*)?$'                   # Optional path
        )

        # USA phone number pattern that matches a variety of formats
        self.phone_pattern = (
            r'^(\+1\s?)?'                     # Optional country code (+1)
            r'(\(?\d{3}\)?[-.\s]?)'           # Area code (with or without parentheses)
            r'\d{3}[-.\s]?\d{4}$'             # The rest of the phone number (7 digits)
        )

        # Email pattern for standard email formats
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Date pattern to support DD-MM-YYYY and MM-DD-YYYY formats
        self.date_pattern = (
            r'^(?:0[1-9]|[12][0-9]|3[01])[-/](?:0[1-9]|1[0-2])[-/](?:19|20)\d{2}$|'  # DD-MM-YYYY
            r'(?:0[1-9]|1[0-2])[-/](?:0[1-9]|[12][0-9]|3[01])[-/](?:19|20)\d{2}$'    # MM-DD-YYYY
        )

    def is_valid_url(self, url: str) -> bool:
        """
        Validate if the given string is a valid URL.

        :param url: The URL string to validate.
        :return: True if valid, False otherwise.
        """
        return re.match(self.url_pattern, url) is not None

    def is_valid_phone(self, phone: str) -> bool:
        """
        Validate if the given string is a valid USA phone number.

        :param phone: The phone number string to validate.
        :return: True if valid, False otherwise.
        """
        return re.match(self.phone_pattern, phone) is not None

    def is_valid_email(self, email: str) -> bool:
        """
        Validate if the given string is a valid email address.

        :param email: The email address string to validate.
        :return: True if valid, False otherwise.
        """
        return re.match(self.email_pattern, email) is not None

    def is_valid_date(self, date_str: str) -> bool:
        """
        Validate if the given string is a valid date in DD-MM-YYYY or MM-DD-YYYY format.
        Also checks for leap year handling.

        :param date_str: The date string to validate.
        :return: True if valid, False otherwise.
        """
        if re.match(self.date_pattern, date_str):
            try:
                # First attempt to parse as DD-MM-YYYY
                datetime.strptime(date_str, '%d-%m-%Y')
                return True
            except ValueError:
                try:
                    # Then attempt to parse as MM-DD-YYYY
                    datetime.strptime(date_str, '%m-%d-%Y')
                    return True
                except ValueError:
                    return False
        return False
