from .base import *
from .secure import *
from .packages import *

DEBUG = False
ALLOWED_HOSTS = []


CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True 

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True