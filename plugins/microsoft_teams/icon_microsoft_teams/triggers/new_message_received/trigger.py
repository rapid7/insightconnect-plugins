import insightconnect_plugin_runtime
import time
from .schema import NewMessageReceivedInput, NewMessageReceivedOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_microsoft_teams.util.teams_utils import (
    get_teams_from_microsoft,
    get_channels_from_microsoft,
)
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean
from icon_microsoft_teams.util.words_utils import add_words_values_to_message, strip_html
from typing import Pattern
import re
import requests
import maya
import validators


class NewMessageReceived(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_message_received",
            description=Component.DESCRIPTION,
            input=NewMessageReceivedInput(),
            output=NewMessageReceivedOutput(),
        )

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
                    message = add_words_values_to_message(message)
                    if maya.parse(message.get("createdDateTime")) > last_time_we_checked:
                        self.logger.info("Analyzing message...")
                        if message_content:  # Do we have a reg ex
                            self.logger.info("Checking message content.")
                            ms_message_content = message.get("body", {}).get("content", "")
                            if message.get("body", {}).get("contentType", "").lower() == "html":
                                ms_message_content = strip_html(ms_message_content)
                            self.logger.info(f"Testing message: {ms_message_content}")
                            if compiled_message_content.search(ms_message_content):
                                self.logger.info("Returning new message.")
                                self.send(
                                    {
                                        Output.MESSAGE: message,
                                        Output.TEAM_NAME: team_name,
                                        Output.CHANNEL_NAME: channel_name,
                                        Output.INDICATORS: self.get_indicators(
                                            message.get("body", {}).get("content", "")
                                        ),
                                    }
                                )
                            else:
                                self.logger.info(
                                    f"Message did not match regex.\nMessage: {ms_message_content}\nRegex: {message_content}"
                                )
                        else:  # we did not have a regex
                            self.logger.info("Returning new message.")
                            self.send(
                                {
                                    Output.MESSAGE: message,
                                    Output.INDICATORS: self.get_indicators(message.get("body", {}).get("content", "")),
                                }
                            )
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
                raise PluginException(
                    cause=f"Invalid regular expression: {message_content}",
                    assistance=f"Please correct {message_content}",
                ) from e
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
                raise PluginException(
                    cause=f"Could not get messages from Microsoft Graph API."
                    f"Get messages result code: {messages_result.status_code}",
                    assistance=messages_result.text,
                ) from e

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

    def get_indicators(self, message: str) -> object:
        urls = self.remove_duplicates(self.extract_urls(message))
        normalized_urls = []
        domains = []

        if urls:
            for url in urls:
                if url.startswith("http") or url.startswith("https"):
                    normalized_urls.append(url)
                else:
                    normalized_urls.append(f"https://{url}")

            for url in normalized_urls:
                domains.append(url.replace("https://", "").replace("http://", ""))

        return {
            "domains": self.remove_duplicates(domains),
            "urls": self.remove_duplicates(normalized_urls),
            "email_addresses": self.remove_duplicates(self.extract_emails(message)),
            "hashes": {
                "md5_hashes": self.remove_duplicates(self.extract_md5(message)),
                "sha1_hashes": self.remove_duplicates(self.extract_sha1(message)),
                "sha256_hashes": self.remove_duplicates(self.extract_sha256(message)),
            },
            "ip_addresses": {
                "ipv4_addresses": self.remove_duplicates(self.extract_ipv4_addresses(message)),
                "ipv6_addresses": self.remove_duplicates(self.extract_ipv6_addresses(message)),
            },
            "mac_addresses": self.remove_duplicates(self.extract_macs(message)),
            "cves": self.remove_duplicates(self.extract_cve(message)),
            "uuids": self.remove_duplicates(self.extract_uuid(message)),
        }

    @staticmethod
    def remove_duplicates(list_with_duplicates):
        return list(dict.fromkeys(list_with_duplicates))

    @staticmethod
    def extract_first_word(message: str) -> str:
        message_normalize = re.sub(r"<.*?>", "", message)
        words = message_normalize.split()

        if len(words) == 0:
            return ""

        return words[0]

    @staticmethod
    def extract_ipv4_addresses(msg: str) -> list:
        return re.findall(r"(?m)\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}(?:/[0-9]{1,2})?\b", msg)

    @staticmethod
    def extract_ipv6_addresses(msg: str) -> list:
        ipv4_seg = r"(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])"
        ipv4_addr = r"(?:(?:" + ipv4_seg + r"\.){3,3}" + ipv4_seg + r")"
        ipv6_seg = r"(?:(?:[0-9a-fA-F]){1,4})"
        ipv6_groups = (
            r"(?:" + ipv6_seg + r":){7,7}" + ipv6_seg,
            r"(?:" + ipv6_seg + r":){1,7}:",
            r"(?:" + ipv6_seg + r":){1,6}:" + ipv6_seg,
            r"(?:" + ipv6_seg + r":){1,5}(?::" + ipv6_seg + r"){1,2}",
            r"(?:" + ipv6_seg + r":){1,4}(?::" + ipv6_seg + r"){1,3}",
            r"(?:" + ipv6_seg + r":){1,3}(?::" + ipv6_seg + r"){1,4}",
            r"(?:" + ipv6_seg + r":){1,2}(?::" + ipv6_seg + r"){1,5}",
            ipv6_seg + r":(?:(?::" + ipv6_seg + r"){1,6})",
            r":(?:(?::" + ipv6_seg + r"){1,7}|:)",
            r"fe80:(?::" + ipv6_seg + r"){0,4}%[0-9a-zA-Z]{1,}",
            r"::(?:ffff(?::0{1,4}){0,1}:){0,1}[^\s:]" + ipv4_addr,
            r"(?:" + ipv6_seg + r":){1,4}:[^\s:]" + ipv4_addr,
        )

        return re.findall("|".join(["(?:{})".format(g) for g in ipv6_groups[::-1]]), msg)

    @staticmethod
    def extract_md5(msg: str) -> list:
        return re.findall(r"(?m)\b[a-zA-Z0-9]{32}\b", msg)

    @staticmethod
    def extract_uuid(msg: str) -> list:
        return re.findall(
            r"(?m)\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b",
            msg,
        )

    @staticmethod
    def extract_sha1(msg: str) -> list:
        return re.findall(r"(?m)\b[a-zA-Z0-9]{40}\b", msg)

    @staticmethod
    def extract_sha256(msg: str) -> list:
        return re.findall(r"(?m)\b[a-zA-Z0-9]{64}\b", msg)

    @staticmethod
    def extract_urls(msg: str) -> list:
        urls = re.findall(
            r"(?m)\b(?:http(?:s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:\/?#[\]@!\$&'\(\)\*\+,;=.]+\b",
            msg.lower(),
        )
        normalized_urls = []
        for url in urls:
            if "@" in url or validators.ipv6(url) or validators.ipv4(url):
                continue

            normalized_urls.append(url)

        return normalized_urls

    @staticmethod
    def extract_emails(msg: str) -> list:
        return re.findall(r"(?m)\b([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)\b", msg.lower())

    @staticmethod
    def extract_cve(msg: str) -> list:
        return re.findall(r"(?m)\bCVE-\d{4}-\d{4,7}\b", msg.upper())

    @staticmethod
    def extract_macs(msg: str) -> list:
        mac_addresses = re.findall(
            r"(?m)\b(?:[0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}"
            r"[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2}[:-][0-9a-fA-F]{2})\b",
            msg.upper(),
        )
        normalized_mac_addresses = []
        for mac_address in mac_addresses:
            normalized_mac_addresses.append(mac_address.replace("-", ":"))

        return normalized_mac_addresses
