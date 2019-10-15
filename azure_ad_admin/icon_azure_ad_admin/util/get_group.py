from komand.exceptions import PluginException
import requests


def get_group(connection, group_name):
    endpoint = f"https://graph.microsoft.com/v1.0/{connection.tenant}/groups"
    headers = connection.get_headers(connection.get_auth_token())
    params = {
        "$filter": f"displayName eq '{group_name}'"
    }
    result = requests.get(endpoint, headers=headers, params=params)
    if not result.status_code == 200:
        raise PluginException(cause="Get User Info failed.",
                              assistance="Unexpected return code from server.",
                              data=result.text)
    group_output = ""
    group_result = result.json()
    if len(group_result["value"]) > 0:
        group_output = group_result["value"][0]
    if not group_output:
        raise PluginException(cause=f"Group with name {group_name} was not found",
                              assistance=f"Please check that {group_name} exists.",
                              data=result.text)
    return group_output
