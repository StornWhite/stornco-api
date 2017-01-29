# Local development environment settings
from .base import *

# Security

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True