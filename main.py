import requests
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

GITHUB_USER = os.getenv("GITHUB_USER")
GITEA_USER = os.getenv("GITEA_USER")
GITEA_TOKEN = os.getenv("GITEA_TOKEN")

GITHUB_URL = f"https://api.github.com/users/{GITHUB_USER}/repos"
GITEA_URL = f"https://git.veen.world/api/v1/users/{GITEA_USER}/repos"
HEADERS = {
    "Authorization": f"token {GITEA_TOKEN}"
}

# Fetch repos from GitHub
response = requests.get(GITHUB_URL)
response.raise_for_status()
github_repos = {repo['name']: repo['clone_url'] for repo in response.json()}

# Fetch repos from Gitea
response = requests.get(GITEA_URL, headers=HEADERS)
response.raise_for_status()
gitea_repos = set(repo['name'] for repo in response.json())

# Identify repos not yet mirrored on Gitea
to_mirror = {name: url for name, url in github_repos.items() if name not in gitea_repos}

# Fetch the Gitea User ID
response = requests.get(f"https://git.veen.world/api/v1/users/{GITEA_USER}", headers=HEADERS)
response.raise_for_status()
gitea_user_id = response.json().get("id")

for name, url in to_mirror.items():
    data = {
        "clone_addr": url,
        "mirror": True,
        "private": True,
        "repo_name": name,
        "uid": gitea_user_id
    }
    response = requests.post(f"https://git.veen.world/api/v1/repos/migrate", headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"{name} was successfully mirrored.")
    else:
        print(f"Error mirroring {name}. Status Code: {response.status_code}, Response: {response.text}")
