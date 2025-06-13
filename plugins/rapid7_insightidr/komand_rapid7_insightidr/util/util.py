import os
import uuid
from flask import request
from insightconnect_plugin_runtime.helper import clean_dict


def get_logging_context():
    log_values = {}
    backup_uuid = str(uuid.uuid4())
    # For cloud get our request ID from upstream services other build a new one
    if os.environ.get("PLUGIN_RUNTIME_ENVIRONMENT", "") == "cloud":
        log_values["R7-Correlation-Id"] = request.headers.get("X-REQUEST-ID", backup_uuid)
    else:
        log_values["R7-Correlation-Id"] = backup_uuid
    return log_values
