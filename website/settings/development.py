from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
import os
import urllib.parse as up
import psycopg2

up.uses_netloc.append("postgres")
url = up.urlparse("postgres://kppvsxjr:08cLWXbKlwxDO2dxwmANoCsOb9Kc2ykk@satao.db.elephantsql.com:5432/kppvsxjr")
database = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port


ALLOWED_HOSTS = ['192.168.1.106',"127.0.0.1"]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'damir',
#         'USER': 'jeremih',
#         'PASSWORD': 'hellomother',
#         'HOST': 'localhost',
#         'PORT': '5433',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': database,
#         'USER': user,
#         'PASSWORD': password,
#         'HOST': host,
#         'PORT': port,
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}