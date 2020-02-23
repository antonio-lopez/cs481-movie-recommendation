"""
# demo
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ["London Paris London","Paris Paris London"]
cv = CountVectorizer()

count_matrix = cv.fit_transform(text)

#print count_matrix.toarray()
similarity_scores = cosine_similarity(count_matrix)

print(similarity_scores)
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#======== Helper Functions =============
def get_title_from_index(index):
	return dataset[dataset.index == index]["title"].values[0]

def get_index_from_title(title):
	return dataset[dataset.title == title]["index"].values[0]

"""Step 1: Read CSV File"""
dataset = pd.read_csv("movie_dataset.csv")
#print(df.columns) # all columns containing a movies' properties

"""Step 2: Select Movie Properties"""
properties = ['keywords', 'cast', 'genres', 'director']

"""Step 3: Create a column in dataset which combines all selected properties"""
for movie_property in properties:
    dataset[movie_property] = dataset[movie_property].fillna('')    # fill in NaN with empty string

def combine_properties(row):
    try:
        return row['keywords'] +" "+ row['cast'] +" "+ row['genres'] +" "+ row['director']
    except:
        print("Error:", row)
dataset["combined_properties"] = dataset.apply(combine_properties, axis=1)  # combine vertically
# print("Combined Properties: ", dataset["combined_properties"].head())

"""Step 4: Create count matrix from this new combined column"""
cv = CountVectorizer()
count_matrix = cv.fit_transform(dataset["combined_properties"])

"""Step 5: Compute the Cosine Similarity based on the count_matrix"""
similarity_scores = cosine_similarity(count_matrix)

"""Step 6: Get index of movie sample from its title"""
movie_user_likes = "Avatar"
movie_index = get_index_from_title(movie_user_likes)

"""Step 7: Get a list of similar movies in descending order of similarity score"""
similar_movies = list(enumerate(similarity_scores[movie_index]))    # convert to list of tuples
sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True) # sort by similarity scores

"""Step 8: Print titles of first 50 movies"""
i = 0
for movie in sorted_similar_movies:
    print(get_title_from_index(movie[0]))
    i=i+1
    if i>50:
        break
