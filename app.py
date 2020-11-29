import os
from src import create_app

app = create_app(os.environ.get('FLASK_CONFIG_FILE', 'flask-dev.cfg'))

#gunicorn app:app -b localhost:8000
