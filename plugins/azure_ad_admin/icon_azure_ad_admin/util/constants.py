GRAPH_MICROSOFT_URL = "https://graph.microsoft.com/v1.0/{}/"


class Endpoint:
    USER_ID = GRAPH_MICROSOFT_URL + "users/{}"
    USER_MEMBER_OF = GRAPH_MICROSOFT_URL + "users/{user_id}/memberOf?$count=true"
    DEVICE_ID = GRAPH_MICROSOFT_URL + "devices/{device_id}"
    DEVICES = GRAPH_MICROSOFT_URL + "devices"
    MEMBERS = GRAPH_MICROSOFT_URL + "groups/{group_id}/members?$count=true"
