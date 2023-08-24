GRAPH_MICROSOFT_URL = "https://graph.microsoft.com/v1.0/{}/"


class Endpoint:
    USER_ID = GRAPH_MICROSOFT_URL + "users/{}"
    DEVICE_ID = GRAPH_MICROSOFT_URL + "devices/{device_id}"
    DEVICES = GRAPH_MICROSOFT_URL + "devices"
