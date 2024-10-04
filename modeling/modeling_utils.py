from sklearn.datasets import fetch_20newsgroups

def load_newsgroups_dataset(categories=None):
    """
    Load the 20 Newsgroups dataset.

    Args:
        categories (list): Optional list of categories to filter the dataset.

    Returns:
        tuple: Documents and target labels.
    """
    newsgroups = fetch_20newsgroups(subset='all', categories=categories, remove=('headers', 'footers', 'quotes'))
    return newsgroups.data, newsgroups.target