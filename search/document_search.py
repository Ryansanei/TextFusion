import spacy
from rapidfuzz import process, fuzz
from search.search_utils import preprocess_text_spacy, load_document_phrases, find_spelling_correction


class TextSearch:
    """Class for performing text search and fuzzy matching on documents."""

    def __init__(self, file_path, threshold=75):
        """
        Initialize the TextSearch object by loading a document and setting a threshold.

        Args:
            file_path (str): Path to the document for searching.
            threshold (int): Minimum similarity score for matching. Default is 75.
        """
        self.nlp = spacy.load('en_core_web_sm')
        self.file_path = file_path
        self.threshold = threshold
        self.phrases = self._load_phrases()
        self.document_words = self._build_word_set()

    def _load_phrases(self):
        """Load the document and extract relevant phrases."""
        return load_document_phrases(self.file_path, self.nlp)

    def _build_word_set(self):
        """Build a set of words from the document to check for spelling corrections."""
        return set(word for phrase in self.phrases for word in phrase.split())

    def search(self, raw_query):
        """
        Search the document for the best matching phrases for a given query.

        Args:
            raw_query (str): The query to search in the document.

        Returns:
            tuple: A tuple containing a list of best matches and the single best match.
        """
        query = preprocess_text_spacy(raw_query, self.nlp)

        # Find the best matches
        matches, best_match = self._search_document(query)

        # Suggest spelling correction if necessary
        corrected_query = find_spelling_correction(raw_query, self.document_words)

        return matches, best_match, corrected_query

    def _search_document(self, query):
        """
        Perform fuzzy matching between the query and phrases from the document.

        Args:
            query (str): Preprocessed query.

        Returns:
            tuple: List of matches above the threshold and the single best match.
        """
        best_matches = []

        # Fuzzy match using partial ratio
        results = process.extract(query, self.phrases, scorer=fuzz.partial_ratio)

        # Filter results based on threshold score
        filtered_results = [(result[0], result[1]) for result in results if result[1] >= self.threshold]
        best_matches.extend(filtered_results)

        # Get the best match
        best_match = process.extractOne(query, self.phrases, scorer=fuzz.partial_ratio)

        return best_matches, best_match