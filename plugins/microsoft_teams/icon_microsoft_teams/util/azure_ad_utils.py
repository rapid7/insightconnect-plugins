from insightconnect_plugin_runtime.exceptions import PluginException
from time import sleep
import requests
from logging import Logger
import insightconnect_plugin_runtime.connection


def get_user_info(logger: Logger, connection: insightconnect_plugin_runtime.connection, user_login: str) -> dict:
    """
    This is used to get information about a user using the user login

    :param logger: object
    :param connection: object
    :param user_login: string
    :return: object (user information dictionary)
    """
    endpoint = (
        f"https://graph.microsoft.com/v1.0/{connection.tenant_id}/users?$filter=userPrincipalName eq '{user_login}'"
    )
    headers = connection.get_headers()

    logger.info(f"Getting user information from:\n{endpoint}")
    result = requests.get(endpoint, headers=headers)

    try:
        result.raise_for_status()
    except Exception as e:
        raise PluginException(cause=f"Unable to get user {user_login}", assistance=result.text) from e

    logger.info(f"Getting user information return code:{result.status_code}")
    try:
        response_json = result.json()
        users = response_json.get("value")
    except Exception as e:
        raise PluginException(
            cause="Get user info returned an unexpected response.",
            assistance="Please contact Rapid7 support with the following information:",
            data=result.text,
        ) from e
    try:
        user = users[0]
    except IndexError as e:
        raise PluginException(
            cause="The server did not send back any results, but the get users call was successful.",
            assistance=f"Usually this indicates the user was not found.\nUser was {user_login}.\n",
            data=result.text,
        ) from e

    return user


def add_user_to_group(
    logger: Logger, connection: insightconnect_plugin_runtime.connection, group_id: str, user_id: str
) -> bool:
    """
    This will add a user to a group

    :param logger: object
    :param connection: object
    :param group_id: string
    :param user_id: string
    :return: boolean
    """
    endpoint = f"https://graph.microsoft.com/v1.0/{connection.tenant_id}/groups/{group_id}/members/$ref"
    headers = connection.get_headers()

    logger.info(f"Adding user with: {endpoint}")
    user_payload = {"@odata.id": f"https://graph.microsoft.com/v1.0/{connection.tenant_id}/users/{user_id}"}

    result = requests.post(endpoint, json=user_payload, headers=headers)
    try:
        result.raise_for_status()
    except Exception as e:
        raise PluginException(
            cause=f"Unable to add user to group:\nUser:{user_id}\nGroup:{group_id}",
            assistance=result.text,
        ) from e

    # https://docs.microsoft.com/en-us/graph/api/group-post-members
    if result.status_code == 204:
        return True

    raise PluginException(
        cause=f"Unexpected response from server when adding user to group. Response code: " f"{result.status_code}.",
        assistance="Please contact Rapid7 support with the following error information:",
        data=result.text,
    )


def remove_user_from_group(
    logger: Logger, connection: insightconnect_plugin_runtime.connection, group_id: str, user_id: str
) -> bool:
    """
    Removes a user from a group

    :param logger: object
    :param connection: object
    :param group_id: string
    :param user_id: string
    :return: boolean
    """
    endpoint = f"https://graph.microsoft.com/v1.0/{connection.tenant_id}/groups/{group_id}/members/{user_id}/$ref"
    headers = connection.get_headers()
    logger.info(f"Removing user with: {endpoint}")

    result = requests.delete(endpoint, headers=headers)
    try:
        result.raise_for_status()
    except Exception as e:
        raise PluginException(
            cause=f"Unable to remove user from group:\nUser:{user_id}\nGroup:{group_id}.",
            assistance=f"{result.text}.",
        ) from e

    # https://docs.microsoft.com/en-us/graph/api/group-post-members
    # 204 no content
    if result.status_code == 204:
        return True

    raise PluginException(
        cause=f"Unexpected response from server when removing user from group. Response code: "
        f"{result.status_code}.",
        assistance="Please contact Rapid7 support with the following error information:",
        data=result.text,
    )


def create_group(
    logger: Logger,
    connection: insightconnect_plugin_runtime.connection,
    group_name: str,
    group_description: str,
    group_nickname: str,
    mail_enabled: bool,
    owners: list,
    members: list,
) -> dict:
    """
    This will create a group in Azure AD

    :param logger: object
    :param connection: object
    :param group_name: string
    :param group_description: string
    :param group_nickname: string
    :param mail_enabled: boolean
    :param owners: list
    :param members: list
    :return: object
    """

    endpoint = f"https://graph.microsoft.com/v1.0/{connection.tenant_id}/groups"
    headers = connection.get_headers()
    payload = {
        "description": group_description,
        "displayName": group_name,
        "groupTypes": ["Unified"],
        "mailEnabled": mail_enabled,
        "mailNickname": group_nickname,
        "securityEnabled": False,
    }

    if owners:
        owners_payload = create_user_paylaod(logger, connection, owners)
        payload["owners@odata.bind"] = owners_payload
    if members:
        members_payload = create_user_paylaod(logger, connection, members)
        payload["members@odata.bind"] = members_payload

    logger.info(f"Creating group with: {endpoint}")
    result = requests.post(endpoint, json=payload, headers=headers)
    try:
        result.raise_for_status()
    except Exception as e:
        raise PluginException(cause=f"Unable to create group: {group_name}", assistance=result.text) from e

    # https://docs.microsoft.com/en-us/graph/api/group-post-groups?view=graph-rest-1.0&tabs=http
    if result.status_code == 201:
        try:
            return result.json()
        except Exception as e:
            raise PluginException(PluginException.Preset.INVALID_JSON) from e

    raise PluginException(
        cause=f"Unexpected response from server when creating group {group_name}. Response code: "
        f"{result.status_code}.",
        assistance="Please contact Rapid7 support with the following error information:",
        data=result.text,
    )


def create_user_paylaod(logger: Logger, connection: insightconnect_plugin_runtime.connection, group_list: list) -> list:
    """
    This takes a list of user names, gets their IDs, then returns a list of odata objects that can
    be fed into create group

    :param logger: object
    :param connection: object
    :param group_list: list
    :return: list
    """
    user_payload = []
    for user_login in group_list:
        logger.info(f"Getting user ID: {user_login}")
        user_object = get_user_info(logger, connection, user_login)
        user_id = user_object.get("id")
        user_odata_thing = f"https://graph.microsoft.com/v1.0/{connection.tenant_id}/users/{user_id}"
        user_payload.append(user_odata_thing)

    return user_payload


def delete_group(logger: Logger, connection: insightconnect_plugin_runtime.connection, group_name: str) -> bool:
    """
    This will delete a group from Azure

    :param logger: object
    :param connection: object
    :param group_name: string
    :return: boolean
    """
    group_id = get_group_id_from_name(logger, connection, group_name)
    endpoint = f"https://graph.microsoft.com/v1.0/{connection.tenant_id}/groups/{group_id}"
    headers = connection.get_headers()

    logger.info(f"Deleting group with: {endpoint}")
    result = requests.delete(endpoint, headers=headers)
    try:
        result.raise_for_status()
    except Exception as e:
        raise PluginException(cause="Delete group failed", assistance=result.text) from e

    # https://docs.microsoft.com/en-us/graph/api/group-delete
    if result.status_code == 204:
        return True

    raise PluginException(
        cause=f"The server returned an unexpected result while deleting the '{group_name}' group.",
        assistance="Please contact Rapid7 support with the following information:",
        data=result.text,
    )


def get_group_id_from_name(
    logger: Logger, connection: insightconnect_plugin_runtime.connection, group_name: str
) -> str:
    """
    This will take a group name and return its ID

    :param logger: object
    :param connection: object
    :param group_name: string
    :return: string
    """
    endpoint = f"https://graph.microsoft.com/v1.0/{connection.tenant_id}/groups?$filter=displayName eq '{group_name}'"
    headers = connection.get_headers()

    logger.info(f"Getting group ID with: {endpoint}")
    result = requests.get(endpoint, headers=headers)

    try:
        result.raise_for_status()
    except Exception as e:
        raise PluginException(cause="Get group ID failed.", assistance=result.text) from e

    try:
        result_json = result.json()
        results = result_json.get("value")
    except Exception as e:
        raise PluginException(PluginException.Preset.INVALID_JSON) from e

    try:
        result = results[0]
    except Exception as e:
        raise PluginException(
            cause="Get group id was successful, but the server did not return any results.",
            assistance=f"This usually indicates the group was not found.\nGroup: {group_name}",
            data=result.text,
        ) from e

    return result.get("id")


def enable_teams_for_group(logger, connection, group_id):
    """
    This will take a group ID and enable it in Teams

    :param logger: object
    :param connection: object
    :param group_id: string
    :return: boolean
    """
    endpoint = f"https://graph.microsoft.com/v1.0/{connection.tenant_id}/groups/{group_id}/team"
    headers = connection.get_headers()
    payload = {
        "memberSettings": {
            "allowCreateUpdateChannels": True,
            "allowDeleteChannels": True,
            "allowAddRemoveApps": True,
            "allowCreateUpdateRemoveTabs": True,
            "allowCreateUpdateRemoveConnectors": True,
        },
        "guestSettings": {"allowCreateUpdateChannels": False, "allowDeleteChannels": False},
        "messagingSettings": {
            "allowUserEditMessages": True,
            "allowUserDeleteMessages": True,
            "allowOwnerDeleteMessages": True,
            "allowTeamMentions": True,
            "allowChannelMentions": True,
        },
        "funSettings": {
            "allowGiphy": True,
            "giphyContentRating": "strict",
            "allowStickersAndMemes": True,
            "allowCustomMemes": True,
        },
    }

    logger.info(f"Enabling team with: {endpoint}")
    result = requests.put(endpoint, json=payload, headers=headers)
    if result.status_code == 201:
        logger.info("Team was enabled successfully.")
        return True

    # https://docs.microsoft.com/en-us/graph/api/team-put-teams?view=graph-rest-1.0&tabs=http
    # This pattern is suggested by microsoft
    for i in range(2, 6):  # 2 to 5 - this is our second attempt, and python range is weird...thus 6
        logger.info(
            f"Attempt to enable team failed. Status code: {result.status_code}\n"
            f"Sleeping for 10 seconds and trying again. Attempt number: {i}"
        )
        sleep(10)
        result = requests.put(endpoint, json=payload, headers=headers)
        if result.status_code == 201:
            logger.info("Team was enabled successfully.")
            return True

    raise PluginException(
        cause=f"Could not enable Teams for group with ID: {group_id}.",
        assistance="This may be due to a replication delay in Azure. Please try again later, or "
        "enable the team manually. If this problem persists, contact Rapid7 support with "
        "the following information:",
        data=f"Status Code: {result.status_code}\n" f"Response:\n{result.text}",
    )


def add_user_to_owners(
    logger: Logger, connection: insightconnect_plugin_runtime.connection.Connection, group_id: str, user_id: str
) -> bool:
    endpoint = f"https://graph.microsoft.com/beta/groups/{group_id}/owners/$ref"
    logger.info(f"Adding user to group owners with: {endpoint}")

    result = requests.post(
        endpoint,
        json={"@odata.id": f"https://graph.microsoft.com/beta/users/{user_id}"},
        headers=connection.get_headers(),
    )
    if result.status_code == 204:
        logger.info("User was added successfully.")
        return True
    if result.status_code == 400:
        logger.info("Unable to add user to group owners. The user is already one of a group owners.")
        return True
    elif result.status_code == 401:
        raise PluginException(
            cause="Invalid credentials.",
            assistance="Please check that provided credentials are correct.",
        )
    elif result.status_code == 403:
        raise PluginException(
            cause="The account configured in your plugin connection is unauthorized to access this service.",
            assistance="Verify the permissions for your account and try again.",
        )
    elif result.status_code == 404:
        raise PluginException(
            cause="Invalid username or group provided.",
            assistance="Please check that provided username and group are correct.",
        )
    try:
        result.raise_for_status()
    except Exception as e:
        raise PluginException(
            cause=f"Unable to add user to group owners:\nUser:{user_id}\nGroup:{group_id}.",
            assistance=f"{result.text}.",
            data=e,
        )
    raise PluginException(
        cause=f"Unexpected response from server when adding user to group owners. Response code: {result.status_code}.",
        assistance="Please contact Rapid7 support with the following error information:",
        data=result.text,
    )


def add_user_to_channel(
    logger: Logger,
    connection: insightconnect_plugin_runtime.connection.Connection,
    group_id: str,
    channel_id: str,
    user_id: str,
) -> bool:
    endpoint = f"https://graph.microsoft.com/beta/teams/{group_id}/channels/{channel_id}/members/"
    logger.info(f"Adding user to channel with: {endpoint}")

    result = requests.post(
        endpoint,
        json={
            "@odata.type": "#microsoft.graph.aadUserConversationMember",
            "roles": [],
            "user@odata.bind": f"https://graph.microsoft.com/beta/users/{user_id}",
        },
        headers=connection.get_headers(),
    )
    if result.status_code == 201:
        logger.info("User was added successfully.")
        return True
    if result.status_code == 400:
        logger.info("Unable to add user to channel. The user has already been added to the channel.")
        return True
    elif result.status_code == 401:
        raise PluginException(
            cause="Invalid credentials.",
            assistance="Please check that provided credentials are correct.",
        )
    elif result.status_code == 403:
        raise PluginException(
            cause="The account configured in your plugin connection is unauthorized to access this service.",
            assistance="Verify the permissions for your account and try again.",
        )
    elif result.status_code == 404:
        raise PluginException(
            cause="Invalid username, group or channel provided.",
            assistance="Please check that provided username, group and channel are correct.",
        )
    try:
        result.raise_for_status()
    except Exception as e:
        raise PluginException(
            cause=f"Unable to add user to channel:\nUser:{user_id}\nChannel:{channel_id}.",
            assistance=f"{result.text}.",
            data=e,
        )
    raise PluginException(
        cause=f"Unexpected response from server when adding user to channel. Response code: {result.status_code}.",
        assistance="Please contact Rapid7 support with the following error information:",
        data=result.text,
    )
