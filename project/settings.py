import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('PGSQL_HOST'),
        'PORT': os.getenv('PGSQL_PORT'),
        'NAME': os.getenv('PGSQL_DBNAME'),
        'USER': os.getenv('PGSQL_USER'),
        'PASSWORD': os.getenv('PGSQL_PWD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = True

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
