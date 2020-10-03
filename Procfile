web: gunicorn wsgi.py:main --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
