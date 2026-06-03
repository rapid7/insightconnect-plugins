import re
import urllib.parse
from logging import Logger
from time import sleep
from typing import Union

from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

from icon_microsoft_teams.util.base_client import BaseClient
from icon_microsoft_teams.util.constants import GRAPH_SCOPE_DEFAULT, AUTH_URL
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean


class GraphApiClient(BaseClient):
    """Microsoft Graph API client using application-only (client_credentials) authentication."""

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self, app_id: str, app_secret: str, tenant_id: str, base_url: str, endpoint: str, logger: Logger
    ):
        """
        Initialize the Graph API client.

        :param app_id: Azure App Registration client ID
        :type app_id: str

        :param app_secret: Azure App Registration client secret
        :type app_secret: str

        :param tenant_id: Azure AD tenant ID
        :type tenant_id: str

        :param base_url: Graph API base URL (e.g., https://graph.microsoft.com)
        :type base_url: str

        :param endpoint: Endpoint type (Normal, GCC, etc.) for auth URL resolution
        :type endpoint: str

        :param logger: Logger instance
        :type logger: Logger
        """
        super().__init__(
            app_id=app_id,
            app_secret=app_secret,
            tenant_id=tenant_id,
            auth_url=AUTH_URL.get(endpoint, "https://login.microsoftonline.com"),
            scope=GRAPH_SCOPE_DEFAULT,
            logger=logger,
        )
        self._base_url = base_url

    def test(self):
        """
        Test Graph API connectivity by authenticating and calling the organization endpoint.

        :raises PluginException: If authentication or API call fails
        """
        try:
            self._authenticate()
            self._make_request("GET", "/v1.0/organization")
        except PluginException:
            raise
        except Exception as error:
            raise PluginException(
                cause="Graph API connection test failed.",
                assistance="Please verify your Application ID, Directory ID, and Application Secret. "
                "Ensure the app registration has Microsoft Graph application permissions with admin consent.",
                data=error,
            ) from error

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Union[dict, list]:
        """
        Make a Graph API request with authentication.

        :param method: HTTP method
        :type method: str

        :param endpoint: API endpoint path (e.g., /v1.0/groups)
        :type endpoint: str

        :param kwargs: Additional arguments (json, params, etc.)

        :return: Parsed JSON response
        :rtype: Union[dict, list]
        """
        url = f"{self._base_url}{endpoint}"
        headers = self._get_auth_headers()
        self._logger.info(f"Making {method} request to: {url}")
        response = self._call_api(method, url, headers=headers, **kwargs)
        return self._handle_json_response(response)

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
            response = self._call_api("GET", next_link, headers=self._get_auth_headers())
            try:
                response.raise_for_status()
                next_json = response.json()
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
        url = f"{self._base_url}{endpoint}"
        response = self._call_api("POST", url, headers=self._get_auth_headers(), json=payload)

        if response.status_code == 201:
            return True

        self._raise_for_status(response)
        return False

    def delete_channel(self, team_id: str, channel_id: str) -> bool:
        """Delete a channel from a team."""
        endpoint = f"/v1.0/teams/{team_id}/channels/{channel_id}"

        self._logger.info(f"Deleting channel: {channel_id}")
        url = f"{self._base_url}{endpoint}"
        response = self._call_api("DELETE", url, headers=self._get_auth_headers())

        if response.status_code == 204:
            return True

        self._raise_for_status(response)
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
        url = f"{self._base_url}{endpoint}"
        response = self._call_api("POST", url, headers=self._get_auth_headers(), json=payload)

        if response.status_code == 204:
            return True

        self._raise_for_status(response)
        return False

    def remove_member_from_group(self, group_id: str, user_id: str) -> bool:
        """Remove a user from a group."""
        endpoint = f"/v1.0/groups/{group_id}/members/{user_id}/$ref"

        self._logger.info(f"Removing user {user_id} from group {group_id}")
        url = f"{self._base_url}{endpoint}"
        response = self._call_api("DELETE", url, headers=self._get_auth_headers())

        if response.status_code == 204:
            return True

        self._raise_for_status(response)
        return False

    def add_group_owner(self, group_id: str, user_id: str) -> bool:
        """Add a user as an owner of a group."""
        endpoint = f"/v1.0/groups/{group_id}/owners/$ref"
        payload = {"@odata.id": f"{self._base_url}/v1.0/directoryObjects/{user_id}"}

        self._logger.info(f"Adding user {user_id} as owner of group {group_id}")
        url = f"{self._base_url}{endpoint}"
        response = self._call_api("POST", url, headers=self._get_auth_headers(), json=payload)

        if response.status_code == 204:
            self._logger.info("User was added as owner successfully.")
            return True
        if response.status_code == 400:
            self._logger.info("User is already an owner of this group.")
            return True

        self._raise_for_status(response)
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
        url = f"{self._base_url}{endpoint}"
        response = self._call_api("POST", url, headers=self._get_auth_headers(), json=payload)

        if response.status_code == 201:
            self._logger.info("User was added to channel successfully.")
            return True
        if response.status_code == 400:
            self._logger.info("User has already been added to the channel.")
            return True

        self._raise_for_status(response)
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
            payload["owners@odata.bind"] = self._build_user_references(owners)
        if members:
            payload["members@odata.bind"] = self._build_user_references(members)

        self._logger.info(f"Creating group: {group_name}")
        url = f"{self._base_url}{endpoint}"
        response = self._call_api("POST", url, headers=self._get_auth_headers(), json=payload)

        if response.status_code == 201:
            try:
                return response.json()
            except ValueError as error:
                raise PluginException(
                    cause="Non-JSON response received",
                    assistance="Group was created but the response could not be parsed.",
                    data=str(error),
                ) from error

        self._raise_for_status(response)
        return {}

    def delete_group(self, group_id: str) -> bool:
        """Delete a group."""
        endpoint = f"/v1.0/groups/{group_id}"

        self._logger.info(f"Deleting group: {group_id}")
        url = f"{self._base_url}{endpoint}"
        response = self._call_api("DELETE", url, headers=self._get_auth_headers())

        if response.status_code == 204:
            return True

        self._raise_for_status(response)
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
        url = f"{self._base_url}{endpoint}"
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
            response = self._call_api("PUT", url, headers=self._get_auth_headers(), json=payload)

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

    def create_chat(self, members: list, topic: str = None, installed_apps: list = None) -> dict:
        """Create a new chat, optionally installing apps (e.g. bots) into the chat."""
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

        # Add installed apps (bots) to the chat at creation time
        if installed_apps:
            payload["installedApps"] = [
                {"teamsApp@odata.bind": f"{self._base_url}/v1.0/appCatalogs/teamsApps/{app_id}"}
                for app_id in installed_apps
            ]

        self._logger.info(f"Creating chat with {len(list_members)} members")
        if installed_apps:
            self._logger.info(f"Installing {len(installed_apps)} app(s) into chat")

        url = f"{self._base_url}{endpoint}"
        response = self._call_api("POST", url, headers=self._get_auth_headers(), json=payload)

        if response.status_code == 201:
            try:
                return response.json()
            except ValueError as error:
                raise PluginException(
                    cause="Non-JSON response received",
                    assistance="Chat was created but the response could not be parsed.",
                    data=str(error),
                ) from error

        # When installedApps is included, the API returns 202 Accepted with an async operation
        if response.status_code == 202:
            return self._handle_async_chat_creation(response)

        self._raise_for_status(response)
        return {}

    def _handle_async_chat_creation(self, response, max_attempts: int = 10, poll_interval: int = 3) -> dict:
        """
        Handle the 202 Accepted response from chat creation with installed apps.

        The Location header contains the operation URL. We extract the chat ID
        and attempt to fetch the chat directly. If not ready yet, we poll the
        operation endpoint until it succeeds.
        """
        location = response.headers.get("Location", "")
        self._logger.info(f"Chat creation is async (202 Accepted). Location: {location}")

        # Extract the chat ID from the location path: /chats('<chat_id>')/operations(...)
        chat_id = self._extract_chat_id_from_location(location)
        self._logger.info(f"Extracted chat ID: {chat_id}")

        if not chat_id and not location:
            raise PluginException(
                cause="Chat creation returned 202 but no Location header",
                assistance="The chat may have been created but we cannot confirm. Check Teams manually.",
            )

        # Try fetching the chat directly first — it's often available immediately
        if chat_id:
            sleep(2)  # Brief pause to let provisioning complete
            try:
                chat_result = self._make_request("GET", f"/v1.0/chats/{chat_id}")
                if chat_result and chat_result.get("id"):
                    self._logger.info("Chat fetched successfully on first attempt")
                    return chat_result
            except PluginException:
                self._logger.info("Chat not ready yet, falling back to polling operation")

        # Fall back to polling the operation endpoint
        if location:
            # The Location header may or may not include /v1.0 — normalize it
            if location.startswith("/chats("):
                operation_url = f"{self._base_url}/v1.0{location}"
            else:
                operation_url = f"{self._base_url}{location}"

            self._logger.info(f"Polling operation URL: {operation_url}")

            for attempt in range(max_attempts):
                sleep(poll_interval)
                self._logger.info(f"Polling chat creation operation (attempt {attempt + 1}/{max_attempts})")
                poll_response = self._call_api("GET", operation_url, headers=self._get_auth_headers())

                if poll_response.status_code == 200:
                    try:
                        result = poll_response.json()
                    except ValueError:
                        continue

                    status = result.get("status", "").lower()
                    self._logger.info(f"Operation status: {status}")

                    if status in ("succeeded", "completed"):
                        self._logger.info("Chat creation operation succeeded")
                        if chat_id:
                            return self._make_request("GET", f"/v1.0/chats/{chat_id}")
                        return result
                    elif status == "failed":
                        raise PluginException(
                            cause="Chat creation operation failed",
                            assistance="The async chat creation operation reported a failure.",
                            data=str(result),
                        )
                    # Otherwise still in progress — continue polling
                elif poll_response.status_code == 404:
                    # Operation endpoint gone — try fetching chat directly
                    self._logger.info("Operation endpoint returned 404, attempting direct chat fetch")
                    if chat_id:
                        try:
                            return self._make_request("GET", f"/v1.0/chats/{chat_id}")
                        except PluginException:
                            continue

        # Exhausted retries — try one final direct fetch
        if chat_id:
            try:
                chat_result = self._make_request("GET", f"/v1.0/chats/{chat_id}")
                if chat_result and chat_result.get("id"):
                    self._logger.info("Chat fetched successfully after polling exhausted")
                    return chat_result
            except PluginException:
                pass
            # Return partial result with the ID so the user still has something to work with
            self._logger.warning("Chat creation polling exhausted — returning partial result with chat ID")
            return {"id": chat_id, "chatType": "unknown", "status": "provisioning"}

        raise PluginException(
            cause="Chat creation timed out",
            assistance="The chat creation operation did not complete within the expected time. "
            "The chat may still be provisioning. Please check Teams.",
        )
        raise PluginException(
            cause="Chat creation timed out",
            assistance="The chat creation operation did not complete within the expected time. "
            "The chat may still be provisioning. Please check Teams.",
        )

    @staticmethod
    def _extract_chat_id_from_location(location: str) -> str:
        """
        Extract chat ID from the Location header path.

        Expected format: /chats('19:xxx@unq.gbl.spaces')/operations('...')
        """
        if not location:
            return ""
        import re

        match = re.search(r"/chats\('([^']+)'\)", location)
        if match:
            return match.group(1)
        return ""

    # ─── Helpers ──────────────────────────────────────────────────────────────────

    def _build_user_references(self, user_logins: list) -> list:
        """
        Build odata user reference list from user login names.

        :param user_logins: List of user principal names
        :type user_logins: list

        :return: List of odata directory object references
        :rtype: list
        """
        return [
            f"{self._base_url}/v1.0/directoryObjects/{self.get_user_info(login).get('id')}" for login in user_logins
        ]
