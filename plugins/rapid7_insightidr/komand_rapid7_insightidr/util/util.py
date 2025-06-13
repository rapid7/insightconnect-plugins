from flask import request
from insightconnect_plugin_runtime.helper import clean_dict


# when running in cloud enabled mode, loggers from within a thread will not have the correct context from the SDK
# we then need to read in this context from the request object and add it back to loggers from with the thread
def get_logging_context():
    log_values = {}
    log_values["R7-Correlation-Id"] = request.headers.get("X-REQUEST-ID")
    return clean_dict(log_values)
