#!/bin/bash

# Activate the virtual environment if necessary
source venv/bin/activate  # Change this path if your venv is located somewhere else

# Run Gunicorn server
gunicorn app:app  # Replace 'app' with the name of your Flask app file without the .py extension
