from text_search import TextSearch

# Initialize the search class with the file path and a threshold for similarity score
file_path = 'test.txt'  # Path to your document
text_search = TextSearch(file_path, threshold=75)

# Query to search for
query = "Artificial Inteligence"

# Perform the search
matches, best_match, corrected_query = text_search.search(query)

# Display results
if matches:
    print(f"Best matches found (with score >= {text_search.threshold}):")
    for match, score in matches:
        print(f"Text: {match} | Similarity Score: {score}")
else:
    print(f"No exact matches found with score >= {text_search.threshold}.")

if corrected_query != query:
    print(f"Did you mean: '{corrected_query}'?")