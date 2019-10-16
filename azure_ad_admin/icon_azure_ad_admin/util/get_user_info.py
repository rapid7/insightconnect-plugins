import requests
from komand.exceptions import PluginException


def get_user_info(connection, user_id):
    endpoint = f"https://graph.microsoft.com/v1.0/{connection.tenant}/users/{user_id}"
    headers = connection.get_headers(connection.get_auth_token())

    result = requests.get(endpoint, headers=headers)
    if not result.status_code == 200:
        raise PluginException(cause="Get User Info failed.",
                              assistance="Unexpected return code from server.",
                              data=result.text)
    return result
