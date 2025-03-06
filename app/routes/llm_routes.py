from flask import Blueprint, request, jsonify
from app.services.llm_service import infer_file_name

llm_bp = Blueprint("llm_bp", __name__)

@llm_bp.route('/infer_file_name', methods=['POST'])
def infer_file_name_route():
    data = request.json
    short_title = data.get("short_title")

    if not short_title:
        return jsonify({"error": "Missing short_title"}), 400

    file_name = infer_file_name(short_title)
    return jsonify({"file_name": file_name}), 200