from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
Base = declarative_base()

DB_USER = os.getenv('user')
DB_PASSWORD = os.getenv('password')
DB_HOST = os.getenv('host')
DB_PORT = os.getenv('port')
DB_DATABASE_NAME = os.getenv('database')

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE_NAME
)


class DatabaseConnection:
    def __init__(self):
        self.engine = self.establishing_connection()
        self.sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def establishing_connection(self):
        return create_engine(url=SQLALCHEMY_DATABASE_URL)

    def get_db(self):
        db = self.sessionLocal()
        try:
            yield db
        finally:
            db.close()
