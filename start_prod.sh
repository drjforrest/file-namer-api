#!/bin/bash

# Activate virtual environment
source .venv/bin/activate

# Set production environment variables
export FLASK_ENV=production
export OLLAMA_HOST=192.168.1.88:11434

# Start Gunicorn with our config
gunicorn -c gunicorn_config.py "app:create_app()" 