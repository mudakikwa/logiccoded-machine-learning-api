# started the ml model
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from termcolor import colored

app = Flask(__name__)


@app.route("/query", methods=["POST", "GET"])
def getCode():
    if(request.method == 'POST'):
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
                return df.loc[df['number'] == index]["code"].values[0]
            except Exception:
                pass

        def get_index_from_title(title):
            index = df.index
            return index[df["title"] == title].values[0]+1

        code_title = request.form["query"]
        code_index = get_index_from_title(code_title)
        similar_code = list(enumerate(cosine_sim[code_index]))
        sorted_code = sorted(similar_code, key=lambda x: x[1], reverse=True)
        print(sorted_code[0][0])
        return jsonify({"query": get_code_from_index(sorted_code[0][0])})

    return "<h1>Welcome </h1>"
