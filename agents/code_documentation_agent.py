import requests
import os
import subprocess
from config import HEURIST_API_KEY, HEURIST_ENDPOINT

def clone_repo(repo_url, dest_folder="repo"):
    if os.path.exists(dest_folder):
        subprocess.run(["rm", "-rf", dest_folder])
    subprocess.run(["git", "clone", repo_url, dest_folder])

def extract_docstrings(file_path):
    """ Extracts docstrings from a Python file """
    docstrings = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        inside_docstring = False
        current_docstring = []

        for line in lines:
            if '"""' in line or "'''" in line:
                if inside_docstring:
                    inside_docstring = False
                    docstrings.append("\n".join(current_docstring))
                    current_docstring = []
                else:
                    inside_docstring = True
            if inside_docstring:
                current_docstring.append(line.strip())
    
    return "\n\n".join(docstrings)

def analyze_repo_for_docs(repo_path="repo"):
    documentation = {}
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                docs = extract_docstrings(file_path)
                if docs:
                    documentation[file] = docs
    return documentation

def send_to_heurist(documentation):
    headers = {"Authorization": f"Bearer {HEURIST_API_KEY}", "Content-Type": "application/json"}
    response = requests.post(HEURIST_ENDPOINT, json={"docs": documentation}, headers=headers)
    return response.json() if response.status_code == 200 else response.text

def main(repo_url):
    clone_repo(repo_url)
    docs = analyze_repo_for_docs()
    result = send_to_heurist(docs)
    print("Heurist API Response:", result)

if __name__ == "__main__":
    repo_url = input("Enter GitHub Repository URL: ")
    main(repo_url)
