from insightconnect_plugin_runtime.exceptions import PluginException
import requests
import re
from logging import Logger
import insightconnect_plugin_runtime.connection
from insightconnect_plugin_runtime.helper import clean

from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean


def get_teams_from_microsoft(  # noqa: C901
    logger: Logger, connection: insightconnect_plugin_runtime.connection, team_name=None, explicit=True
) -> list:
    """
    This will get teams from the Graph API. If a team_name is provided it will only return that team, or throw
    an error if that team is not found

    :param logger: object (logging.logger)
    :param connection: object (insightconnect_plugin_runtime.connection)
    :param team_name: string
    :param explicit: boolean
    :return: array of teams
    """
    compiled_team_name = re.compile("")
    if team_name and not explicit:
        try:
            compiled_team_name = re.compile(team_name)
        except Exception as error:
            raise PluginException(
                cause=f"Team Name {team_name} was an invalid regular expression.",
                assistance=f"Please correct {team_name}",
                data=error,
            ) from error

    # See if we are looking for a team name exactly or not
    if explicit:
        teams_url = f"https://graph.microsoft.com/beta/groups?$filter=resourceProvisioningOptions/Any(x:x eq 'Team') and displayName eq '{team_name}'"
    else:
        teams_url = "https://graph.microsoft.com/beta/groups?$filter=resourceProvisioningOptions/Any(x:x eq 'Team')"
    headers = connection.get_headers()
    teams_result = requests.get(teams_url, headers=headers)  # nosec B113
    try:
        teams_result.raise_for_status()
    except Exception as error:
        raise PluginException(cause="Attempt to get teams failed.", assistance=teams_result.text, data=error) from error

    try:
        teams = teams_result.json().get("value")
    except Exception as error:
        raise PluginException(PluginException.Preset.INVALID_JSON, data=error) from error

    nextlink = teams_result.json().get("@odata.nextLink")

    # If there's more than 20 teams, the results will come back paginated.
    while nextlink:
        try:
            new_teams = requests.get(nextlink, headers=headers)  # nosec B113
        except Exception as error:
            raise PluginException(
                cause="Attempt to get paginated teams failed.", assistance=teams_result.text, data=error
            ) from error
        nextlink = new_teams.json().get("@odata.nextLink", "")
        teams.extend(new_teams.json().get("value"))

    if team_name:
        logger.info(f"Team name: {team_name}")
        for team in teams:
            name = team.get("displayName")
            logger.info(f"Checking team: {name}")
            if compiled_team_name.search(name):
                return [team]
        raise PluginException(
            cause=f"Team {team_name} was not found.",
            assistance=f"Please verify {team_name} is a valid team name",
        )

    return teams


def get_channels_from_microsoft(  # noqa: C901
    logger: Logger,
    connection: insightconnect_plugin_runtime.connection,
    team_id: str,
    channel_name=None,
    explicit=False,
) -> list:
    """
    This will get all channels available to a team from the Graph API
    If the channel_name is provided it will only return that channel or throw an error
    if that channel is not found


    :param logger: object (logging.logger)
    :param connection: (insightconnect_plugin_runtime.connection)
    :param team_id: String
    :param channel_name: String
    :param explicit: boolean
    :return: list
    """
    compiled_channel_name = None
    if channel_name:
        try:
            compiled_channel_name = re.compile(channel_name)
        except Exception as error:
            raise PluginException(
                cause=f"Channel Name {compiled_channel_name} was an invalid regular expression.",
                assistance=f"Please correct {compiled_channel_name}",
                data=error,
            ) from error

    # See if we are looking for a channel name exactly or not
    if explicit:
        channels_url = f"https://graph.microsoft.com/beta/{connection.tenant_id}/teams/{team_id}/channels?filter=displayName eq '{channel_name}'"
    else:
        channels_url = f"https://graph.microsoft.com/beta/{connection.tenant_id}/teams/{team_id}/channels"
    headers = connection.get_headers()
    channels_result = requests.get(channels_url, headers=headers)  # nosec B113
    try:
        channels_result.raise_for_status()
    except Exception as error:
        raise PluginException(
            cause="Attempt to get channels failed.", assistance=channels_result.text, data=error
        ) from error
    try:
        channels = channels_result.json().get("value")
    except Exception as error:
        raise PluginException(PluginException.Preset.INVALID_JSON, data=error) from error

    # Note: the channels endpoint does not paginate. Channels max out at 200 per team
    # All 200 will be returned in one list

    if channel_name:
        logger.info(f"Channel name: {channel_name}")
        for channel in channels:
            name = channel.get("displayName")
            logger.info(f"Checking channel: {name}")
            if compiled_channel_name.search(name):
                return [channel]
        raise PluginException(
            cause=f"Channel {channel_name} was not found.",
            assistance=f"Please verify {channel_name} is a valid channel for the team with id: {team_id}",
        )

    return channels


def send_message(
    logger: Logger,
    connection: insightconnect_plugin_runtime.connection,
    message: str,
    team_id: str = None,
    channel_id: str = None,
    thread_id: str = None,
    chat_id: str = None,
) -> dict:
    """
    Send a message to Teams

    :param logger: object (logging.logger)
    :param connection: object (insightconnect_plugin_runtime.connection)
    :param message: String
    :param team_id: String
    :param channel_id: String
    :param thread_id: string
    :param chat_id: string
    :return: dict
    """

    if chat_id:
        send_message_url = f"https://graph.microsoft.com/beta/chats/{chat_id}/messages"
    else:
        send_message_url = f"https://graph.microsoft.com/beta/teams/{team_id}/channels/{channel_id}/messages"
        if thread_id:
            send_message_url = f"{send_message_url}/{thread_id}/replies"

    logger.info(f"Sending message to: {send_message_url}")
    headers = connection.get_headers()

    body = {"body": {"content": message}}

    result = requests.post(send_message_url, headers=headers, json=body)  # nosec B113
    try:
        result.raise_for_status()
    except Exception as error:
        raise PluginException(cause="Send message failed.", assistance=result.text, data=error) from error

    message = result.json()
    return message


def send_html_message(
    logger: Logger,
    connection: insightconnect_plugin_runtime.connection,
    message: str,
    team_id: str,
    channel_id: str,
    thread_id: str = None,
) -> dict:
    """
    Send HTML content as a message to Teams

    :param logger: object (logging.logger)
    :param connection: object (insightconnect_plugin_runtime.connection)
    :param message: String (HTML)
    :param team_id: String
    :param channel_id: String
    :param thread_id: string
    :return: dict
    """
    send_message_url = f"https://graph.microsoft.com/beta/teams/{team_id}/channels/{channel_id}/messages"

    if thread_id:
        send_message_url = send_message_url + f"/{thread_id}/replies"

    logger.info(f"Sending message to: {send_message_url}")
    headers = connection.get_headers()

    body = {"body": {"contentType": "html", "content": message}}

    result = requests.post(send_message_url, headers=headers, json=body)  # nosec B113
    try:
        result.raise_for_status()
    except Exception as error:
        raise PluginException(cause="Send message failed.", assistance=result.text, data=error) from error

    message = result.json()
    return message


def create_chat(connection: insightconnect_plugin_runtime.connection, members: str, topic: str) -> dict:
    """
    Creates a chat for given users

    :param connection: Object (insightconnect_plugin_runtime.connection)
    :param members: String
    :return: dict
    """

    create_chat_endpoint = "https://graph.microsoft.com/beta/chats/"
    create_chat_payload = {}

    list_members = []
    for member in members:
        formatted_member = {
            "@odata.type": "#microsoft.graph.aadUserConversationMember",
            "roles": [f"{member.get('role')}"],
            "user@odata.bind": f"https://graph.microsoft.com/v1.0/users('{member.get('user_info')}')",
        }
        list_members.append(formatted_member)

    if len(list_members) == 2:
        create_chat_payload["chatType"] = "oneOnOne"
    elif len(list_members) > 2:
        create_chat_payload["chatType"] = "group"
        if topic:
            create_chat_payload["topic"] = topic
    else:
        raise PluginException(cause="Create chat failed.", assistance="Less than 2 valid members were provided")

    create_chat_payload["members"] = list_members

    headers = connection.get_headers()

    result = requests.post(create_chat_endpoint, json=create_chat_payload, headers=headers)  # nosec B113

    try:
        result.raise_for_status()
    except Exception as error:
        raise PluginException(cause="Create chat failed.", assistance=result.text, data=error) from error

    if not result.status_code == 201:
        raise PluginException(cause="Create channel returned an unexpected result.", assistance=result.text)

    return result.json()


def create_channel(
    logger: Logger,
    connection: insightconnect_plugin_runtime.connection,
    team_id: str,
    channel_name: str,
    description: str,
    channel_type: str,
) -> bool:
    """
    Creates a channel for a given team

    :param logger: (logging.logger)
    :param connection: Object (insightconnect_plugin_runtime.connection)
    :param team_id: String
    :param channel_name: String
    :param description: String
    :param channel_type: String
    :return: boolean
    """

    create_channel_endpoint = f"https://graph.microsoft.com/beta/teams/{team_id}/channels"
    create_channel_payload = {
        "description": description,
        "displayName": channel_name,
        "membershipType": channel_type.lower(),
    }

    headers = connection.get_headers()

    logger.info(f"Creating {channel_type} channel with: {create_channel_endpoint}")
    result = requests.post(create_channel_endpoint, json=create_channel_payload, headers=headers)  # nosec B113

    try:
        result.raise_for_status()
    except Exception as error:
        raise PluginException(
            cause=f"Create channel {channel_name} failed.", assistance=result.text, data=error
        ) from error

    if not result.status_code == 201:
        raise PluginException(cause="Create channel returned an unexpected result.", assistance=result.text)

    return True


def delete_channel(
    logger: Logger, connection: insightconnect_plugin_runtime.connection, team_id: str, channel_id: str
) -> bool:
    """
    Deletes a channel for a given team

    :param logger: (logging.logger)
    :param connection: Object (insightconnect_plugin_runtime.connection)
    :param team_id: String
    :param channel_id: String
    :return: boolean
    """

    delete_channel_endpoint = (
        f"https://graph.microsoft.com/v1.0/{connection.tenant_id}/teams/{team_id}/channels/{channel_id}"
    )

    headers = connection.get_headers()

    logger.info(f"Deleting channel with: {delete_channel_endpoint}")
    result = requests.delete(delete_channel_endpoint, headers=headers)  # nosec B113

    try:
        result.raise_for_status()
    except Exception as error:
        raise PluginException(
            cause=f"Delete channel {channel_id} failed.", assistance=result.text, data=error
        ) from error

    if not result.status_code == 204:
        raise PluginException(cause="Delete channel returned an unexpected result.", assistance=result.text)

    return True


def get_message_from_channel(  # noqa: C901
    connection: insightconnect_plugin_runtime.connection,
    team_id: str,
    channel_id: str,
    message_id: str,
    reply_id: str = None,
) -> list:
    message_url = f"https://graph.microsoft.com/beta/{connection.tenant_id}/teams/{team_id}/channels/{channel_id}/messages/{message_id}"
    if reply_id:
        message_url = f"https://graph.microsoft.com/beta/{connection.tenant_id}/teams/{team_id}/channels/{channel_id}/messages/{message_id}/replies/{reply_id}"
    headers = connection.get_headers()
    response = requests.get(message_url, headers=headers)  # nosec B113
    try:
        response.raise_for_status()
    except Exception as error:
        raise PluginException(preset=PluginException.Preset.BAD_REQUEST, assistance=response.text, data=error)
    try:
        message = response.json()
    except Exception as error:
        raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
    return remove_null_and_clean(message)


def get_message_from_chat(  # noqa: C901
    connection: insightconnect_plugin_runtime.connection,
    username: str,
    chat_id: str,
    message_id: str,
) -> list:
    message_url = f"https://graph.microsoft.com/beta/{connection.tenant_id}/users/{username}/chats/{chat_id}/messages/{message_id}"
    headers = connection.get_headers()
    response = requests.get(message_url, headers=headers)  # nosec B113

    try:
        response.raise_for_status()
    except Exception as error:
        raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=error)
    try:
        message = response.json()
    except Exception as error:
        raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
    return remove_null_and_clean(message)


def list_messages_from_chat(connection: insightconnect_plugin_runtime.connection, chat_id: str) -> list:  # noqa: C901
    """
    Lists the last 50 messages from a teams chat

    :param connection: Object (insightconnect_plugin_runtime.connection)
    :param chat_id: String
    :return: list
    """

    params = {"$top": 50, "$orderby": "createdDateTime desc"}
    message_url = f"https://graph.microsoft.com/beta/{connection.tenant_id}/chats/{chat_id}/messages/"
    headers = connection.get_headers()
    response = requests.get(message_url, headers=headers, params=params)  # nosec B113

    try:
        response.raise_for_status()
        messages = response.json().get("value", [])
    except requests.HTTPError as http_error:
        raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=http_error)
    except ValueError as value_error:
        raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=value_error)
    except Exception as error:
        raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    clean_messages = []

    for message in messages:
        clean_messages.append(clean(message))

    return clean_messages


def get_reply_list(  # noqa: C901
    connection: insightconnect_plugin_runtime.connection,
    team_id: str,
    channel_id: str,
    message_id: str,
) -> list:
    message_url = f"https://graph.microsoft.com/beta/{connection.tenant_id}/teams/{team_id}/channels/{channel_id}/messages/{message_id}/replies"
    headers = connection.get_headers()
    response = requests.get(message_url, headers=headers)  # nosec B113

    try:
        response.raise_for_status()
    except Exception as error:
        raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=error)
    try:
        messages = response.json()
    except Exception as error:
        raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=error)
    return clean(messages.get("value", []))
