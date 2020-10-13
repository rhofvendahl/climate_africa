import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import environ
env = environ.Env(DEBUG=(bool, False))
env_file = os.path.join(BASE_DIR, '.env')
environ.Env.read_env(env_file=env_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Should really be in .env, but don't want to cause trouble for fellow devs
SECRET_KEY = env('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'browse',
    'common',
    'compose',
    'map',
    # 'story',
    'help',
    'menu',
    'public',
    # 'view_post',
    # 'view_profile',

    'bootstrap4',
    'cities_light',
    'tz_detect',
    # 'stronghold'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'stronghold.middleware.LoginRequiredMiddleware',
    'climate_africa.middleware.RequireLoginMiddleware',
    'tz_detect.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'climate_africa.urls'

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

WSGI_APPLICATION = 'climate_africa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'climate_africa',
        'USER': 'postgres',
        'PASSWORD': 'postgres', # replace with env('DB_PASSWORD') asap.
        'HOST': 'localhost',
        # 'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# OVERWRITTEN by django-heroku?
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.9/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'common/static/'),
)

LOGIN_URL = '/login/'

OPEN_URLS = [
    '/welcome/',
    '/login/',
    '/join/',
]

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
GS_BUCKET_NAME = 'climate-africa-media'
# AWS_S3_REGION_NAME = 'us-west-002'
# AWS_S3_ENDPOINT_URL = 'https://s3.us-west-002.backblazeb2.com/'
# AWS_S3_SIGNATURE_VERSION='v4'
# STATICFILES_STORAGE

# AUTH_USER_MODEL = 'common.CustomUser'

try:
    print('Generating google credentials file')
    google_credentials_string = env('GOOGLE_CREDENTIALS')
    google_credentials_file = open(BASE_DIR + '/google-credentials.json', 'w')
    google_credentials_file.write(google_credentials_string)
    google_credentials_file.close()
except:
    print('Error: GOOGLE_CREDENTIALS env variable not found.')

# Configure Django App for Heroku.
# Manages DATABASE_URL, ALLOWED_HOSTS, WhiteNoise (static assets), logging, Heroku CI
# Should be at bottom, according to package readme
import django_heroku
django_heroku.settings(locals())
