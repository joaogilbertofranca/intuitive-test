import psycopg2
from psycopg2 import pool

class Database:
    def __init__(self):
        self.pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dbname="intuitive",
            user="root",
            password="root",
            host="localhost",
            port="5432"
        )
        if not self.pool:
            raise Exception("Erro ao criar o pool de conexões")

    def get_connection(self):
        return self.pool.getconn()

    def release_connection(self, conn):
        self.pool.putconn(conn)

    def close_pool(self):
        self.pool.closeall()


db = Database()
