#!/bin/bash
# Start the Flask application with Gunicorn
gunicorn app:app --bind 0.0.0.0:8000 --workers 3
