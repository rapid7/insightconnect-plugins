import re
import requests
import time
from insightconnect_plugin_runtime.exceptions import PluginException

GUID_PATTERN = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.IGNORECASE)

# Properties that require the user to be referenced by GUID rather than UPN
GUID_REQUIRED_PROPERTIES = {"signinactivity"}

# Default properties returned by the Graph API when no $select is specified
DEFAULT_USER_PROPERTIES = [
    "businessPhones",
    "displayName",
    "givenName",
    "id",
    "jobTitle",
    "mail",
    "mobilePhone",
    "officeLocation",
    "preferredLanguage",
    "surname",
    "userPrincipalName",
]


def _resolve_user_id(connection, user_id, headers, logger):
    """Resolve a UPN to a user's object ID (GUID) via a minimal Graph API call."""
    endpoint = f"https://graph.microsoft.com/v1.0/{connection.tenant}/users/{user_id}?$select=id"
    response = requests.get(endpoint, headers=headers)
    if response.status_code != 200:
        raise PluginException(
            cause="Failed to resolve user ID.",
            assistance="Please verify the user ID is valid and try again.",
            data=response.text,
        )
    return response.json().get("id")


def get_user_info(connection, user_id, logger, select=None):
    headers = connection.get_headers(connection.get_auth_token())

    # If select includes properties that require GUID lookup, resolve the UPN first
    if select and GUID_REQUIRED_PROPERTIES.intersection(prop.lower() for prop in select):
        if not GUID_PATTERN.match(user_id):
            logger.info(f"Resolving UPN '{user_id}' to GUID for properties that require it.")
            user_id = _resolve_user_id(connection, user_id, headers, logger)

    endpoint = f"https://graph.microsoft.com/v1.0/{connection.tenant}/users/{user_id}?$expand=manager"

    if select:
        # Filter out 'manager' from select since it's a navigation property handled by $expand
        select_properties = [prop for prop in select if prop.lower() != "manager"]
        # Merge with default properties so the user doesn't lose standard fields
        merged_properties = list(dict.fromkeys(DEFAULT_USER_PROPERTIES + select_properties))
        if merged_properties:
            endpoint += f"&$select={','.join(merged_properties)}"

    result = None
    try:
        result = requests.get(endpoint, headers=headers)
    except Exception:
        counter = 0
        # We are going to try this 5 times and give up.
        for counter in range(1, 6):
            logger.info(f"Get user info failed, trying again, attempt {counter}.")
            logger.info("Sleeping for 5 seconds...")
            time.sleep(5)
            try:
                logger.info("Attempting to get user info.")
                result = requests.get(endpoint, headers=headers)
                break  # We didn't get an exception, so break the loop
            except Exception:
                logger.info("Get user info failed.")

    if result and not result.status_code == 200:
        time.sleep(5)  # adding retry
        result = requests.get(endpoint, headers=headers)
        if not result.status_code == 200:
            raise PluginException(
                cause="Get User Info failed.",
                assistance="Unexpected return code from server.",
                data=result.text,
            )
    return result
