import os
from dotenv import load_dotenv

load_dotenv()


HOST = os.getenv('HOST')
BASE_API_PREFIX = 'api/v1'

JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')


class PostgresqlConfig:
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    port = os.getenv('PORT')
    host = HOST
    database = os.getenv('DATABASE')
    prefix = 'Postgresql'

