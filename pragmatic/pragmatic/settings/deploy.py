from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("PRAGMATIC_SETTINGS_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django",
        "USER": "django",
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": "mariadb",
        "PORT": "3306",
    }
}
