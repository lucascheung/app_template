from server.config.config import IS_DEV
from server.common.constants import *

if IS_DEV:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    PREFERRED_URL_SCHEME='http'
else:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PREFERRED_URL_SCHEME = 'https'
