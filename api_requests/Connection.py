import requests   # ← the real HTTP library
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:5000").strip('"')

def check_db_connection():
    try:
        response = requests.get(f"{BACKEND_URL}/check-db", timeout=3)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
