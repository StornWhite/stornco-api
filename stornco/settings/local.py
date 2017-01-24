# Local development environment settings
import os

from .base import *


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ('DB_ENGINE'),
        'HOST': os.environ('DB_HOST'),
        'PORT': os.environ('DB_PORT'),
        'NAME': os.environ('DB_NAME'),
        'USER': os.environ('DB_USER'),
        'PASSWORD': os.environ('DB_PASSWORD'),
    }
}
