from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


def read_secret(secret_name):
    file = open("/run/secrets/" + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()

    return secret


SECRET_KEY = read_secret("DJANGO_SECRET_KEY")


ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django",
        "USER": "django",
        "PASSWORD": read_secret("MYSQL_PASSWORD"),
        "HOST": "mariadb",
        "PORT": "3306",
    }
}
