import requests
from logging import Logger
from typing import Union
from time import sleep
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

from icon_microsoft_teams.util.constants import TIMEOUT, HTTP_ERROR_MAP
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean

import re
import urllib.parse


class GraphApiClient:
    """Microsoft Graph API client using application-only (client_credentials) authentication."""

    def __init__(self, base_url: str, logger: Logger, get_headers_func):
        """
        Initialize the Graph API client.

        :param base_url: The Graph API base URL (e.g., https://graph.microsoft.com)
        :param logger: Logger instance
        :param get_headers_func: Callable that returns auth headers dict
        """
        self._base_url = base_url
        self._logger = logger
        self._get_headers = get_headers_func
        self._session = requests.Session()

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Union[dict, list]:
        """
        Central request method with error handling.

        :param method: HTTP method (GET, POST, PUT, DELETE, PATCH)
        :param endpoint: API endpoint path (e.g., /v1.0/groups)
        :param kwargs: Additional arguments passed to requests
        :return: Parsed JSON response
        """
        url = f"{self._base_url}{endpoint}"
        headers = self._get_headers()

        self._logger.info(f"Making {method} request to: {url}")

        try:
            response = self._session.request(
                method=method,
                url=url,
                headers=headers,
                timeout=TIMEOUT,
                **kwargs,
            )
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause="Request timed out",
                assistance=f"The request to {url} timed out after {TIMEOUT} seconds. "
                "Please verify network connectivity and try again.",
                data=str(error),
            ) from error
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect",
                assistance=f"Could not connect to {self._base_url}. "
                "Please verify network connectivity and that the endpoint is correct.",
                data=str(error),
            ) from error

        return self._handle_response(response)

    def _handle_response(self, response: requests.Response) -> Union[dict, list, None]:
        """Handle the API response, raising appropriate exceptions for error codes."""
        if response.status_code == 204:
            return None

        if response.status_code >= 400:
            self._handle_error_status(response)

        if not response.content:
            return None

        try:
            return response.json()
        except ValueError as error:
            raise PluginException(
                cause="Non-JSON response received",
                assistance="The server returned a response that could not be parsed as JSON.",
                data=response.text[:500],
            ) from error

    def _handle_error_status(self, response: requests.Response):
        """Map HTTP error codes to PluginExceptions."""
        status_code = response.status_code
        error_info = HTTP_ERROR_MAP.get(status_code)

        if error_info:
            raise PluginException(
                cause=error_info["cause"],
                assistance=error_info["assistance"],
                data=response.text[:1000],
            )

        raise PluginException(
            cause=f"Unexpected HTTP error: {status_code}",
            assistance="An unexpected error occurred. Please contact support if this persists.",
            data=response.text[:1000],
        )

    # ─── Teams / Groups ───────────────────────────────────────────────────────────

    def get_teams(self, team_name: str = None, explicit: bool = True) -> list:
        """
        Get teams from Microsoft Graph.

        :param team_name: Optional team name to filter by
        :param explicit: If True, match exact name; if False, use regex
        :return: List of team objects
        """
        endpoint = self._build_teams_endpoint(team_name, explicit)
        result = self._make_request("GET", endpoint)
        teams = result.get("value", [])
        teams = self._paginate_results(teams, result.get("@odata.nextLink"))

        if team_name:
            return self._filter_teams_by_name(teams, team_name, explicit)

        return teams

    def _build_teams_endpoint(self, team_name: str, explicit: bool) -> str:
        """Build the Graph API endpoint for listing teams."""
        if explicit and team_name:
            parsed_team_name = urllib.parse.quote(team_name, safe="")
            return (
                f"/v1.0/groups?$filter=resourceProvisioningOptions/Any(x:x eq 'Team') "
                f"and displayName eq '{parsed_team_name}'"
            )
        return "/v1.0/groups?$filter=resourceProvisioningOptions/Any(x:x eq 'Team')"

    def _paginate_results(self, items: list, next_link: str) -> list:
        """Follow pagination links and collect all results."""
        while next_link:
            next_result = self._session.get(next_link, headers=self._get_headers(), timeout=TIMEOUT)
            try:
                next_result.raise_for_status()
                next_json = next_result.json()
            except Exception as error:
                raise PluginException(
                    cause="Attempt to get paginated results failed.",
                    assistance="Pagination request failed during retrieval.",
                    data=str(error),
                ) from error
            items.extend(next_json.get("value", []))
            next_link = next_json.get("@odata.nextLink")
        return items

    def _filter_teams_by_name(self, teams: list, team_name: str, explicit: bool) -> list:
        """Filter teams list by name (exact or regex match)."""
        self._logger.info(f"Looking for team: {team_name}")

        compiled_team_name = None
        if not explicit:
            try:
                compiled_team_name = re.compile(team_name)
            except re.error as error:
                raise PluginException(
                    cause=f"Team Name {team_name} was an invalid regular expression.",
                    assistance=f"Please correct {team_name}",
                    data=str(error),
                ) from error

        for team in teams:
            name = team.get("displayName", "")
            if explicit and name == team_name:
                return [team]
            if not explicit and compiled_team_name.search(name):
                return [team]

        raise PluginException(
            cause=f"Team {team_name} was not found.",
            assistance=f"Please verify {team_name} is a valid team name.",
        )

    # ─── Channels ─────────────────────────────────────────────────────────────────

    def get_channels(self, team_id: str, channel_name: str = None) -> list:
        """
        Get channels for a team.

        :param team_id: The team ID
        :param channel_name: Optional channel name to filter by (regex match)
        :return: List of channel objects
        """
        compiled_channel_name = None
        if channel_name:
            try:
                compiled_channel_name = re.compile(channel_name)
            except re.error as error:
                raise PluginException(
                    cause=f"Channel Name {channel_name} was an invalid regular expression.",
                    assistance=f"Please correct {channel_name}",
                    data=str(error),
                ) from error

        endpoint = f"/v1.0/teams/{team_id}/channels"
        result = self._make_request("GET", endpoint)
        channels = result.get("value", [])

        if channel_name:
            self._logger.info(f"Looking for channel: {channel_name}")
            for channel in channels:
                name = channel.get("displayName", "")
                if compiled_channel_name.match(name):
                    return [channel]
            raise PluginException(
                cause=f"Channel {channel_name} was not found.",
                assistance=f"Please verify {channel_name} is a valid channel for the team with id: {team_id}",
            )

        return channels

    def create_channel(self, team_id: str, channel_name: str, description: str, channel_type: str) -> bool:
        """Create a channel in a team."""
        endpoint = f"/v1.0/teams/{team_id}/channels"
        payload = {
            "description": description,
            "displayName": channel_name,
            "membershipType": channel_type.lower(),
        }

        self._logger.info(f"Creating {channel_type} channel: {channel_name}")
        response = self._session.request(
            method="POST",
            url=f"{self._base_url}{endpoint}",
            headers=self._get_headers(),
            json=payload,
            timeout=TIMEOUT,
        )

        if response.status_code == 201:
            return True

        self._handle_error_status(response)
        return False

    def delete_channel(self, team_id: str, channel_id: str) -> bool:
        """Delete a channel from a team."""
        endpoint = f"/v1.0/teams/{team_id}/channels/{channel_id}"

        self._logger.info(f"Deleting channel: {channel_id}")
        response = self._session.request(
            method="DELETE",
            url=f"{self._base_url}{endpoint}",
            headers=self._get_headers(),
            timeout=TIMEOUT,
        )

        if response.status_code == 204:
            return True

        self._handle_error_status(response)
        return False

    # ─── Messages (Read) ──────────────────────────────────────────────────────────

    def get_channel_messages(self, team_id: str, channel_id: str) -> list:
        """Get messages from a channel."""
        endpoint = f"/v1.0/teams/{team_id}/channels/{channel_id}/messages"
        result = self._make_request("GET", endpoint)
        return result.get("value", [])

    def get_channel_message(self, team_id: str, channel_id: str, message_id: str, reply_id: str = None) -> dict:
        """Get a specific message or reply from a channel."""
        if reply_id:
            endpoint = f"/v1.0/teams/{team_id}/channels/{channel_id}/messages/{message_id}/replies/{reply_id}"
        else:
            endpoint = f"/v1.0/teams/{team_id}/channels/{channel_id}/messages/{message_id}"

        result = self._make_request("GET", endpoint)
        return remove_null_and_clean(result)

    def get_chat_message(self, chat_id: str, message_id: str) -> dict:
        """Get a specific message from a chat."""
        endpoint = f"/v1.0/chats/{chat_id}/messages/{message_id}"
        result = self._make_request("GET", endpoint)
        return remove_null_and_clean(result)

    def list_chat_messages(self, chat_id: str, top: int = 50) -> list:
        """List messages from a chat."""
        endpoint = f"/v1.0/chats/{chat_id}/messages?$top={top}&$orderby=createdDateTime desc"
        result = self._make_request("GET", endpoint)
        messages = result.get("value", [])
        return [clean(message) for message in messages]

    def get_message_replies(self, team_id: str, channel_id: str, message_id: str) -> list:
        """Get all replies to a message in a channel."""
        endpoint = f"/v1.0/teams/{team_id}/channels/{channel_id}/messages/{message_id}/replies"
        result = self._make_request("GET", endpoint)
        return clean(result.get("value", []))

    # ─── Users ────────────────────────────────────────────────────────────────────

    def get_user_info(self, user_login: str) -> dict:
        """Get user information by UPN (email)."""
        endpoint = f"/v1.0/users?$filter=userPrincipalName eq '{user_login}'"

        self._logger.info(f"Getting user information for: {user_login}")
        result = self._make_request("GET", endpoint)
        users = result.get("value", [])

        if not users:
            raise PluginException(
                cause=f"User {user_login} was not found.",
                assistance=f"Please verify {user_login} is a valid user principal name.",
            )

        return users[0]

    # ─── Group Management ─────────────────────────────────────────────────────────

    def add_member_to_group(self, group_id: str, user_id: str) -> bool:
        """Add a user as a member to a group."""
        endpoint = f"/v1.0/groups/{group_id}/members/$ref"
        payload = {"@odata.id": f"{self._base_url}/v1.0/directoryObjects/{user_id}"}

        self._logger.info(f"Adding user {user_id} to group {group_id}")
        response = self._session.request(
            method="POST",
            url=f"{self._base_url}{endpoint}",
            headers=self._get_headers(),
            json=payload,
            timeout=TIMEOUT,
        )

        if response.status_code == 204:
            return True

        self._handle_error_status(response)
        return False

    def remove_member_from_group(self, group_id: str, user_id: str) -> bool:
        """Remove a user from a group."""
        endpoint = f"/v1.0/groups/{group_id}/members/{user_id}/$ref"

        self._logger.info(f"Removing user {user_id} from group {group_id}")
        response = self._session.request(
            method="DELETE",
            url=f"{self._base_url}{endpoint}",
            headers=self._get_headers(),
            timeout=TIMEOUT,
        )

        if response.status_code == 204:
            return True

        self._handle_error_status(response)
        return False

    def add_group_owner(self, group_id: str, user_id: str) -> bool:
        """Add a user as an owner of a group."""
        endpoint = f"/v1.0/groups/{group_id}/owners/$ref"
        payload = {"@odata.id": f"{self._base_url}/v1.0/directoryObjects/{user_id}"}

        self._logger.info(f"Adding user {user_id} as owner of group {group_id}")
        response = self._session.request(
            method="POST",
            url=f"{self._base_url}{endpoint}",
            headers=self._get_headers(),
            json=payload,
            timeout=TIMEOUT,
        )

        if response.status_code == 204:
            self._logger.info("User was added as owner successfully.")
            return True
        if response.status_code == 400:
            self._logger.info("User is already an owner of this group.")
            return True

        self._handle_error_status(response)
        return False

    def add_member_to_channel(self, team_id: str, channel_id: str, user_id: str, role: str) -> bool:
        """Add a member to a channel."""
        endpoint = f"/v1.0/teams/{team_id}/channels/{channel_id}/members"
        payload = {
            "@odata.type": "#microsoft.graph.aadUserConversationMember",
            "roles": [role],
            "user@odata.bind": f"{self._base_url}/v1.0/users('{user_id}')",
        }

        self._logger.info(f"Adding user {user_id} to channel {channel_id}")
        response = self._session.request(
            method="POST",
            url=f"{self._base_url}{endpoint}",
            headers=self._get_headers(),
            json=payload,
            timeout=TIMEOUT,
        )

        if response.status_code == 201:
            self._logger.info("User was added to channel successfully.")
            return True
        if response.status_code == 400:
            self._logger.info("User has already been added to the channel.")
            return True

        self._handle_error_status(response)
        return False

    def create_group(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self,
        group_name: str,
        group_description: str,
        group_nickname: str,
        mail_enabled: bool,
        owners: list = None,
        members: list = None,
    ) -> dict:
        """Create a Microsoft 365 group."""
        endpoint = "/v1.0/groups"
        payload = {
            "description": group_description,
            "displayName": group_name,
            "groupTypes": ["Unified"],
            "mailEnabled": mail_enabled,
            "mailNickname": group_nickname,
            "securityEnabled": False,
        }

        if owners:
            owners_payload = self._build_user_references(owners)
            payload["owners@odata.bind"] = owners_payload
        if members:
            members_payload = self._build_user_references(members)
            payload["members@odata.bind"] = members_payload

        self._logger.info(f"Creating group: {group_name}")
        response = self._session.request(
            method="POST",
            url=f"{self._base_url}{endpoint}",
            headers=self._get_headers(),
            json=payload,
            timeout=TIMEOUT,
        )

        if response.status_code == 201:
            try:
                return response.json()
            except ValueError as error:
                raise PluginException(
                    cause="Non-JSON response received",
                    assistance="Group was created but the response could not be parsed.",
                    data=str(error),
                ) from error

        self._handle_error_status(response)
        return {}

    def delete_group(self, group_id: str) -> bool:
        """Delete a group."""
        endpoint = f"/v1.0/groups/{group_id}"

        self._logger.info(f"Deleting group: {group_id}")
        response = self._session.request(
            method="DELETE",
            url=f"{self._base_url}{endpoint}",
            headers=self._get_headers(),
            timeout=TIMEOUT,
        )

        if response.status_code == 204:
            return True

        self._handle_error_status(response)
        return False

    def get_group_id_from_name(self, group_name: str) -> str:
        """Get a group ID by its display name."""
        endpoint = f"/v1.0/groups?$filter=displayName eq '{group_name}'"

        self._logger.info(f"Getting group ID for: {group_name}")
        result = self._make_request("GET", endpoint)
        groups = result.get("value", [])

        if not groups:
            raise PluginException(
                cause=f"Group {group_name} was not found.",
                assistance=f"Please verify {group_name} is a valid group name.",
            )

        return groups[0].get("id")

    def enable_teams_for_group(self, group_id: str) -> bool:
        """Enable Microsoft Teams for a group."""
        endpoint = f"/v1.0/groups/{group_id}/team"
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

        self._logger.info(f"Enabling Teams for group: {group_id}")

        for attempt in range(1, 6):
            response = self._session.request(
                method="PUT",
                url=f"{self._base_url}{endpoint}",
                headers=self._get_headers(),
                json=payload,
                timeout=TIMEOUT,
            )

            if response.status_code == 201:
                self._logger.info("Team was enabled successfully.")
                return True

            self._logger.info(
                f"Attempt {attempt} to enable team failed (status: {response.status_code}). "
                f"Retrying in 10 seconds..."
            )
            sleep(10)

        raise PluginException(
            cause=f"Could not enable Teams for group with ID: {group_id}.",
            assistance="This may be due to a replication delay in Azure. Please try again later.",
            data=f"Status Code: {response.status_code}\nResponse:\n{response.text}",
        )

    # ─── Chats ────────────────────────────────────────────────────────────────────

    def create_chat(self, members: list, topic: str = None) -> dict:
        """Create a new chat."""
        endpoint = "/v1.0/chats"
        payload = {}

        list_members = []
        for member in members:
            formatted_member = {
                "@odata.type": "#microsoft.graph.aadUserConversationMember",
                "roles": [member.get("role", "owner")],
                "user@odata.bind": f"{self._base_url}/v1.0/users('{member.get('user_info')}')",
            }
            list_members.append(formatted_member)

        if len(list_members) == 2:
            payload["chatType"] = "oneOnOne"
        elif len(list_members) > 2:
            payload["chatType"] = "group"
            if topic:
                payload["topic"] = topic
        else:
            raise PluginException(
                cause="Create chat failed.",
                assistance="At least 2 members are required to create a chat.",
            )

        payload["members"] = list_members

        self._logger.info(f"Creating chat with {len(list_members)} members")
        response = self._session.request(
            method="POST",
            url=f"{self._base_url}{endpoint}",
            headers=self._get_headers(),
            json=payload,
            timeout=TIMEOUT,
        )

        if response.status_code == 201:
            try:
                return response.json()
            except ValueError as error:
                raise PluginException(
                    cause="Non-JSON response received",
                    assistance="Chat was created but the response could not be parsed.",
                    data=str(error),
                ) from error

        self._handle_error_status(response)
        return {}

    # ─── Helpers ──────────────────────────────────────────────────────────────────

    def _build_user_references(self, user_logins: list) -> list:
        """Build odata user reference list from user login names."""
        user_refs = []
        for user_login in user_logins:
            user = self.get_user_info(user_login)
            user_id = user.get("id")
            user_refs.append(f"{self._base_url}/v1.0/directoryObjects/{user_id}")
        return user_refs
