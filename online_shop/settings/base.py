import os
from django.core.exceptions import ImproperlyConfigured
from pathlib import Path


def get_env_variable(var_name):
    """Get the environment variable or return Exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {} environment variable.'.format(var_name)
        raise ImproperlyConfigured(error_msg)


BASE_DIR = str(Path(__file__).resolve().parent.parent.parent)


SECRET_KEY = get_env_variable('ONLINE_SHOP_SECRET_KEY')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'products.apps.ProductsConfig',
    'mptt',
    'django.contrib.humanize',
    'social_django',
    'auto_posting',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',  # <--
]

ROOT_URLCONF = 'online_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'online_shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Authentication backends

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.github.GithubOAuth2',  # for Github authentication
    'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication
    'social_core.backends.twitter.TwitterOAuth',  # for Twitter authentication
    'social_core.backends.linkedin.LinkedinOAuth2',  # for Linkedin authentication
    'social_core.backends.instagram.InstagramOAuth2',  # for instagram authentication

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = get_env_variable('ONLINE_SHOP_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = get_env_variable('ONLINE_SHOP_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_GITHUB_KEY = get_env_variable('ONLINE_SHOP_SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = get_env_variable('ONLINE_SHOP_SOCIAL_AUTH_GITHUB_SECRET')

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = get_env_variable('ONLINE_SHOP_SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY')
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = get_env_variable('ONLINE_SHOP_SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET')

SOCIAL_AUTH_FACEBOOK_KEY = get_env_variable('ONLINE_SHOP_SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = get_env_variable('ONLINE_SHOP_SOCIAL_AUTH_FACEBOOK_SECRET')

SOCIAL_AUTH_TWITTER_KEY = get_env_variable('ONLINE_SHOP_SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = get_env_variable('ONLINE_SHOP_SOCIAL_AUTH_TWITTER_SECRET')


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Iran'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static_url/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')

MEDIA_URL = '/meida/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]

###

LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'users:login'
LOGOUT_URL = 'users:logout'
