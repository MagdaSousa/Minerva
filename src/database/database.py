from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.database.settings import DBSettings

Base = declarative_base()


class DBConnection:
    def __init__(self):
        self.settings = DBSettings()
        self.database_url = "'postgres+psycopg2://{0}:{1}@{2}:{3}/{4}'".format(
            self.settings.db_user,
            self.settings.db_password,
            self.settings.db_host,
            self.settings.db_port,
            self.settings.db_database_name
        )
        self.engine = self.establishing_connection()
        self.sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def establishing_connection(self):
        return create_engine(url=self.database_url)

    def get_db(self):
        db = self.sessionLocal()
        try:
            yield db
        finally:
            db.close()
