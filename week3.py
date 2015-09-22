import numpy as np
import week2
import pandas
from scipy.optimize import newton
from sklearn.linear_model import LogisticRegression
import math


def solve_matrix(filename):
    mat = np.matrix(week2.read_matrix(filename))
    A = np.matrix(mat[:, range(len(mat))])
    last_column = np.array(mat[:, len(mat)])

    return np.linalg.solve(A, last_column)


def roots(filename):
    points = np.matrix(week2.read_matrix(filename))

    x = np.asarray(points[:, 0]).squeeze()
    y = np.asarray(points[:, 1]).squeeze()

    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)

    root = newton(f, 0)

    return root


def panda_movie_merge():
    movies = pandas.read_table('movies.dat', sep='::', names=['movie id', 'title', 'genre'])
    ratings = pandas.read_table('ratings.dat', sep='::', names=['user id', 'movie id', 'rating', 'timestamp'])
    users = pandas.read_table('users.dat', sep='::', names=['user id', 'gender', 'age', 'occupation code', 'zip'])

    return movies.merge(
        ratings.merge(users, on='user id'),
        on='movie id'
    )


def panda_top_movies(movie_data):
    group_by_movie = movie_data.groupby(['movie id'])
    ratings_by_movie = group_by_movie['rating'].agg({'rating count': sum})

    top_five = ratings_by_movie.sort(columns='rating count', ascending=False).iloc[0:5]
    active_titles = ratings_by_movie[ratings_by_movie['rating count'] >= 250]

    #print top_five
    #print active_titles

    movies_ratings = movie_data.merge(active_titles.reset_index(), on='movie id')
    # filter gender
    female_ratings = movies_ratings[movies_ratings['gender'].isin(['F'])]
    male_ratings = movies_ratings[movies_ratings['gender'].isin(['M'])]

    print female_ratings.groupby(['movie id'])['rating'].agg(['mean']).sort(columns='mean', ascending=False).iloc[0:3]


def bag_prediction(bag):
    training_data = bag[:-int(math.floor(len(bag)*0.1))]
    test_data = bag[-int(math.ceil(len(bag)*0.1)):]
    dataset = [row[:-1] for row in training_data]
    t_vec = [row[-1] for row in training_data]

    classifier = LogisticRegression().fit(dataset, t_vec)

    test_dataset = [row[:-1] for row in test_data]
    test_t_vec = [row[-1] for row in test_data]

    return classifier.predict(test_dataset), classifier.score(test_dataset, test_t_vec)

if "__main__" == __name__:
    # print solve_matrix("matrix3")
    # print roots("ENyYffaq.txt")
    # print roots('ENyYffaq.txt')
    # movie_data = panda_movie_merge()
    # panda_top_movies(movie_data)
    pizza_bag = week2.bag_of_words("pizza-train.json", limit=None)
    print bag_prediction(pizza_bag)