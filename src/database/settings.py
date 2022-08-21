import os


class DBSettings:
    def __init__(self):
        self.db_user = os.getenv('POSTGRES_USER')
        self.db_password = os.getenv('POSTGRES_PASSWORD')
        self.db_host = os.getenv('DATABASE_HOST')
        self.db_port = os.getenv('DATABASE_PORT')
        self.db_database_name = os.getenv('POSTGRES_DB')


