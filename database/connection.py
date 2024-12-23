import psycopg2
from contextlib import contextmanager
from config.settings import DATABASE, HOST, USERSERVER, PASSWORD, PORT
from .db_interface import DBInterface

class PostgresConnection(DBInterface):
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = psycopg2.connect(database=DATABASE, host=HOST, user=USERSERVER, password=PASSWORD, port=PORT)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print('Conexão com PostgreSQL encerrada')

@contextmanager
def instance_cursor():
    db = PostgresConnection()
    db.connect()
    try:
        yield db
    finally:
        db.close()