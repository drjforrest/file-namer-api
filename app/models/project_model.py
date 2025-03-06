import sqlite3

DATABASE = 'app.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_project(project_id, month, year, seq):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO projects (project_id, month, year, seq) VALUES (?, ?, ?, ?)",
                   (project_id, month, year, seq))
    db.commit()
    db.close()