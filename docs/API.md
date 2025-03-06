# File Namer API Documentation

## Overview
The File Namer API is a Flask-based service that helps generate standardized project IDs and file names using LLM (Large Language Model) technology. The API provides endpoints for project ID generation, file path generation, and file name inference.

## Base URL
```
http://localhost:5000
```

## Authentication
Currently, the API does not require authentication.

## Endpoints

### 1. Generate Project ID
Generates a standardized project ID based on a short title and date.

**Endpoint:** `POST /generate_project_id`

**Request Body:**
```json
{
    "short_title": "string",
    "date_added": "YYYY-MM-DD"
}
```

**Parameters:**
- `short_title` (required): A brief title for the project
- `date_added` (required): The date the project was added in YYYY-MM-DD format

**Response:**
```json
{
    "project_id": "string"
}
```

**Error Response:**
```json
{
    "error": "string"
}
```

**Status Codes:**
- 200: Success
- 400: Bad Request (missing or invalid parameters)

### 2. Generate File Path
Generates a standardized file path for a project based on category and project ID.

**Endpoint:** `POST /generate_file_path`

**Request Body:**
```json
{
    "category": "string",
    "project_id": "string"
}
```

**Parameters:**
- `category` (required): The project category
- `project_id` (required): The project ID generated from the generate_project_id endpoint

**Response:**
```json
{
    "file_path": "string"
}
```

**Error Response:**
```json
{
    "error": "Missing required fields"
}
```

**Status Codes:**
- 200: Success
- 400: Bad Request (missing required fields)

### 3. Infer File Name
Uses an LLM to generate a standardized file name based on a short title.

**Endpoint:** `POST /infer_file_name`

**Request Body:**
```json
{
    "short_title": "string"
}
```

**Parameters:**
- `short_title` (required): A brief title for the file

**Response:**
```json
{
    "file_name": "string"
}
```

**Error Response:**
```json
{
    "error": "Missing short_title"
}
```

**Status Codes:**
- 200: Success
- 400: Bad Request (missing short_title)

## Environment Variables
The API uses the following environment variables:

- `OLLAMA_HOST`: The host address for the Ollama service (default: 127.0.0.1)
- `FLASK_ENV`: The Flask environment (development/production)
- `SECRET_KEY`: Secret key for Flask application
- `DATABASE_URL`: SQLite database URL

## Example Usage

### 1. Generate Project ID
```bash
curl -X POST http://localhost:5000/generate_project_id \
  -H "Content-Type: application/json" \
  -d '{
    "short_title": "Customer Survey Analysis",
    "date_added": "2024-03-06"
  }'
```

### 2. Generate File Path
```bash
curl -X POST http://localhost:5000/generate_file_path \
  -H "Content-Type: application/json" \
  -d '{
    "category": "Research",
    "project_id": "CS20240306-001"
  }'
```

### 3. Infer File Name
```bash
curl -X POST http://localhost:5000/infer_file_name \
  -H "Content-Type: application/json" \
  -d '{
    "short_title": "Customer Survey Analysis Q1 2024"
  }'
```

## Error Handling
The API returns appropriate HTTP status codes and error messages in the response body when:
- Required parameters are missing
- Invalid data is provided
- Server errors occur

## Rate Limiting
Currently, the API does not implement rate limiting.

## Dependencies
- Flask
- Ollama (for LLM functionality)
- python-dotenv (for environment variable management)
- SQLite (for database storage) 