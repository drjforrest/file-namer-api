from flask import Blueprint, request, jsonify
from app.services.project_service import generate_project_id

project_bp = Blueprint("project_bp", __name__)

@project_bp.route('/generate_project_id', methods=['POST'])
def generate_project_id_route():
    data = request.json
    short_title = data.get("short_title")
    date_added = data.get("date_added")

    project_id, error_msg = generate_project_id(short_title, date_added)
    if error_msg:
        return jsonify({"error": error_msg}), 400

    return jsonify({"project_id": project_id}), 200