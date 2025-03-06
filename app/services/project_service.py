import datetime
from app.models.project_model import create_project, get_db

def generate_project_id(short_title, date_added):
    try:
        date_obj = datetime.datetime.strptime(date_added, "%Y-%m-%dT%H:%M:%S.%fZ")
        month, year = date_obj.strftime("%m"), date_obj.strftime("%Y")

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT MAX(seq) FROM projects WHERE month=? AND year=?", (month, year))
        last_seq = cursor.fetchone()[0]
        seq = 1 if last_seq is None else last_seq + 1

        project_id = f"{seq:04}-{month}-{short_title}-{year}"
        create_project(project_id, month, year, seq)

        return project_id, None
    except ValueError:
        return None, "Invalid date format. Expected ISO format."