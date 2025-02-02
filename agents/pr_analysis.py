import requests
from config import HEURIST_API_KEY, HEURIST_ENDPOINT

def analyze_pr_with_heurist(pr_data):
    headers = {"Authorization": f"Bearer {HEURIST_API_KEY}", "Content-Type": "application/json"}
    data = {"code_diff": pr_data["diff"], "description": pr_data["title"]}
    
    response = requests.post(HEURIST_ENDPOINT, json=data, headers=headers)
    return response.json() if response.status_code == 200 else response.text

def handle_pull_request(payload):
    pr_data = payload.get("pull_request", {})
    print(f"Analyzing PR #{pr_data['number']} with Heurist AI...")
    analysis_result = analyze_pr_with_heurist(pr_data)
    print("AI PR Analysis:", analysis_result)
