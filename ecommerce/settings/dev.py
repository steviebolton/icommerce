from .base import *

ALLOWED_HOSTS = ["i-commerce-bags-of-fun-humancode.c9users.io", "i-commerce-bags-of-fun-humancode.c9users.io"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

