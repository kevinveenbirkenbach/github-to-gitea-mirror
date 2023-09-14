import requests
from dotenv import load_dotenv
import os

# Lade die .env Datei
load_dotenv()

GITHUB_USER = os.getenv("GITHUB_USER")
GITEA_USER = os.getenv("GITEA_USER")
GITEA_TOKEN = os.getenv("GITEA_TOKEN")

GITHUB_URL = f"https://api.github.com/users/{GITHUB_USER}/repos"
GITEA_URL = f"https://git.veen.world/api/v1/users/{GITEA_USER}/repos"
HEADERS = {
    "Authorization": f"token {GITEA_TOKEN}"
}

# Hole die Repos von GitHub
response = requests.get(GITHUB_URL)
response.raise_for_status()
github_repos = {repo['name']: repo['clone_url'] for repo in response.json()}

# Hole die Repos von Gitea
response = requests.get(GITEA_URL, headers=HEADERS)
response.raise_for_status()
gitea_repos = set(repo['name'] for repo in response.json())

# Finde die Repos, die noch nicht auf Gitea gemirrored werden
to_mirror = {name: url for name, url in github_repos.items() if name not in gitea_repos}

for name, url in to_mirror.items():
    data = {
        "clone_url": url,
        "mirror": True,
        "private": True,
        "repo_name": name,
        "uid": GITEA_USER
    }
    response = requests.post(f"https://git.veen.world/api/v1/repos/migrate", headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"{name} wurde erfolgreich gemirrored.")
    else:
        print(f"Fehler beim Mirroring von {name}. Status-Code: {response.status_code}, Antwort: {response.text}")
