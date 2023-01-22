import sqlite3

def get_all(query: str):
    """
    Получение списка всех  фильмов/сериалов из БД
    :param query:
    :return:
    """
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row

        result = []

        for item in connection.execute(query).fetchall():
            result.append(dict(item))

        return result


def get_one(query: str):
    """
    Получение одного фильма/сериала из БД
    :param query:
    :return:
    """
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(query).fetchone()

        return dict(result)
