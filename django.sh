#!/bin/bash
echo "Migrate"
python manage.py migrate
echo "=================================="

echo "Start server"
gunicorn backend.wsgi:application --bind 0.0.0.0:8000