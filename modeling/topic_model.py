import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim import corpora
from gensim.models.ldamodel import LdaModel
from gensim.models import CoherenceModel
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_20newsgroups


class TopicModeling:
    """Class for performing topic modeling and clustering on a dataset."""

    def __init__(self, documents):
        """
        Initialize the TopicModeling object with a set of documents.

        Args:
            documents (list): List of raw text documents to analyze.
        """
        self.documents = documents
        self.processed_docs = self._preprocess_documents()
        self.dictionary = corpora.Dictionary(self.processed_docs)
        self.corpus = [self.dictionary.doc2bow(doc) for doc in self.processed_docs]

    def _preprocess_documents(self):
        """Preprocess the documents by removing stopwords and tokenizing."""
        nltk.download('punkt')
        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))

        def preprocess(text):
            words = word_tokenize(text.lower())
            return [word for word in words if word.isalpha() and word not in stop_words]

        return [preprocess(doc) for doc in self.documents]

    def find_best_num_topics(self, start=2, limit=10, step=1):
        """
        Find the best number of topics by computing coherence scores.

        Args:
            start (int): Starting number of topics.
            limit (int): Maximum number of topics to test.
            step (int): Step size between topic numbers.

        Returns:
            int: Best number of topics based on coherence score.
        """
        model_list, coherence_values = self._compute_coherence_values(start, limit, step)

        # Plot coherence score vs number of topics
        x = range(start, limit, step)
        plt.plot(x, coherence_values)
        plt.xlabel("Number of Topics")
        plt.ylabel("Coherence Score")
        plt.title("Coherence Score vs Number of Topics")
        plt.show()

        # Find the number of topics with the highest coherence score
        best_num_topics = x[coherence_values.index(max(coherence_values))]
        print(f"The best number of topics based on coherence score is: {best_num_topics}")
        return best_num_topics

    def _compute_coherence_values(self, start, limit, step):
        """Compute coherence values for different numbers of topics."""
        coherence_values = []
        model_list = []

        for num_topics in range(start, limit, step):
            model = LdaModel(corpus=self.corpus, id2word=self.dictionary, num_topics=num_topics, passes=15)
            model_list.append(model)
            coherence_model = CoherenceModel(model=model, texts=self.processed_docs, dictionary=self.dictionary,
                                             coherence='c_v')
            coherence_values.append(coherence_model.get_coherence())

        return model_list, coherence_values

    def perform_lda(self, num_topics):
        """
        Perform Latent Dirichlet Allocation (LDA) with the given number of topics.

        Args:
            num_topics (int): Number of topics to use in the LDA model.

        Returns:
            LdaModel: Trained LDA model.
        """
        lda_model = LdaModel(corpus=self.corpus, num_topics=num_topics, id2word=self.dictionary, passes=15)
        return lda_model

    def find_best_num_clusters(self, X, max_clusters=10):
        """
        Find the best number of clusters using the Elbow method and Silhouette Score.

        Args:
            X (sparse matrix): Document-term matrix (TF-IDF or similar).
            max_clusters (int): Maximum number of clusters to test.
        Returns:
                    int: Best number of clusters based on silhouette score.
                """
        wcss = []  # Within-cluster sum of squares for each k
        silhouette_scores = []  # Silhouette scores for each k
        range_clusters = range(2, max_clusters + 1)

        for k in range_clusters:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(X)
            wcss.append(kmeans.inertia_)  # Sum of squared distances
            silhouette_avg = silhouette_score(X, kmeans.labels_)
            silhouette_scores.append(silhouette_avg)

        # Plot Elbow Method results and Silhouette Scores
        self._plot_clustering_results(range_clusters, wcss, silhouette_scores)

        # Determine best number of clusters
        best_num_clusters = range_clusters[np.argmax(silhouette_scores)]
        print(f"The best number of clusters based on silhouette score is: {best_num_clusters}")
        return best_num_clusters

    def _plot_clustering_results(self, range_clusters, wcss, silhouette_scores):
        """Plot the Elbow Method results and Silhouette Scores."""
        plt.figure(figsize=(12, 6))

        # Elbow Method plot
        plt.subplot(1, 2, 1)
        plt.plot(range_clusters, wcss, marker='o')
        plt.title('Elbow Method: WCSS vs Number of Clusters')
        plt.xlabel('Number of clusters')
        plt.ylabel('WCSS')

        # Silhouette Score plot
        plt.subplot(1, 2, 2)
        plt.plot(range_clusters, silhouette_scores, marker='o')
        plt.title('Silhouette Score vs Number of Clusters')
        plt.xlabel('Number of clusters')
        plt.ylabel('Silhouette Score')

        plt.show()

    def cluster_documents(self, num_clusters, X):
        """
        Perform KMeans clustering on the documents.

        Args:
            num_clusters (int): Number of clusters to use in KMeans.
            X (sparse matrix): Document-term matrix (TF-IDF or similar).

        Returns:
            list: Cluster labels for each document.
        """
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(X)
        return kmeans.labels_