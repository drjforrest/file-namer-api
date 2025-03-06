import os
import ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Ollama host from environment variable (including port 11434)
os.environ['OLLAMA_HOST'] = os.getenv('OLLAMA_HOST', '127.0.0.1:11434')

def infer_file_name(short_title):
    """Uses an LLM to infer a standardized file name based on the title."""
    response = ollama.chat(model="mistral", messages=[
        {"role": "system", "content": "You are a helpful assistant that formats file names."},
        {"role": "user", "content": f"Generate a standardized file name for: {short_title}"}
    ])
    return response['message']['content']