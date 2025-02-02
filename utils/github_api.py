import requests
from config import GITHUB_ACCESS_TOKEN

GITHUB_API_URL = "https://api.github.com"

def get_repository_data(repo_owner, repo_name):
    url = f"{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}"
    headers = {"Authorization": f"token {GITHUB_ACCESS_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching repo: {response.text}")
        return None

def fetch_open_prs(repo_owner, repo_name):
    url = f"{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}/pulls"
    headers = {"Authorization": f"token {GITHUB_ACCESS_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching PRs: {response.text}")
        return None

def fetch_issues(repo_owner, repo_name):
    url = f"{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}/issues"
    headers = {"Authorization": f"token {GITHUB_ACCESS_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching issues: {response.text}")
        return None
