import hmac
import hashlib
import json
from flask import Flask, request, jsonify
from config import GITHUB_WEBHOOK_SECRET
from pr_analysis import handle_pull_request
from issue_triage import handle_issue

app = Flask(__name__)

def verify_signature(payload, signature):
    mac = hmac.new(GITHUB_WEBHOOK_SECRET.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(f"sha256={mac}", signature)

@app.route("/webhook", methods=["POST"])
def github_webhook():
    payload = request.get_data()
    signature = request.headers.get("X-Hub-Signature-256")

    if not verify_signature(payload, signature):
        return jsonify({"error": "Invalid signature"}), 403
    
    event = request.headers.get("X-GitHub-Event")
    data = json.loads(payload)

    if event == "pull_request":
        handle_pull_request(data)
    elif event == "issues":
        handle_issue(data)

    return jsonify({"message": "Processed"}), 200

if __name__ == "__main__":
    app.run(port=5000)
