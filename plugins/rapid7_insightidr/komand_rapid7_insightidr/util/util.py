import os
from flask import request
from insightconnect_plugin_runtime.helper import clean_dict


def get_logging_context():
    log_values = {}
    # For cloud get our request ID from upstream services
    if os.environ.get("PLUGIN_RUNTIME_ENVIRONMENT", "") == "cloud":
        log_values["R7-Correlation-Id"] = request.headers.get("X-REQUEST-ID")

    return clean_dict(log_values)
