#!/bin/sh

# Exit on any error
set -e

# Wait for the PostgreSQL service to be ready
while ! nc -z $POSTGRES_HOST 5432; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

# Make and apply migrations
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate

# Collect static files (if any)
# python manage.py collectstatic --noinput

# Start the Django development server
exec "$@"
