poetry run python manage.py flush --no-input
poetry run python manage.py migrate
poetry run python manage.py collectstatic --no-input --clear
poetry run gunicorn orisa_api.wsgi:application --bind 0.0.0.0:8000