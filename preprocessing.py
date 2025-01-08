import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess_steps(df_credits, df_movies):

    df1 = df_credits
    df2 = df_movies

    df1.columns = ["id", "tittle", "cast", "crew"]
    df2 = df2.merge(df1, on="id")

    return df1, df2