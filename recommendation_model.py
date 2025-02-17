import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer


def movie_recommendations(df1, df2, title):
    # #! Demographic Filtering
    # C = df2["vote_average"].mean()
    # m = df2["vote_count"].quantile(0.9)
    # q_movies = df2.copy().loc[df2["vote_count"] >= m]

    # def weighted_rating(x, m=m, C=C):
    #     v = x["vote_count"]
    #     R = x["vote_average"]
    #     # Calculation based on the IMDB formula
    #     return (v / (v + m) * R) + (m / (m + v) * C)

    # # Define a new feature 'score' and calculate its value with `weighted_rating()`
    # q_movies["score"] = q_movies.apply(weighted_rating, axis=1)

    # # Sort movies based on score calculated above
    # q_movies = q_movies.sort_values("score", ascending=False)

    # # Print the top 15 movies
    # # q_movies[['title', 'vote_count', 'vote_average', 'score']].head(10)

    #! Content Based Filtering
    # Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
    tfidf = TfidfVectorizer(stop_words="english")

    # Replace NaN with an empty string
    df2["overview"] = df2["overview"].fillna("")

    # Construct the required TF-IDF matrix by fitting and transforming the data
    tfidf_matrix = tfidf.fit_transform(df2["overview"])

    # Compute the cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Construct a reverse map of indices and movie titles
    indices = pd.Series(df2.index, index=df2["title"]).drop_duplicates()

    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return df2["title"].iloc[movie_indices]
