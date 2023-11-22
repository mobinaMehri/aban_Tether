from migration import Database


class MovieServices:
    def insert(self, title, genre, release_date):
        query = """
        INSERT INTO movies (title, genre, release_date)
        VALUES (%s, %s, %s)
        """
        values = (title, genre, release_date)
        db = Database()
        db.connect()
        db.execute(query, values)
        db.close_connection()

    def update(self, movie_id, title, genre, release_date):
        query = """
        UPDATE movies
        SET title = %s, genre = %s, release_date = %s
        WHERE id = %s
        """
        values = (title, genre, release_date, movie_id)
        db = Database()
        db.connect()
        db.execute(query, values)
        db.close_connection()

    def delete(self, movie_id):
        query = "DELETE FROM movies WHERE id = %s"
        values = movie_id
        db = Database()
        db.connect()
        db.execute(query, values)
        db.close_connection()

    def get_all(self):
        query = "SELECT * FROM movies"
        db = Database()
        db.connect()
        result = db.fetchall(query)
        db.close_connection()
        return result

    def get_by_id(self, movie_id):
        query = f"SELECT * FROM movies WHERE id = {movie_id}"
        db = Database()
        db.connect()
        result = db.fetchone(query)
        db.close_connection()
        return result


class PersonServices:
    def insert(self, name, age):
        query = """
        INSERT INTO persons (name, age)
        VALUES (%s, %s)
        """
        values = (name, age)
        db = Database()
        db.connect()
        db.execute(query, values)
        db.close_connection()

    def update(self, name, age, person_id):
        query = """
        UPDATE persons
        SET name = %s, age = %s
        WHERE id = %s
        """
        values = (name, age, person_id)
        db = Database()
        db.connect()
        db.execute(query, values)
        db.close_connection()

    def delete(self, person_id):
        query = "DELETE FROM persons WHERE id = %s"
        values = person_id
        db = Database()
        db.connect()
        db.execute(query, values)
        db.close_connection()

    def get_all(self):
        query = "SELECT * FROM persons"
        db = Database()
        db.connect()
        result = db.fetchall(query)
        db.close_connection()
        return result

    def get_by_id(self, person_id):
        query = f"SELECT * FROM persons WHERE id = {person_id}"
        db = Database()
        db.connect()
        result = db.fetchone(query)
        db.close_connection()
        return result


class CastPivotMovieServices:
    def insert(self, movie_id, person_id):
        query = """
        INSERT INTO cast_pivot_movie_table (movie_id, person_id)
        VALUES (%s, %s)
        """
        values = (movie_id, person_id)
        db = Database()
        db.connect()
        db.execute(query, values)
        db.close_connection()

    def get_all(self):
        query = '''
        SELECT *
        FROM persons AS p 
        JOIN cast_pivot_movie_table AS cpm
        ON p.id = cpm.person_id
        JOIN movies AS m
        ON m.id = cpm.movie_id
        '''
        db = Database()
        db.connect()
        result = db.fetchall(query)
        db.close_connection()
        return result

    def get_by_id(self, person_id):
        query = '''
        SELECT *
        FROM persons AS p 
        JOIN cast_pivot_movie_table AS cpm
        ON p.id = cpm.person_id
        JOIN movies AS m
        ON m.id = cpm.movie_id 
        WHERE p.id = {person_id}
        '''.format(person_id=person_id)
        db = Database()
        db.connect()
        result = db.fetchone(query)
        db.close_connection()
        return result


class DirectorPivotMovieServices:
    def insert(self, movie_id, person_id):
        query = """
        INSERT INTO director_pivot_movie_table (movie_id, person_id)
        VALUES (%s, %s)
        """
        values = (movie_id, person_id)
        db = Database()
        db.connect()
        db.execute(query, values)
        db.close_connection()

    def get_all(self):
        query = '''
        SELECT *
        FROM persons AS p
        JOIN director_pivot_movie_table AS dpm
        ON p.id = dpm.person_id
        JOIN movies AS m
        ON m.id = dpm.movie_id
        '''
        db = Database()
        db.connect()
        result = db.fetchall(query)
        db.close_connection()
        return result

    def get_by_id(self, person_id):
        query = '''
        SELECT *
        FROM persons AS p 
        JOIN director_pivot_movie_table AS dpm
        ON p.id = dpm.person_id
        JOIN movies AS m
        ON m.id = dpm.movie_id 
        WHERE p.id = {person_id}
        '''.format(person_id=person_id)
        db = Database()
        db.connect()
        result = db.fetchone(query)
        db.close_connection()
        return result

