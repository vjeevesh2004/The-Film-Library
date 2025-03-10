# -*- coding: utf-8 -*-
"""Netflix.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13j9UaxxAmdLgQPnhkKJKa6sC3iBjqns6
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd

file_path = "/content/netflix_titles.csv"
df = pd.read_csv(file_path)

df["director"] = df["director"].fillna("Unknown")

df["cast"] = df["cast"].fillna("Unknown")

df["country"] = df["country"].fillna(df["country"].mode()[0])

df["date_added"] = df["date_added"].fillna(df["date_added"].mode()[0])

df["rating"] = df["rating"].fillna(df["rating"].mode()[0])

df["duration"] = df["duration"].fillna(df["duration"].mode()[0])

output_file = "/content/netflix_titles_sorted.csv"
df.to_csv(output_file, index=False)

print("File saved at:", output_file)