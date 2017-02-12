# Local development environment settings
from .base import *

# Security

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True

# CORS - cross origin resource sharing
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'null',
    '127.0.0.1:8000',
)
CORS_ALLOW_CREDENTIALS = True