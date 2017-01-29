# Production environment settings
import os
from .base import *

# For security:

DEBUG = False

ALLOWED_HOSTS = [
    '.storn.co'
]


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