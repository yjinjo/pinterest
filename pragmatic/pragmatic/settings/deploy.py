from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

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
