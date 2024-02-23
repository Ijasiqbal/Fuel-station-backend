#!/bin/bash
pip install -r requirements.txt

python manage.py makemigrations  --noinput
python manage.py migrate  --noinput

python3.9 manage.py collectstatic --noinput
