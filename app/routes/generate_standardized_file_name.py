from flask import Blueprint, request, jsonify
import datetime
import re

file_bp = Blueprint("file_bp", __name__)

VALID_FILE_TYPES = ["pdf", "txt", "docx", "csv", "md"]  # Extend as needed


@file_bp.route('/cli_generate_filename', methods=['POST'])
def cli_generate_filename():
    data = request.json
    short_title = data.get("short_title")
    date_added = data.get("date_added")
    file_type = data.get("file_type", "txt").lower()

    if not short_title or not date_added:
        return "Error: Missing required fields", 400

    file_name, error_msg = standardize_filename(short_title, date_added, file_type)
    if error_msg:
        return f"Error: {error_msg}", 400

    return file_name, 200


@file_bp.route('/generate_standardized_filename', methods=['POST'])
def generate_standardized_filename():
    data = request.json
    short_title = data.get("short_title")
    date_added = data.get("date_added")
    file_type = data.get("file_type", "txt").lower()

    if not short_title or not date_added:
        return jsonify({"error": "Missing required fields"}), 400

    file_name, error_msg = standardize_filename(short_title, date_added, file_type)
    if error_msg:
        return jsonify({"error": error_msg}), 400

    return jsonify({"file_name": file_name}), 200