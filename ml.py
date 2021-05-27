import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from termcolor import colored

df = pd.read_csv("dataset.csv")
feature = ['title', 'Code Description', 'Functionality Language']


def extract_feuture(row):
    return row["title"]+" " + row["Code Description"]+" "+row["Functionality Language"]


for feature in feature:
    df[feature] = df[feature].fillna("")

df["combined_features"] = df.apply(extract_feuture, axis=1)
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)


def get_code_from_index(index):
    try:
        return print(df.loc[df['number'] == index]["code"].values[0])
    except Exception:
        pass


def get_index_from_title(title):
    index = df.index
    return index[df["title"] == title].values[0]+1


code_title = "Coion to database"
code_index = get_index_from_title(code_title)
similar_code = list(enumerate(cosine_sim[code_index]))
sorted_code = sorted(similar_code, key=lambda x: x[1], reverse=True)
i = 0
print(colored(''' ################################################################
################################################################
# ################################################################
# ################################################################''', "green"))
for element in sorted_code:
    print(colored(element[0], "red"))
    get_code_from_index(element[0])
    if(element[1] > 0.2):
        i = i+1

    if i > 0:
        break
