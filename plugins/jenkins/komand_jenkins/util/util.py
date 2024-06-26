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
    last_build_number = job_info.get("lastBuild", {}).get("number")
    if not last_build_number:
        return 1
    return last_build_number + 1
