from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from src.database.settings import DBSettings
from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, Float, DATE, Table, insert, delete
from loguru import logger

Base = declarative_base()


class DBConnection:
    def __init__(self):
        self.settings = DBSettings()
        self.database_url = "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
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

    def insert_executor(self, table_name, values):
        try:
            with self.engine.connect() as conn:
                logger.info(f"{values}")
                conn.detach()
                query = insert(table_name).values(values)
                conn.execute(query)
        except Exception as error:
            raise logger.error(f"verifyinsert_executor {error}")

    def delete_executor(self, table_name, values):
        try:
            with self.engine.connect() as conn:
                logger.info(f"{values}")
                conn.detach()
                query = delete(table_name).values(values)
                conn.execute(query)
        except Exception as error:
            raise logger.error(f"verifyinsert_executor {error}")

    def get_db(self):
        db = self.sessionLocal()
        return db
        # try:
        #     yield db
        # finally:
        #    print("finalizei")
        # db.close()
