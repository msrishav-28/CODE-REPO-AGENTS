from flask import Flask
import threading
import github_webhook
import code_documentation_agent
import pr_analysis
import issue_triage

app = Flask(__name__)

def start_webhook_server():
    github_webhook.app.run(port=5000)

def run_code_doc_agent():
    repo_url = input("Enter GitHub Repository URL: ")
    code_documentation_agent.main(repo_url)

def run_pr_analysis():
    repo_owner = input("Enter Repository Owner: ")
    repo_name = input("Enter Repository Name: ")
    pr_data = pr_analysis.fetch_open_prs(repo_owner, repo_name)
    for pr in pr_data:
        pr_analysis.analyze_pr_with_heurist(pr)

def run_issue_triage():
    repo_owner = input("Enter Repository Owner: ")
    repo_name = input("Enter Repository Name: ")
    issues = issue_triage.fetch_issues(repo_owner, repo_name)
    for issue in issues:
        issue_triage.triage_issue_with_heurist(issue)

if __name__ == "__main__":
    print("<<Choose an option:>>")
    print("1️.Start GitHub Webhook Server")
    print("2️.Run Code Documentation Agent")
    print("3️.Analyze Pull Requests")
    print("4️.Triage Issues")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Starting Webhook Server...")
        threading.Thread(target=start_webhook_server).start()
    elif choice == "2":
        print("Running Code Documentation Agent...")
        run_code_doc_agent()
    elif choice == "3":
        print("Running PR Analysis...")
        run_pr_analysis()
    elif choice == "4":
        print("Running Issue Triage...")
        run_issue_triage()
    else:
        print("Invalid choice. Exiting...")
