#Used libraries
from bertopic import BERTopic
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from bertopic.representation import MaximalMarginalRelevance
from sentence_transformers import SentenceTransformer
from bertopic.representation import KeyBERTInspired
from umap import UMAP
from hdbscan import HDBSCAN
import numpy as np
import re
import random
import matplotlib.pyplot as plt
import seaborn as sns

#Reading and defining files for the model
tvshows = pd.read_csv('filtered_dataset.csv')
docs = tvshows['text_window']
timestamps = tvshows['year']

#Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2", device='cpu')
embeddings = embedding_model.encode(docs, show_progress_bar=True)
umap_model = UMAP(n_neighbors=5, n_components=3, min_dist=0.006, metric='cosine', random_state=42, )
hdbscan_model = HDBSCAN(min_cluster_size=74, metric='euclidean', cluster_selection_method='leaf',)
vectorizer_model = CountVectorizer(stop_words="english", min_df=2, ngram_range=(1, 2))
representation_model = KeyBERTInspired()
model = BERTopic(
    embedding_model=embedding_model,
    umap_model=umap_model,
    hdbscan_model=hdbscan_model,
    vectorizer_model=vectorizer_model,
    representation_model=representation_model,
    
    # hyperparameters
    top_n_words=10,
    verbose=True
)
topics, probs = model.fit_transform(docs, embeddings)
