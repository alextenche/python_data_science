import pandas as pd

# imdb_ratings = pd.read_csv('http://bit.ly/imdbratings')
# imdb_ratings.to_csv('data/imdb_ratings.csv', sep=',', index=False)

imdb_movies = pd.read_csv('data/imdb_ratings.csv')
print(imdb_movies.head())

print(imdb_movies.describe())

print(imdb_movies.shape)

print(imdb_movies.dtypes)
