from .base import *


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, ".env"),
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("PRAGMATIC_SETTINGS_SECRET_KEY")

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
