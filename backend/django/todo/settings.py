from pathlib import Path
import os 

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = str(os.environ.get("DEBUG")) == "1"

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'delete_todo.apps.DeleteTodoConfig',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]

ROOT_URLCONF = 'todo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todo.wsgi.application'

#DECLARE DATABASE VARIABLES 
DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVAILABLE = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT
])

if DB_IS_AVAILABLE:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_DATABASE,
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'todo_list_penn',
#         'USER': 'httpdwgp',
#         'PASSWORD': '0074',
#         'HOST': 'localhost',
#         'PORT': 5432      
#         }
# }

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'UNAUTHENTICATED_USER': None 
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators



# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
