from dotenv import dotenv_values


class DBSettings:
    def __init__(self):
        config = dotenv_values(".env")
        print('load settings', config)

        self.db_user = config.get('POSTGRES_USER', 'magda')
        self.db_password = config.get('POSTGRES_PASSWORD', 'pg439')
        self.db_host = config.get('DATABASE_HOST', 'localhost')
        self.db_port = config.get('DATABASE_PORT', 5432)
        self.db_database_name = config.get('POSTGRES_DB', 'minerva')
