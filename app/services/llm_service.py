import os
import ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Ollama client with host from environment variable
ollama.set_host(os.getenv('OLLAMA_HOST', '127.0.0.1'))

def infer_file_name(short_title):
    """Uses an LLM to infer a standardized file name based on the title."""
    response = ollama.chat(model="mistral", messages=[
        {"role": "system", "content": "You are a helpful assistant that formats file names."},
        {"role": "user", "content": f"Generate a standardized file name for: {short_title}"}
    ])
    return response['message']['content']