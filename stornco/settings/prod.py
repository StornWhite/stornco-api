# Production environment settings
import os
from .base import *

# For security:

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
# Todo: Reset allowed hosts to '.storn.co'
ALLOWED_HOSTS = [
    '.*.*'
]

# CORS - cross origin resource sharing
# Todo: Further restrict when we are able to attach front end to dev enviros
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'null',
    '127.0.0.1:8000',
    'www.storn.co',
    'www.storn.co.s3-website-us-west-1.amazonaws.com/'
)
CORS_ALLOW_CREDENTIALS = True

# Static file stuff:

# Production static file directories are relative to:
STATIC_ROOT = "stornco-prod-static.s3-website-us-west-1.amazonaws.com/"
STATIC_URL = "stornco-prod-static.s3-website-us-west-1.amazonaws.com/"

# Collects static files to s3.
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# S3 bucket identity:
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')