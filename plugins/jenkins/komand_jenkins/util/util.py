from typing import Any, Dict

from requests import Response


def extract_job_number(response: Response) -> int:
    location = response.headers.get("Location", "")
    if not location:
        return 0
    if location.endswith("/"):
        location = location[:-1]
    return int(location.split("/")[-1])


def extract_build_number(job_info: Dict[str, Any]) -> int:
    last_build = job_info.get("lastBuild", {})
    if not last_build or not last_build.get("number"):
        return 1
    return last_build.get("number", 0) + 1
