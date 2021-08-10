release: python manage.py migrate
web: gunicorn ipo_result.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
