import requests
import base64

def upload(gh_token, repo, path, content):
    data = {
        "message": f"Automated commit: Adding {path}",
        "content": base64.b64encode(content.encode("utf-8")).decode("utf-8")
    }

    headers = {"Authorization": f"Bearer {gh_token}"}
    r = requests.put(f"https://api.github.com/repos/{repo}/contents/{path}", headers=headers, json=data)
    r.raise_for_status()
