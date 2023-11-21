import psycopg2


class Migration:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="mobina",
            port="5432"
        )
        self.cursor = self.conn.cursor()

    def create_movies_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS movies (
            id SERIAL PRIMARY KEY,
            title TEXT,
            genre TEXT,
            release_date INTEGER 
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def create_persons_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS persons (
            id SERIAL PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def create_pivot_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS pivot_table (
            movie_id INTEGER REFERENCES movies(id),
            person_id INTEGER REFERENCES persons(id),
            rating INTEGER,
            PRIMARY KEY (movie_id, person_id)
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


migration = Migration()
migration.create_movies_table()
migration.create_persons_table()
migration.create_pivot_table()
migration.close_connection()
