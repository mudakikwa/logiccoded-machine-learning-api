import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df=pd.read_csv("movie_dataset.csv")
features = ['keywords', 'cast', 'genres', 'director']

def combine_features(row):
    return row['keywords']+' '+row['cast']+' '+row['genres']+' '+row['director']

for feature in features:
    df[feature]=df[feature].fillna("")
df["combined_features"]=df.apply(combine_features,axis=1)
cv=CountVectorizer()
counter_matrix=cv.fit_transform(df["combined_features"])
cosine_sim=cosine_similarity(counter_matrix)

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title == title]["index"].value[0]
    
