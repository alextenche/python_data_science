import pandas as pd

orders = pd.read_table('http://bit.ly/chiporders')
print(orders.head())

# read from url
user_col = ['user_id', 'age', 'gender', 'occupation', 'zipcode']

movie_reviews = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_col)
print(type(movie_reviews))
print(movie_reviews.head())

# read from file
movie_reviews_from_file = pd.read_table('data/movie_reviews.csv', sep=',')
print(movie_reviews_from_file.head())

# save to csv
movie_reviews.to_csv('data/movie_reviews.csv', sep=',', index=False)
