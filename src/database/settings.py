from dotenv import dotenv_values


class DBSettings:
    def __init__(self):
        config = dotenv_values(".env")
        print('load settings', config)

        self.db_user = config.get('POSTGRES_USER')
        self.db_password = config.get('POSTGRES_PASSWORD')
        self.db_host = config.get('DATABASE_HOST')
        self.db_port = config.get('DATABASE_PORT')
        self.db_database_name = config.get('POSTGRES_DB')
