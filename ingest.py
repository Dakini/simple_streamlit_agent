import pandas as pd
from minsearch import Index, VectorSearch
from sentence_transformers import SentenceTransformer
import numpy as np

embedding_model = SentenceTransformer("multi-qa-distilbert-cos-v1")


def load_data():
    return pd.read_csv("intelligent_chunking.csv").to_dict("records")


def create_vectors(data):
    embeddings = []

    for doc in data:
        text = doc["section"]
        v = embedding_model.encode(text)

        embeddings.append(v)
    return np.array(embeddings)


def create_vector_index(data):

    embeddings = create_vectors(data)
    index = VectorSearch()
    index.fit(embeddings, data)

    return index


def create_text_index(data):

    index = Index(text_fields=["filename", "section"], keyword_fields=[])
    index.fit(data)

    return index


def embed_query(query):
    return embedding_model.encode(query)


def index_data():
    data = load_data()
    text_index = create_text_index(data)
    vector_index = create_vector_index(data)

    return text_index, vector_index
