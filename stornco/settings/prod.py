# Production environment settings
from .base import *

# Todo: Remove elasticbeanstalk host after configuring DNS
# Todo: Explicitly list allowed hosts after configuring DNS
ALLOWED_HOSTS = [
    '.us-west-1.elasticbeanstalk.com',
    '.storn.co'
]

# No DB on production as a test
DATABASES = {}