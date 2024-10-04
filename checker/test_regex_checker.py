from checker import RegexChecker

# Initialize the RegexChecker class
checker = RegexChecker()

# Sample data to validate
sample_url = "https://www.example.com"
invalid_url = "htp:/invalid-url"

sample_phone = "+1 (405) 456-7890"
invalid_phone = "123"

sample_email = "user@example.com"
invalid_email = "invalid-email"

sample_date = "25-12-2024"
invalid_date = "31-02-2024"

# Validate URL
print(f"URL '{sample_url}' is valid: {checker.is_valid_url(sample_url)}")
print(f"URL '{invalid_url}' is valid: {checker.is_valid_url(invalid_url)}")

# Validate phone number
print(f"Phone '{sample_phone}' is valid: {checker.is_valid_phone(sample_phone)}")
print(f"Phone '{invalid_phone}' is valid: {checker.is_valid_phone(invalid_phone)}")

# Validate email address
print(f"Email '{sample_email}' is valid: {checker.is_valid_email(sample_email)}")
print(f"Email '{invalid_email}' is valid: {checker.is_valid_email(invalid_email)}")

# Validate date
print(f"Date '{sample_date}' is valid: {checker.is_valid_date(sample_date)}")
print(f"Date '{invalid_date}' is valid: {checker.is_valid_date(invalid_date)}")