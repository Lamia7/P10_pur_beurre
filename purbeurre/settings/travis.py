import os

from . import *


# SECRET_KEY = "travis_secret_key"
SECRET_KEY = os.getenv("TRAVIS_SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
