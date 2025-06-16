import requests
import os
from flask import request
from insightconnect_plugin_runtime.helper import clean_dict


def get_logging_context():
    log_values = {}
    # For cloud get our request ID from upstream services
    if os.environ.get("PLUGIN_RUNTIME_ENVIRONMENT", "") == "cloud":
        log_values["R7-Correlation-Id"] = request.headers.get("X-REQUEST-ID")
    return clean_dict(log_values)


def send_session_request(req_url, req_headers, req_params=None):
    if req_params is None:
        req_params = {}
    with requests.Session() as session:
        prepared_request = session.prepare_request(request=requests.Request(
            method="GET", headers=req_headers, url=req_url, params=req_params))
        response = session.send(prepared_request)
    return response
