#!/bin/bash

# Activate the virtual environment if necessary
.\venv\Scripts\activate

# Run Gunicorn server
gunicorn app:app  # Replace 'app' with the name of your Flask app file without the .py extension
