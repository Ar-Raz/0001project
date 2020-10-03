from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.106',"127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'damir',
        'USER': 'jeremih',
        'PASSWORD': 'hellomother',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
