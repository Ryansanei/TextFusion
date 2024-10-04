from extractor import RegexChecker

# Initialize the checker
checker = RegexChecker()

# Sample text to extract data from
sample_text = """
You can contact me via email at example.email@test.com or visit my website at https://www.example.com. 
Feel free to call me at +1 (123) 456-7890 or (234) 567-8901. Let's schedule a meeting on 12/05/2023 or 05-12-2023.
Invalid URL examples: http:/invalid-url or www.invalid-site. Email examples: invalid-email@test, valid.email@domain.com
"""

# Extract data from the sample text
extracted_data = checker.extract_data(sample_text)

# Display the extracted information
print("Extracted Emails:", extracted_data.get("emails", []))
print("Extracted URLs:", extracted_data.get("urls", []))
print("Extracted Phone Numbers:", extracted_data.get("phones", []))
print("Extracted Dates:", extracted_data.get("dates", []))
print("URL Purposes:", extracted_data.get("url_purposes", {}))

# Individual validation tests
print("\nValidation Tests:")
print("Is 'https://www.example.com' a valid URL?", checker.is_valid_url("https://www.example.com"))
print("Is '+1 (123) 456-7890' a valid phone number?", checker.is_valid_phone("+1 (123) 456-7890"))
print("Is 'valid.email@domain.com' a valid email?", checker.is_valid_email("valid.email@domain.com"))
print("Is '31-02-2024' a valid date?", checker.is_valid_date("31-02-2024"))  # Invalid date
print("Is '12/05/2023' a valid date?", checker.is_valid_date("12/05/2023"))  # Valid date in MM-DD-YYYY