import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    f = open(MOVIE_DATA, 'r', encoding='utf-8')

    directors = defaultdict(list)

    reader = csv.DictReader(f)
    for row in reader:
        try:
            director_name = row['director_name']
            title = row['movie_title'].replace('\xa0', '')
            year = int(row['title_year'])
            score = float(row['imdb_score'])
            directors[director_name].append(Movie(title, year, score))
        except  ValueError:
            continue

    f.close()
    return directors

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate average score'''
    temp = defaultdict(list)
    for director_name, Movie in directors.items():
        Movie.sort(key=lambda Movie: Movie.score, reverse=True)
        if len([movie for movie in Movie if movie.year >= 1960]) >= 4:
            temp[(director_name, _calc_mean(Movie))] = Movie
            #temp[director_name].append(_calc_mean(Movie))
    return temp

def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    movie_list = [movie.score for movie in movies]
    return round(sum(movie_list)/len(movie_list), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()