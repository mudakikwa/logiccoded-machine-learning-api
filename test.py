from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
text = ["London Paris London", "Paris Paris London"]
cv=CountVectorizer()
count_matrix=cv.fit_transform(text)
print(cv.get_feature_names())
print(count_matrix.toarray())
similarity_score=cosine_similarity(count_matrix)
print(similarity_score)

