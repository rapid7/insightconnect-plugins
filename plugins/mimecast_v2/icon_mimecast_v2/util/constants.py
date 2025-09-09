BASE_URL = "https://api.services.mimecast.com/"


class Endpoints:
    # OAuth
    AUTH = f"{BASE_URL}oauth/token"

    # SIEM
    GET_SIEM_LOGS_BATCH = f"{BASE_URL}siem/v1/batch/events/cg"

    # Impersonation protection logs
    GET_IMPERSONATION_LOGS = f"{BASE_URL}api/ttp/impersonation/get-logs"

    # Attachment protection logs
    GET_ATTACHMENT_LOGS = f"{BASE_URL}api/ttp/attachment/get-logs"

    # URL protection logs
    GET_URL_LOGS = f"{BASE_URL}api/ttp/url/get-logs"
