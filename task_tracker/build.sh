#!/usr/bin/env bash
set -o errexit

pip install -r ../requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
User.objects.filter(username='admin').exists() or User.objects.create_superuser(
    'admin',
    'admin@example.com',
    '1qazcde3'
)"

python manage.py shell -c "
from app.models import TaskType

for name in [
    'Bug',
    'Feature',
    'Improvement',
    'Documentation',
    'Testing',
    'Code Review',
    'Refactoring',
    'Research',
    'Deployment',
    'Maintenance',
]:
    TaskType.objects.get_or_create(name=name)
"