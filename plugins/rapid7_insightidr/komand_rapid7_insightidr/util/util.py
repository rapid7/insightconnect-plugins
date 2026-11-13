import requests
import os
from flask import request
from insightconnect_plugin_runtime.helper import clean_dict
from typing import Any


class QueryStalledError(Exception):
    """Raised while polling a Log Search query whose progress has stopped changing, so it can be resubmitted."""

    def __init__(self, progress: Any, time_left: int) -> None:
        super().__init__(f"Query progress stuck at {progress} with {time_left} seconds left")
        self.progress = progress
        self.time_left = time_left


def get_logging_context():
    log_values = {}
    # For cloud get our request ID from upstream services
    if os.environ.get("PLUGIN_RUNTIME_ENVIRONMENT", "") == "cloud":
        log_values["R7-Correlation-Id"] = request.headers.get("X-REQUEST-ID")
    return clean_dict(log_values)


def send_session_request(
    request_url: str, request_headers: dict[str, Any], request_id: str, request_params: dict[str, Any] = None
):
    if request_params is None:
        request_params = {}
    with requests.Session() as session:
        prepared_request = session.prepare_request(
            request=requests.Request(
                method="GET",
                headers={**request_headers, "R7-Correlation-Id": request_id},
                url=request_url,
                params=request_params,
            )
        )
        response = session.send(prepared_request)
    return response
