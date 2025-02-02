import requests
from config import HEURIST_API_KEY, HEURIST_ENDPOINT

def triage_issue_with_heurist(issue_data):
    headers = {"Authorization": f"Bearer {HEURIST_API_KEY}", "Content-Type": "application/json"}
    data = {"issue_title": issue_data["title"], "description": issue_data["body"]}
    
    response = requests.post(HEURIST_ENDPOINT, json=data, headers=headers)
    return response.json() if response.status_code == 200 else response.text

def handle_issue(payload):
    issue = payload.get("issue", {})
    print(f"Triage issue #{issue['number']} with Heurist AI...")
    triage_result = triage_issue_with_heurist(issue)
    print("AI Triage Result:", triage_result)
