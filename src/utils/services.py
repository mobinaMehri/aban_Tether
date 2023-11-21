import psycopg2


class MoviesServices:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="mobina",
            port=5432,
        )
        self.cursor = self.conn.cursor()

    def insert(self, title, genre, release_date):
        query = """
        INSERT INTO movies (title, genre, release_date)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (title, genre, release_date))
        self.conn.commit()

    def update(self, movie_id, title, genre, release_date):
        query = """
        UPDATE movies
        SET title = %s, genre = %s, release_date = %s
        WHERE id = %s
        """
        self.cursor.execute(query, (title, genre, release_date, movie_id))
        self.conn.commit()

    def delete(self, movie_id):
        query = """
        DELETE FROM movies
        WHERE id = %s
        """
        self.cursor.execute(query, (movie_id,))
        self.conn.commit()

    def get_all(self):
        query = """
        SELECT * FROM movies
        """
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def get_by_id(self, movie_id):
        query = """
        SELECT * FROM movies
        WHERE id = %s
        """
        self.cursor.execute(query, (movie_id,))
        row = self.cursor.fetchone()
        return row

    def close_connection(self):
        self.cursor.close()
        self.conn.close()