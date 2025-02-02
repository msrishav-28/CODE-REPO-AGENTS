import requests
from config import HEURIST_API_KEY

HEURIST_API_URL = "https://api.heurist.ai/v1/execute"

def analyze_code_with_heurist(code_snippet):
    payload = {
        "api_key": HEURIST_API_KEY,
        "code": code_snippet,
        "task": "generate_documentation"
    }
    
    response = requests.post(HEURIST_API_URL, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error in Heurist API: {response.text}")
        return None
