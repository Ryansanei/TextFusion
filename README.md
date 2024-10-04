# **TextFusion**

**TextFusion** is a Python library for text processing, offering text search, topic modeling, and regex-based data extraction/validation. It enables document search, clustering, and format validation (URLs, emails, dates). Ideal for building text-centric applications with easy-to-use, powerful tools.
## Project Components

1.	**Text Search**

	• **Description:** This module provides document search functionality, which can be used to search through a document for specific keywords or patterns.
	• **Main Files:**
	• document_search.py: Contains the logic for searching text within a document.
	• DocumentSearch_demo.py: Demonstrates how to use the document search capabilities.
	• test.txt: A sample text file for testing search functionality.



2.	**Topic Modeling**

	• Description: This module offers topic modeling capabilities, using techniques like LDA (Latent Dirichlet Allocation) to discover hidden topics in documents.
	• Main Files:
	• topic_modeling.py: Contains the core topic modeling logic.
	• TopicModeling_demo.py: A demo file to showcase how topic modeling can be performed using the module.



3.	**Regex Checker**

	• Description: The regex checker module provides functionality to validate various types of inputs such as URLs, phone numbers, emails, and dates using regular expressions.
	• Main Files:
	• checker.py: Includes the RegexChecker class for validating different input types.
	• test_checker.py: Test cases for validating the functionality of RegexChecker.



4. **Regex Extractor**

	• Description: The regex extractor module allows for the extraction of data (such as emails, URLs, phone numbers, and dates) from raw text input. It also classifies URLs based on their top-level domain (TLD).
	• Main Files:
	• extractor.py: Contains the RegexExtractor class to extract and validate data.
	• test_extractor.py: Test cases for validating the functionality of RegexExtractor.



## Getting Started

### Installation

**1.	Clone the repository:**
	
`git clone https://github.com/your-repo/TextFusion.git` 
      
**2 .	Navigate to the project directory:**

`cd TextFusion`

**3.     Install required dependencies (if any):**
       `pip install -r requirements.txt`
       

#### Usage

**1.	Text Search:**
To perform document search, use DocumentSearch_demo.py to see a demonstration.

**2.	Topic Modeling:**
Execute TopicModeling_demo.py to explore topic modeling on sample text data.

**3.	Regex Checker:**
Use the RegexChecker class to validate URLs, phone numbers, emails, and dates.

```
from regex_checker.checker import RegexChecker
checker = RegexChecker()
valid_url = checker.is_valid_url("https://example.com")
```



**4.	Regex Extractor:**
Extract emails, URLs, phone numbers, and dates from text using RegexExtractor.


```
from regex_extractor.extractor import RegexExtractor
extractor = RegexExtractor()
data = extractor.extract_data("Sample text with a URL: https://example.com and an email: example@example.com")
print(data)
```

#### Testing

To run tests, you can execute the corresponding test files for each module:

`python -m unittest discover`


	
