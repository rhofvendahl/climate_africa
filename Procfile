release: python manage.py migrate && python manage.py generate_google_credentials
web: gunicorn climate_africa.wsgi
