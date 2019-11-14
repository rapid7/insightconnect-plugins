import komand
import time
from .schema import NewMessageReceivedInput, NewMessageReceivedOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException
from icon_microsoft_teams.util.teams_utils import get_teams_from_microsoft, get_channels_from_microsoft
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean
from typing import Pattern
import re
import requests
import maya


class NewMessageReceived(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='new_message_received',
                description=Component.DESCRIPTION,
                input=NewMessageReceivedInput(),
                output=NewMessageReceivedOutput())

    def run(self, params={}):
        """Run the trigger"""
        team_name = params.get(Input.TEAM_NAME)
        channel_name = params.get(Input.CHANNEL_NAME)
        message_content = params.get(Input.MESSAGE_CONTENT)

        # Check for valid regex
        compiled_message_content = self.compile_message_content(message_content)

        # Setup the messages endpoint
        messages_endpoint = self.setup_endpoint(channel_name, team_name)

        # Get our initial set of messages
        sorted_messages = self.get_sorted_messages(messages_endpoint)

        # Get our most recent message date:
        try:
            last_time_we_checked = maya.parse(sorted_messages[0].get("createdDateTime"))
        except Exception as e:
            raise PluginException(PluginException.Preset.INVALID_JSON) from e

        time.sleep(1)  # Make sure we don't kill the API. It's limited to 3 calls a second

        while True:
            # Get messages
            sorted_messages = self.get_sorted_messages(messages_endpoint)
            most_recent_message_time = maya.parse(sorted_messages[0].get("createdDateTime"))

            if most_recent_message_time > last_time_we_checked:  # We have new messages
                self.logger.info("New messages found.")
                temp_time = most_recent_message_time

                for message in sorted_messages:  # For each new message
                    message = remove_null_and_clean(message)
                    if maya.parse(message.get("createdDateTime")) > last_time_we_checked:
                        self.logger.info("Analyzing message...")
                        if message_content:
                            self.logger.info("Checking message content.")
                            if compiled_message_content.search(message.get("body", {}).get("content", "")):
                                self.logger.info("Returning new message.")
                                self.send({Output.MESSAGE: message})
                            else:
                                self.logger.info(f"Message did not match {message_content}")
                        else:
                            self.logger.info("Returning new message.")
                            self.send({Output.MESSAGE: message})
                    else:
                        # This speeds up execution a ton. The Beta endpoint doesn't limit how many messages are returned.
                        # Thus, get out of the loop as soon as we see an old message
                        self.logger.info("End of new messages")
                        break

                last_time_we_checked = temp_time
            else:
                self.logger.info("No new messages found...\n\n")
            time.sleep(params.get("interval", 10))

    def compile_message_content(self, message_content: str) -> Pattern:
        """
        This will take a regex string and compile it to verify it's valid

        :param message_content: String
        :return: Pattern
        """
        compiled_message_content = None
        if message_content:
            try:
                compiled_message_content = re.compile(message_content)
            except Exception as e:
                raise PluginException(cause=f"Invalid regular expression: {message_content}",
                                      assistance=f"Please correct {message_content}") from e
        return compiled_message_content

    def get_sorted_messages(self, messages_endpoint: str) -> list:
        """
        This gets new messages from the Graph API, sorts them into chronological order and returns that payload
        as a list of json objects

        :param messages_endpoint: string
        :return: list (of json messages)
        """
        headers = self.connection.get_headers()
        messages_result = requests.get(messages_endpoint, headers=headers)
        try:
            messages_result.raise_for_status()

        # The beta API bombs out every once in a while with Auth denied. Try forcing a refersh of our auth token and
        # retry getting messages before raising an exception.
        except Exception:
            self.logger.info("Get messages failed, refreshing token and trying again.")
            time.sleep(10)  # sleep for 10 seconds to make sure we're not killing the API
            headers = self.connection.get_headers(True)  # This will force a refresh of our auth token
            messages_result = requests.get(messages_endpoint, headers=headers)
            try:
                messages_result.raise_for_status()
            except Exception as e:
                raise PluginException(cause=f"Could not get messages from Microsoft Graph API."
                                            f"Get messages result code: {messages_result.status_code}",
                                      assistance=messages_result.text) from e

        sorted_messages = self.sort_messages_from_request(messages_result.json())
        return sorted_messages

    def sort_messages_from_request(self, messages_result: dict) -> list:
        """
        Takes a json payload from Graph API, extracts all the messages, then returns them in chronological order

        :param messages_result: dict (json payload from the get messages endpoint)
        :return: list (json message objects)
        """
        messages = messages_result.get("value")

        # reverse for descending order
        messages.sort(key=lambda x: maya.parse(x.get("createdDateTime", 0)), reverse=True)
        return messages

    def setup_endpoint(self, channel_name: str, team_name: str) -> str:
        """
        This takes a team name and channel in that team and generates a get messages endpoint.

        :param channel_name: String
        :param team_name: String
        :return: String (URL)
        """
        team = get_teams_from_microsoft(self.logger, self.connection, team_name)
        team_id = team[0].get("id")
        channel = get_channels_from_microsoft(self.logger, self.connection, team_id, channel_name)
        channel_id = channel[0].get("id")
        messages_endpoint = f"https://graph.microsoft.com/beta/teams/{team_id}/channels/{channel_id}/messages"
        return messages_endpoint
