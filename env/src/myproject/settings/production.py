from .base import *

DEBUG = config('DEBUG',cast=bool)

ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':config('Axeswa'),
        'USER': config('postgres'),
        'PASSWORD':config('12345') ,
        'HOST': config('127.0.0.1'),
        'PORT':'5432'
    }
}




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





AXESWA_PUBLIC_KEY = ('AXESWA_LIVE_PUBLIC_KEY')  

AXESWA_SECRET_KEY = ('AEXSWA_LIVE_SECRET_KEY') 







