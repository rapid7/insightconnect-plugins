import requests
import os
from flask import request
from insightconnect_plugin_runtime.helper import clean_dict
from typing import Any


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
