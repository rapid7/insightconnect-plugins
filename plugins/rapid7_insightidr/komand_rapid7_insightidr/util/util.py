import os
from flask import request
from insightconnect_plugin_runtime.helper import clean_dict


def get_logging_context():
    log_values = {}
    if os.environ.get("PLUGIN_RUNTIME_ENVIRONMENT", "") == "cloud":
        log_values["R7-Correlation-Id"] = request.headers.get("X-REQUEST-ID")
        return clean_dict(log_values)
    else:
        return log_values
