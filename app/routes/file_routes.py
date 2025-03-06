from flask import Blueprint, request, jsonify
import os

file_bp = Blueprint("file_bp", __name__)


@file_bp.route('/generate_file_path', methods=['POST'])
def generate_file_path():
    data = request.json
    category = data.get("category")
    project_id = data.get("project_id")

    if not category or not project_id:
        return jsonify({"error": "Missing required fields"}), 400

    file_path = f"/Users/drjforrest/Projects/{category}/{project_id}/project_file.txt"
    return jsonify({"file_path": file_path}), 200