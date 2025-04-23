set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --on-input

python manage.py migrate

