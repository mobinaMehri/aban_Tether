import psycopg2


class Database:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'postgres'
        self.user = 'postgres'
        self.password = 'mobina'
        self.port = '5432'
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            print(f"Error connect: {e}")

    def execute(self, query, values=None):
        try:
            if values:
                self.cursor.execute(query, values)
                self.connection.commit()
            else:
                self.cursor.execute(query)
                self.connection.commit()
        except psycopg2.Error as e:
            print(f"Error execute: {e}")

    def fetchall(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error execute: {e}")

    def fetchone(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except psycopg2.Error as e:
            print(f"Error execute: {e}")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


class Migration:
    def create_movies_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS movies (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            genre VARCHAR(255),
            release_date date 
        )
        """
        db = Database()
        db.connect()
        db.execute(query)
        db.close_connection()

    def create_persons_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS persons (
            id SERIAL PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
        """
        db = Database()
        db.connect()
        db.execute(query)
        db.close_connection()

    def create_cast_pivot_movie_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS cast_pivot_movie_table (
            id SERIAL PRIMARY KEY,
            movie_id INTEGER REFERENCES movies(id),
            person_id INTEGER REFERENCES persons(id),
        )
        """
        db = Database()
        db.connect()
        db.execute(query)
        db.close_connection()

    def create_director_pivot_movie_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS director_pivot_movie_table (
            id SERIAL PRIMARY KEY,
            movie_id INTEGER REFERENCES movies(id),
            person_id INTEGER REFERENCES persons(id),
        )
        """
        db = Database()
        db.connect()
        db.execute(query)
        db.close_connection()

    def migrate(self):
        self.create_persons_table()
        self.create_movies_table()
        self.create_cast_pivot_movie_table()
        self.create_director_pivot_movie_table()


if __name__ == '__main__':
    m = Migration()
    m.migrate()
