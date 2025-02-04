BASE_URL = "https://api.services.mimecast.com/"


class Endpoints:
    AUTH = f"{BASE_URL}oauth/token"
    GET_SIEM_LOGS_BATCH = f"{BASE_URL}siem/v1/batch/events/cg"
