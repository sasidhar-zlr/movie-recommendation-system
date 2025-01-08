import pandas as pd

from recommendation_model import movie_recommendations
from preprocessing import preprocess_steps

df_credits = pd.read_csv("tmdb_5000_credits.csv")
df_movies = pd.read_csv("tmdb_5000_movies.csv")

# df1, df2 = preprocess_steps(df_credits, df_movies)
# result = movie_recommendations(df1, df2, "The Dark Knight")
# print(result)


def get_recommendations(title):
    df1, df2 = preprocess_steps(df_credits, df_movies)
    return movie_recommendations(df1, df2, title)

# import pickle

# # Save the model
# with open('get_recommendations_model.pkl', 'wb') as f:
#     pickle.dump(get_recommendations, f)