import os

import requests

JIRA_API_CLIENT = requests.Session()
JIRA_API_CLIENT.headers.update(
    {"Authorization": f"Bearer {os.getenv("JIRA_ACCESS_TOKEN")}"}
)
