import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME', 'username')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'password')
    MYSQL_HOSTNAME = os.environ.get('MYSQL_HOSTNAME', 'localhost')
    MYSQL_DBNAME = os.environ.get('MYSQL_DBNAME', 'db_name')


    SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_DATABASE_URL') or \
        f'mysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DBNAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'root')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '1234')
    MONGO_HOSTNAME = os.environ.get('MONGO_HOSTNAME', 'localhost')
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'db_name')

    MONGO_URI = os.environ.get('MONGO_URI') or \
        f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOSTNAME}/{MONGO_DBNAME}'


    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'super-secret')
