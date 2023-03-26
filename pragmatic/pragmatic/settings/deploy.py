from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django",
        "USER": "django",
        "PASSWORD": "test1234!",
        "HOST": "mariadb",
        "PORT": "3306",
    }
}
