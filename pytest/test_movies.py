import os
import random
import string
import sqlite3

import pytest

from movies import MovieDb

salt = ''.join(
    random.choice(string.ascii_lowercase) for i in range(20)
)
DB = os.path.join(os.getenv("TMP", "/tmp"), f'movies_{salt}.db')
# https://www.imdb.com/list/ls055592025/
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = 'movies'


@pytest.fixture
def db():
    # instantiate MovieDb class using above constants
    # do proper setup / teardown using MovieDb methods
    # https://docs.pytest.org/en/latest/fixture.html (hint: yield)
    movie_db = MovieDb(DB, DATA, TABLE)
    movie_db.init()
    yield movie_db
    movie_db.con.close()
    if os.path.exists(DB):
        os.remove(DB)

def test_query_move(db):
    movie = db.query(title='The Godfather', year=1972)
    assert movie == [(1, "The Godfather", 1972, 9.2)]


def test_query_by_year(db):
    movie = db.query(year=1994)
    assert movie == [(2, "The Shawshank Redemption", 1994, 9.3)]


def test_query_by_score(db):
    movies = db.query(score_gt=9)
    assert movies == [
        (1, "The Godfather", 1972, 9.2),
        (2, "The Shawshank Redemption", 1994, 9.3),
    ]


def test_query_without_filters_returns_all_rows(db):
    movies = db.query()
    assert len(movies) == len(DATA)

def test_add_movie(db):
    assert db.add('Romantic Love', 2026, 8) == 11

def test_delete_movie(db):
    db.delete(10)
    query = db.query("Lawrence of Arabia")
    assert query == []

def test_drop_table(db):
    db.drop_table()
    with pytest.raises(sqlite3.OperationalError):
        db.cur.execute(f"SELECT COUNT(*) FROM {TABLE}")

# write tests for all MovieDb's query / add / delete