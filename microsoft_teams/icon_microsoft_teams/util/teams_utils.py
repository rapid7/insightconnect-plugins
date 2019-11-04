from komand.exceptions import PluginException
import requests
import re


def get_teams_from_microsoft(logger, connection, team_name=None):
    """
    This will get teams from the Graph API. If a team_name is provided it will only return that team, or throw
    an error if that team is not found

    :param logger: object (logging.logger)
    :param connection: object (komand.connection)
    :param team_name: string
    :return: array of teams
    """
    compiled_team_name = None
    if team_name:
        try:
            compiled_team_name = re.compile(team_name)
        except Exception as e:
            raise PluginException(cause=f"Team Name {team_name} was an invalid regular expression.",
                                  assistance=f"Please correct {team_name}") from e

    teams_url = "https://graph.microsoft.com/beta/groups?$filter=resourceProvisioningOptions/Any(x:x eq 'Team')"
    headers = connection.get_headers()
    teams_result = requests.get(teams_url, headers=headers)
    try:
        teams_result.raise_for_status()
    except Exception as e:
        raise PluginException(cause="Attempt to get teams failed.",
                              assistance=teams_result.text) from e
    try:
        teams = teams_result.json().get("value")
    except Exception as e:
        raise PluginException(PluginException.Preset.INVALID_JSON) from e

    if team_name:
        logger.info(f"Team name: {team_name}")
        for team in teams:
            name = team.get("displayName")
            logger.info(f"Checking team: {name}")
            if compiled_team_name.match(name):
                return [team]
        else:
            raise PluginException(cause=f"Team {team_name} was not found.",
                                  assistance=f"Please verify {team_name} is a valid team name")

    return teams


def get_channels_from_microsoft(logger, connection, team_id, channel_name=None):
    """
    This will get all channels available to a team from the Graph API
    If the channel_name is provided it will only return that channel or throw an error
    if that channel is not found


    :param logger: object (logging.logger)
    :param connection: (komand.connection)
    :param team_id: String
    :param channel_name: String
    :return: Array
    """
    compiled_channel_name = None
    if channel_name:
        try:
            compiled_channel_name = re.compile(channel_name)
        except Exception as e:
            raise PluginException(cause=f"Channel Name {compiled_channel_name} was an invalid regular expression.",
                                  assistance=f"Please correct {compiled_channel_name}") from e

    channels_url = f"https://graph.microsoft.com/beta/{connection.tenant_id}/teams/{team_id}/channels"
    headers = connection.get_headers()
    channels_result = requests.get(channels_url, headers=headers)
    try:
        channels_result.raise_for_status()
    except Exception as e:
        raise PluginException(cause="Attempt to get channels failed.",
                              assistance=channels_result.text) from e
    try:
        channels = channels_result.json().get("value")
    except Exception as e:
        raise PluginException(PluginException.Preset.INVALID_JSON) from e

    if channel_name:
        logger.info(f"Channel name: {channel_name}")
        for channel in channels:
            name = channel.get("displayName")
            logger.info(f"Checking channel: {name}")
            if compiled_channel_name.match(name):
                return [channel]
        else:
            raise PluginException(cause=f"Channel {channel_name} was not found.",
                                  assistance=f"Please verify {channel_name} is a valid channel for the team "
                                             f"with id: {team_id}")

    return channels


def send_message(logger, connection, message, team_id, channel_id):
    """
    Send a message to Teams

    :param logger: object (logging.logger)
    :param connection: object (komand.connection)
    :param message: String
    :param team_id: String
    :param channel_id: String
    :return: dict
    """
    send_message_url = f"https://graph.microsoft.com/beta/teams/{team_id}/channels/{channel_id}/messages"
    logger.info(f"Sending message to: {send_message_url}")
    headers = connection.get_headers()

    body = {
      "body": {
         "content": message
      }
    }

    result = requests.post(send_message_url, headers=headers, json=body)
    try:
        result.raise_for_status()
    except Exception as e:
        raise PluginException(cause="Send message failed.",
                              assistance=result.text) from e

    message = result.json()
    return message


def send_html_message(logger, connection, message, team_id, channel_id):
    """
    Send HTML content as a message to Teams

    :param logger: object (logging.logger)
    :param connection: object (komand.connection)
    :param message: String (HTML)
    :param team_id: String
    :param channel_id: String
    :return: dict
    """
    send_message_url = f"https://graph.microsoft.com/beta/teams/{team_id}/channels/{channel_id}/messages"
    logger.info(f"Sending message to: {send_message_url}")
    headers = connection.get_headers()

    body = {
      "body": {
          "contentType": "html",
          "content": message
      }
    }

    result = requests.post(send_message_url, headers=headers, json=body)
    try:
        result.raise_for_status()
    except Exception as e:
        raise PluginException(cause="Send message failed.",
                              assistance=result.text) from e

    message = result.json()
    return message
