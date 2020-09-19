from django.core.management.base import BaseCommand

import os
BASE_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../../..'))

import environ
env = environ.Env(DEBUG=(bool, False))
env_file = os.path.join(BASE_DIR, '.env')
environ.Env.read_env(env_file=env_file)

class Command(BaseCommand):
    help = 'Create start tags/intentions'
    def handle(self, *args, **options):
        print('Generating google credentials file')
        print(BASE_DIR + '/google-credentials.json')
        print(env('HEY'))
        google_credentials_string = env('GOOGLE_CREDENTIALS')
        google_credentials_file = open(BASE_DIR + '/google-credentials.json', 'w')
        google_credentials_file.write(google_credentials_string)
        google_credentials_file.close()
