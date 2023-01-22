from flask import Flask, jsonify
from utils import *


app = Flask(__name__)


@app.route('/movie/<title>')
def get_by_title(title: str):
    query = f"""
    SELECT * FROM netflix
    WHERE title = '{title}'     
    """

    query_result = get_one(query)

    movie = {
          "title": query_result["title"],
          "country": query_result["country"],
          "release_year": query_result["release_year"],
          "listed_in": query_result["listed_in"],
          "description": query_result["description"]
    }

    return jsonify(movie)


@app.route('/movie/<year1>/to/<year2>')
def get_by_year(year1: str, year2: str):
    query = f"""
        SELECT * FROM netflix
        WHERE release_year BETWEEN '{year1}'  AND '{year2}'
        LIMIT 100   
        """

    result = []

    for item in get_all(query):
        result.append(
            {
            "title": item["title"],
            "release_year": item["release_year"]
            }
        )

    return jsonify(result)


@app.route('/movie/rating/<value>')
def get_movie_by_rating(value: str):
    query = """
            SELECT * FROM netflix
            """

    if value == 'children':
        query += 'WHERE rating = "G"'
    elif value == 'family':
        query += 'WHERE rating = "G" OR rating = "PG" OR rating = "PG-13"'
    elif value == 'adult':
        query += 'WHERE rating = "R" OR rating = "NC-17"'

    result = []

    for item in get_all(query):
        result.append(
            {
                "title": item["title"],
                "rating": item["rating"],
                "description": item["description"]
            }
        )
    return jsonify(result)


@app.route('/movie/genre/<genre>')
def get_movie_by_genre(genre: str):
    query = f"""
            SELECT * FROM netflix
            WHERE listed_in = '{genre}'
            ORDER BY release_year DESC
            LIMIT 10
            """

    result = []

    for item in get_all(query):
        result.append(
            {
                "title": item["title"],
                "description": item["description"],
            }
        )

    return jsonify(result)


@app.route('/movie/cast/<actor>')
def get_by_cast(actor: str):
    query = f"""
        SELECT * FROM netflix
        WHERE netflix."cast" LIKE '%{actor}%'   
        """

    result = []

    for item in get_all(query):
        result.append(
            {
            "title": item["title"],
            "release_year": item["release_year"],
            "description": item["description"],
            "cast": item["cast"]
            }
        )

    return jsonify(result)


@app.route('/movie/<type>/<year>/<genre>')
def get_movie_by_type(type: str, year: str, genre: str):
    query = f"""
            SELECT * FROM netflix
            WHERE type = '{type}' AND release_year = '{year}' AND listed_in = '{genre}'
            """

    result = []

    for item in get_all(query):
        result.append(
            {
                "title": item["title"],
                "description": item["description"],
            }
        )

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)




