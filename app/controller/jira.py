import os

from internal.constants.console_lights import ColorFG
from internal.constants.data import MERGE_TRAIN
from internal.enums.jira import StageCode, TransitCode
from internal.service.http import JIRA_API_CLIENT


def extract_issue_list(branch_name: str) -> list[str]:
    tasks = []
    try:
        _, *_tasks, _ = branch_name.split("/")
        tasks = _tasks
    except Exception:
        pass
    return tasks


def move_issue(issue_list: list[str], mr_event_type: str | None) -> list[str]:
    unhandled_issues: list[str] = []

    for issue_key in issue_list:
        issue = __get_issue_info(issue_key)
        if not issue:
            continue
        if not issue.get("sprint", None):
            print(ColorFG.YELLOW.format(f"The issue {issue_key} is not in sprint"))
            continue

        try:
            current_stage = issue["status"]["id"]
            if current_stage == StageCode.TODO and not mr_event_type:
                __transit_issue(
                    issue_key,
                    TransitCode.IN_PROGRESS,
                    StageCode.IN_PROGRESS.name.replace("_", " "),
                )
            elif current_stage == StageCode.IN_PROGRESS and mr_event_type:
                __transit_issue(
                    issue_key,
                    TransitCode.IN_REVIEW,
                    StageCode.IN_REVIEW.name.replace("_", " "),
                )
            elif (
                current_stage in [StageCode.IN_REVIEW, StageCode.QA]
                and mr_event_type == MERGE_TRAIN
            ):
                __transit_issue(issue_key, TransitCode.DONE, StageCode.DONE.name)
            else:
                print(f"The task {issue_key} already have right status.")
        except Exception as ex:
            print(ColorFG.RED.format(f"The task {issue_key} is not handled."))
            print("An error has occurred:", ex)
            unhandled_issues.append(issue_key)
            continue
    return unhandled_issues


def __get_issue_info(issue_key: str) -> dict | None:
    res = JIRA_API_CLIENT.get(
        f"{os.getenv('JIRA_SERVER_API')}/agile/1.0/issue/{issue_key}?fields=status&fields=sprint"
    )
    if res.status_code != 200:
        print(f"Couldn't found issue {issue_key}")
        return None
    return res.json().get("fields", {})


def __transit_issue(issue_key: str, stage_code: str, stage_name: str):
    payload = {"transition": {"id": stage_code}}
    res = JIRA_API_CLIENT.post(
        f"{os.getenv('JIRA_SERVER_API')}/api/2/issue/{issue_key}/transitions",
        json=payload,
    )

    if res.status_code == 204:
        print(
            ColorFG.GREEN.format(
                f"The task {issue_key} has been successfully moved to the status '{stage_name}'."
            )
        )
    else:
        raise Exception(
            f"Error: status code {res.status_code}. Server response: {res.text}"
        )
