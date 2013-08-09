import datetime

class DefaultConfig(object):
    DEFAULT_LANGUAGE = 'en_US'

    SECRET_KEY = 'superman'
    DEBUG = True

    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300

    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=1)

    # SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/printus.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://stephane:linux@localhost:5432/printus'
    SQLALCHEMY_ECHO = True

    PRINTUS_URL = 'http://printus.io'
