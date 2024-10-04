from modeling.topic_model import TopicModeling
from modeling_utils import load_newsgroups_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def run_topic_modeling():
    # Load dataset
    documents, _ = load_newsgroups_dataset()

    # Initialize the TopicModeling class
    topic_modeling = TopicModeling(documents)

    # Find the best number of topics and perform LDA
    best_num_topics = topic_modeling.find_best_num_topics()
    lda_model = topic_modeling.perform_lda(best_num_topics)

    # Display topics
    print("\nTopics identified using LDA:")
    for idx, topic in lda_model.print_topics(-1):
        print(f"Topic {idx}: {topic}")

    # Convert documents to a TF-IDF matrix
    vectorizer = TfidfVectorizer(tokenizer=lambda doc: doc, lowercase=False)
    X = vectorizer.fit_transform(topic_modeling.processed_docs)

    # Find the best number of clusters
    best_num_clusters = topic_modeling.find_best_num_clusters(X)

    # Cluster documents
    clusters = topic_modeling.cluster_documents(best_num_clusters, X)

    # Display cluster assignments
    df = pd.DataFrame({'Document': documents, 'Cluster': clusters})

    # Print each document with its corresponding cluster
    print("\nDocument Clustering Results:")
    for i, row in df.iterrows():
        print(f"Document {i+1} is in Cluster {row['Cluster']}")

if __name__ == "__main__":
    run_topic_modeling()