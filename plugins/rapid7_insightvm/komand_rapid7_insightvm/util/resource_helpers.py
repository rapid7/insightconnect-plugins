import defusedxml.ElementTree as etree
import urllib3
import re
from requests import Session
from logging import Logger
from insightconnect_plugin_runtime.exceptions import PluginException
from .exceptions import ResourceNotFound
from . import endpoints, resource_requests

# Suppress insecure request messages
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class V1Session:
    """
    Used to authenticate and deauthenticate from the v1 API
    """

    _SUPPORT = "Contact support for assistance"

    def __init__(self, session, logger):
        """
        Creates a new instance of V1Session
        :param session: Session object available to InsightConnect actions/triggers, usually self.connection.session
        :param logger: Logger object available to InsightConnect actions/triggers, usually self.logger
        :return: ResourceHelper object
        """
        self.logger = logger
        self.session = session

    def v1_authenticate(self, console_url: str):
        """
        Authenticates to APIv1 and saves the session with appropriate headers for making v1 requests
        :param console_url: URL to the InsightVM console
        """
        headers = {"Content-Type": "text/xml"}
        login_request = f'<?xml version="1.0" encoding="UTF-8"?><LoginRequest user-id="{self.session.auth.username}" password="{self.session.auth.password}"/>'
        response = self.session.post(
            f"{console_url}/api/1.1/xml",
            data=login_request,
            verify=False,
            headers=headers,
            allow_redirects=False,
        )
        if response.status_code == 200:
            xml_response = etree.fromstring(response.text)
            session_id = xml_response.attrib["session-id"]
            headers = {
                "nexposeCCSessionID": session_id,
                "Cookie": f"nexposeCCSessionID={session_id}",
            }
            self.logger.info("Successfully authenticated to APIv1")
            self.session.headers.update(headers)
        elif response.status_code == 302:
            raise PluginException(cause="Authentication for APIv1 was not valid", assistance=self._SUPPORT)
        else:
            raise PluginException(cause="Failed to obtain an APIv1 session ID.", assistance=self._SUPPORT)

    def v1_deauthenticate(self, console_url: str):
        """
        Deauthenticates an existing APIv1 session using session header data
        :param console_url: URL to the InsightVM console
        """
        self.session.headers.update({"Content-Type": "text/xml"})
        session_id = self.session.headers.get("nexposeCCSessionID", "")
        logout_request = f'<?xml version="1.0" encoding="UTF-8"?><LogoutRequest session-id="{session_id}"/>'
        response = self.session.post(f"{console_url}/api/1.1/xml", data=logout_request, verify=False)

        if response.status_code == 200:
            xml_response = etree.fromstring(response.text)
            status = xml_response.attrib["success"]
            if int(status) == 1:
                self.logger.info("Successfully logged out of APIv1 session")
            else:
                self.logger.info("Session ID for logout not valid, removing APIv1 session ID headers")
            self.session.headers.pop("nexposeCCSessionID")
            self.session.headers.pop("Cookie")
        else:
            raise PluginException(cause="Failed to log out via APIv1", assistance=self._SUPPORT)


class ValidateUser:
    """
    Validates that a user exists and has the correct permissions
    """

    def __init__(self, session: Session, logger: Logger):
        """
        Creates a new instance of ValidateUser
        :param session: Session object available to InsightConnect actions/triggers, usually self.connection.session
        :param logger: Logger object available to InsightConnect actions/triggers, usually self.logger
        :return: ResourceHelper object
        """
        self.logger = logger
        self.session = session
        self.requests = resource_requests.ResourceRequests(session=self.session, logger=self.logger)

    def validate_role_exists(self, console_url: str, role_id: str) -> dict:
        """
        Validate that a provided InsightVM role exists
        :param console_url: URL to the InsightVM console
        :param role_id: ID of the role to validate
        :return: The role provided that it exists, if it does not exist a detailed error is raised
        """
        endpoint = endpoints.Role.roles(console_url, role_id)
        try:
            response = self.requests.resource_request(endpoint=endpoint)
            return response
        except ResourceNotFound:
            # Get roles to provide a better error
            endpoint = endpoints.Role.roles(console_url)
            roles = self.requests.resource_request(endpoint=endpoint)["resources"]
            role_ids = [r["id"] for r in roles]

            error = f"Specified role ID ({role_id}) does not exist, valid role IDs: {role_ids}"
            self.logger.error(error)
            raise ResourceNotFound(error)

    def validate_user_permissions(self, console_url: str, user: dict) -> dict:  # noqa: MC0001
        """
        Validate that user permissions are appropriate given the user's role.
        This is useful when updating a user's role or create a new user as
        some roles required the allSites, allAssetGroups, or superuser parameters
        to be set.
        :param console_url: URL to the InsightVM console
        :param user: dict containing the details for a user (from the InsightVM API or matching the format)
        :return: The user dict with updated permissions if required
        """
        try:
            endpoint = endpoints.Role.roles(console_url, user["role"]["id"])
        except KeyError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)
        role = self.requests.resource_request(endpoint=endpoint)

        # Set All Sites permission if required and not set
        try:
            if not user["role"]["allSites"]:
                for permission in ("all-permissions", "manage-sites", "manage-tags"):
                    if permission in role["privileges"]:
                        self.logger.info(
                            f"Setting 'Access All Sites' to 'true' as it is required based "
                            f"on the permissions for the role '{user['role']['id']}'"
                        )
                        user["role"]["allSites"] = True
                        break
        except KeyError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        # Set All Asset Groups permission if required and not set
        try:
            if not user["role"]["allAssetGroups"]:
                for permission in ("all-permissions", "manage-dynamic-asset-groups"):
                    if permission in role["privileges"]:
                        self.logger.info(
                            f"Setting 'Access All Asset Groups' to 'true' as it is required based "
                            f"on the permissions for the role '{user['role']['id']}'"
                        )
                        user["role"]["allAssetGroups"] = True
                        break
        except KeyError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        # Set superuser permission if required and not set
        # Do this silently as it isn't exposed to the user of the plugin and
        # appears to simply be an internal setting that custom roles cannot have
        try:
            if not user["role"]["superuser"] and (user["role"]["id"] == "global-admin"):
                user["role"]["superuser"] = True
        except KeyError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON)

        return user

    @staticmethod
    def validate_user_email(email: str) -> None:
        """
        Validate a user email address string.
        :param email: Email address to validate
        :return: None, raises an error if validation fails
        """
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if not email_regex.match(email):
            raise PluginException(
                cause="The email address for user account was not valid",
                assistance="Ensure that the email address is correct",
            )

    def validate_user(self, console_url: str, user: dict) -> dict:
        """
        Runs multiple user account data validators pertinent to performing
        user account creation/update operations
        :param console_url: URL to the InsightVM console
        :param user: dict containing the details for a user (from the InsightVM API or matching the format)
        :return: The user dict with updated values if required for validation
        """
        self.validate_role_exists(console_url, user["role"]["id"])
        self.validate_user_email(user["email"])
        user = self.validate_user_permissions(console_url, user)
        return user
