import os

import requests

from app.schemas.gitlab.thread_linter import IThreadLinter
from internal.common.constants.console_lights import ColorFG


def add_linter_note(input: IThreadLinter):
    message = "Обнаружены неформатированные файлы!"
    # TODO: доделать формирование сообщения

    gitlab_host = os.getenv("GITLAB_SERVER", input.server)
    url = f"{gitlab_host}/api/v4/projects/{input.project}/merge_requests/{input.mr_iid}/discussions"

    payload = {"body": message}
    headers = {
        "PRIVATE-TOKEN": input.access_token,
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, data=payload)
    if response.status_code != 201:
        print(ColorFG.RED.format("Failed to add linter note"))
        print(f"Status code: {response.status_code}\n{response.text}")
        return False
    return True
