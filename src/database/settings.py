import os


class DBSettings:
    def __init__(self):
        self.db_user = os.getenv('user')
        self.db_password = os.getenv('password')
        self.db_host = os.getenv('host')
        self.db_port = os.getenv('port')
        self.db_database_name = os.getenv('database')

