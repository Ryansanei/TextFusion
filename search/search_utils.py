import spacy
from rapidfuzz import process, fuzz

def preprocess_text_spacy(text, nlp):
    """
    Preprocess and tokenize the text using spaCy: lemmatize and lowercase.

    Args:
        text (str): Input text for preprocessing.
        nlp (spacy.Language): spaCy language model.

    Returns:
        str: Preprocessed text with lemmatized words, excluding stopwords and punctuation.
    """
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_punct and not token.is_stop]
    return ' '.join(tokens)


def load_document_phrases(file_path, nlp):
    """
    Load phrases from a document by tokenizing the sentences and removing stopwords and punctuation.

    Args:
        file_path (str): Path to the document.
        nlp (spacy.Language): spaCy language model.

    Returns:
        list: List of preprocessed phrases from the document.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        document_text = file.read()
        doc = nlp(document_text)
        phrases = []
        for sent in doc.sents:
            phrase = ' '.join([token.lemma_ for token in sent if not token.is_stop and not token.is_punct])
            if phrase.strip():
                phrases.append(phrase.strip())
        return phrases


def find_spelling_correction(query, words_set):
    """
    Suggest spelling corrections for individual words in a query.

    Args:
        query (str): Original query text.
        words_set (set): Set of words extracted from the document for comparison.

    Returns:
        str: Corrected query, if any spelling mistakes are detected.
    """
    query_tokens = query.split()
    corrected_tokens = []

    for token in query_tokens:
        correction = process.extractOne(token, words_set, scorer=fuzz.ratio)
        if correction and correction[1] >= 80 and correction[0] != token:
            corrected_tokens.append(correction[0])
        else:
            corrected_tokens.append(token)

    return ' '.join(corrected_tokens)