import numpy as np
import week2
import pandas
from scipy.optimize import newton


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

    movies_ratings = movie_data.merge(active_titles.reset_index(), on='movie id')
    # filter gender
    female_ratings = movies_ratings[movies_ratings['gender'].isin(['F'])]
    male_ratings = movies_ratings[movies_ratings['gender'].isin(['M'])]

    top_3_female_ratings = (
        female_ratings
        .groupby(['movie id'])['rating']
        .agg(['mean'])
        .sort(columns='mean', ascending=False)
        .iloc[0:3]
    )
    top_3_male_ratings = (
        male_ratings
        .groupby(['movie id'])['rating']
        .agg(['mean'])
        .sort(columns='mean', ascending=False)
        .iloc[0:3]
    )

    gender_means = (
        female_ratings
        .groupby(['movie id'])['rating']
        .agg(['mean'])
        .reset_index()
        .merge(
            (
                male_ratings
                .groupby(['movie id'])['rating']
                .agg(['mean'])
                .reset_index()
            ),
            on='movie id'
        )
    )

    gender_means['mean_diff'] = gender_means['mean_x'] - gender_means['mean_y']
    gender_means_diff_sorted = gender_means.sort(columns='mean_diff', ascending=False)

    top_10_female_mean_diff = gender_means_diff_sorted.iloc[0:10]
    top_10_male_mean_diff = gender_means_diff_sorted.iloc[-10:].sort(columns='mean_diff', ascending=True)

    top_5_std_rating = (
        movies_ratings
        .groupby(['movie id'])['rating']
        .agg(['std'])
        .sort(columns='std', ascending=False)
        .iloc[0:5]
    )

    return (
        top_five,
        active_titles,
        top_3_female_ratings,
        top_3_male_ratings,
        top_10_female_mean_diff,
        top_10_male_mean_diff,
        top_5_std_rating
    )


if "__main__" == __name__:
    #print solve_matrix("matrix3")
    #print roots("ENyYffaq.txt")
    movie_data = panda_movie_merge()
    panda_top_movies(movie_data)