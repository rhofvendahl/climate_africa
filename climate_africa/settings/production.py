print('APPLYING PRODUCTION SETTINGS')

from climate_africa.settings.base import *

DEBUG = True

ALLOWED_HOSTS = [
    'climate-africa.herokuapp.com',
]
