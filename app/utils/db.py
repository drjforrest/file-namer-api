import sqlite3
from flask import g

DATABASE = 'app.db'

def get_db():
    """Returns a database connection."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db(app):
    """Initializes the database if it doesn't exist."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
