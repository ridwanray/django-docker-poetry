from .base import *
from decouple import config

ALLOWED_HOSTS = ['*']
DEBUG = config('DEBUG', cast=bool)