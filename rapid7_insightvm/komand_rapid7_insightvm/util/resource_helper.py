from . import endpoints
from .exceptions import ResourceNotFound
import json
import re
import requests
import urllib3
import defusedxml.ElementTree as etree
from komand.exceptions import PluginException
from typing import NamedTuple


class RequestResult(NamedTuple):
    """
    Class for data returned in paged InsightVM API requests
    This is the Python 3.6 style for using named tuples with typing
    """
    page_num: int
    total_pages: int
    resources: dict


class TestResult(NamedTuple):
    """
    Class for data returned in test method
    This is the Python 3.6 style for using named tuples with typing
    """
    status: int
    message: str


class ResourceHelper(object):
    """
    Class for helper methods for making requests against the APIv3. A new instance should
    be instantiated within the action/trigger being developed. New methods should be
    created as instance methods to allow reference of the logger and session passed to
    the __init__ function during instantiation.
    """

    _ERRORS = {
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable",
        000: "Unknown Status Code"
    }

    def __init__(self, session, logger):
        """
        Creates a new instance of ResourceHelper
        :param session: Session object available to Komand actions/triggers, usually self.connection.session
        :param logger: Logger object available to Komand actions/triggers, usually self.logger
        :return: ResourceHelper object
        """
        self.logger = logger
        self.session = session

        # Suppress insecure request messages
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def resource_request(self, endpoint: str, method: str = 'get', params: dict = None, payload: dict = None,
                         json_response: bool = True) -> dict:
        """
        Sends a request to APIv3 with the provided endpoint and optional method/payload
        :param endpoint: Endpoint for the APIv3 call defined in endpoints.py
        :param method: HTTP method for the API request
        :param params: URL parameters to append to the request
        :param payload: JSON body for the API request if required
        :param json_response: Boolean to return raw response
        :return: Dict containing the JSON response body
        """
        try:
            request_method = getattr(self.session, method.lower())
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            if not params:
                params = {}
            if payload is None:
                response = request_method(url=endpoint, headers=headers, params=params, verify=False)
            elif 'rawbody' in payload.keys():
                response = request_method(url=endpoint, headers=headers, params=params, data=payload['rawbody'], verify=False)
            else:
                response = request_method(url=endpoint, headers=headers, params=params, json=payload, verify=False)
        except requests.RequestException as e:
            self.logger.error(e)
            raise

        else:
            if response.status_code in [200, 201]:  # 200 is documented, 201 is undocumented
                if json_response:
                    try:
                        resource = response.json()
                    except json.decoder.JSONDecodeError as e:
                        raise PluginException(cause=f"Error: Received an unexpected response from InsightVM "
                                                    f"(non-JSON or no response was received). "
                                                    f"Response was: {response.content}",
                                              assistance=f"Exception returned was {e}")
                else:
                    resource = {"raw": response.content}
            else:
                try:
                    response = response.json()
                    error = response.get("message", {})
                except (KeyError, json.decoder.JSONDecodeError) as e:
                    self.logger.error("Malformed JSON received.")
                    error = f"Unknown error occurred. Please contact support or try again later.\nResponse:\n{response.text}\nException:\n{str(e)}"

                status_code_message = self._ERRORS.get(response.status_code, self._ERRORS[000])
                self.logger.error(f"{status_code_message} ({response.status_code}): {error}")

                if response.status_code == 404:
                    raise ResourceNotFound(error)
                else:
                    raise Exception(error)

        return resource

    def paged_resource_request(self, endpoint: str, method: str = 'get', params: dict = None,
                               payload: dict = None) -> list:
        """
        Fetches all resources from a paged APIv3 endpoint
        :param endpoint: Endpoint for the APIv3 call defined in endpoints.py
        :param method: HTTP method for the API request
        :param params: URL parameters to append to the request
        :param payload: JSON body for the API request if required
        :return: List object of API resources
        """
        resources = []
        current_page = 0

        # Handle various scenarios where params may be passed
        if not params:
            params = {
                "size": 500,
                "page": current_page
            }
        else:
            if 'size' not in params:
                params['size'] = 500
            # Enable requests with arbitrary starting points
            if 'page' in params:
                current_page = params['page']

        while True:
            self.logger.info(f"Fetching results from page {current_page}")
            params['page'] = current_page
            response = self._get_resource_page(endpoint=endpoint,
                                               method=method,
                                               params=params,
                                               payload=payload)

            resources += response.resources  # Grab resources and append to total
            self.logger.info(f"Got {len(response.resources)} resources "
                             f"from page {response.page_num} / {response.total_pages}")

            if (response.total_pages == 0) or ((response.total_pages - 1) == response.page_num):
                self.logger.info("All pages consumed, returning results...")
                break  # exit the loop
            else:
                self.logger.info("More pages exist, fetching...")
                current_page += 1

        return resources

    def _get_resource_page(self, endpoint: str, method: str, params: dict, payload: dict) -> RequestResult:
        """
        Retrieves resources from a security console
        :param endpoint: Endpoint to reach
        :param method: HTTP method for the API request
        :param params: URL parameters to append to the request
        :param payload: JSON body for the API request if required
        :return: Namedtuple object containing current page number, total pages, and results
        """
        self.logger.info(f"Fetching up to {params['size']} resources from endpoint page {params['page']} ...")
        try:
            request_method = getattr(self.session, method.lower())
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            if not payload:
                response = request_method(url=endpoint,
                                          verify=False,
                                          headers=headers,
                                          params=params
                                          )
            else:
                response = request_method(url=endpoint,
                                          verify=False,
                                          headers=headers,
                                          params=params,
                                          json=payload
                                          )
        except requests.RequestException as e:
            self.logger.error(e)
            raise

        else:
            if response.status_code in [200, 201]:  # 200 is documented, 201 is undocumented
                response_json = response.json()

                r = RequestResult(page_num=response_json["page"]["number"],
                                  total_pages=response_json["page"]["totalPages"],
                                  resources=response_json["resources"])

                return r
            else:
                try:
                    error = response.json()["message"]
                except KeyError:
                    error = "Unknown error occurred. Please contact support or try again later."

                status_code_message = self._ERRORS.get(response.status_code, self._ERRORS[000])
                self.logger.error(f"{status_code_message} ({response.status_code}): {error}")

                if response.status_code == 404:
                    raise ResourceNotFound(error)
                else:
                    raise Exception(error)

    def v1_authenticate(self, console_url: str):
        """
        Authenticates to APIv1 and saves the session with appropriate headers for making v1 requests
        :param console_url: URL to the InsightVM console
        """
        headers = {'Content-Type': 'text/xml'}
        login_request = f'<?xml version="1.0" encoding="UTF-8"?><LoginRequest user-id="{self.session.auth.username}" password="{self.session.auth.password}"/>'
        response = self.session.post(f"{console_url}/api/1.1/xml", data=login_request, verify=False,
                                     headers=headers, allow_redirects=False)
        if response.status_code == 200:
            xml_response = etree.fromstring(response.text)
            session_id = xml_response.attrib['session-id']
            headers = {
                "nexposeCCSessionID": session_id,
                "Cookie": f"nexposeCCSessionID={session_id}"
            }
            self.logger.info('Successfully authenticated to APIv1')
            self.session.headers.update(headers)
        elif response.status_code == 302:
            error = "ERROR: Authentication for APIv1 was not valid"
            raise Exception(error)
        else:
            error = "ERROR: Failed to obtain an APIv1 session ID."
            raise Exception(error)

    def v1_deauthenticate(self, console_url: str):
        """
        Deauthenticates an existing APIv1 session using session header data
        :param console_url: URL to the InsightVM console
        """
        self.session.headers.update({'Content-Type': 'text/xml'})
        session_id = self.session.headers.get('nexposeCCSessionID', '')
        logout_request = f'<?xml version="1.0" encoding="UTF-8"?><LogoutRequest session-id="{session_id}"/>'
        response = self.session.post(f"{console_url}/api/1.1/xml", data=logout_request, verify=False)

        if response.status_code == 200:
            xml_response = etree.fromstring(response.text)
            status = xml_response.attrib['success']
            if int(status) == 1:
                self.logger.info('Successfully logged out of APIv1 session')
            else:
                self.logger.info('Session ID for logout not valid, removing APIv1 session ID headers')
            self.session.headers.pop('nexposeCCSessionID')
            self.session.headers.pop('Cookie')
        else:
            error = "ERROR: Failed to log out via APIv1"
            raise Exception(error)

    @staticmethod
    def test(session: requests.Session, console_url: str) -> TestResult:
        """
        Tests connectivity to the InsightVM Console via administrative info endpoint
        :param session: Requests session populated with basic auth credentials
        :param console_url: URL to the InsightVM console
        :return: Namedtuple indicating connectivity (true = success, false = fail) and error message (if one exists)
        """

        endpoint = endpoints.Administration.get_info(console_url)
        response = None
        try:
            response = session.get(url=endpoint, verify=False)
        except requests.RequestException:
            if response:
                return TestResult(000, response.json()["message"])
            else:
                return TestResult(000, 'Failed to connect to InsightVM Console')
        else:
            status = response.status_code in [200, 201]
            if status:
                return TestResult(status, '')
            return TestResult(status, response.json()["message"])

    # Validators
    def validate_role_exists(self, console_url: str, role_id: str) -> dict:
        """
        Validate that a provided InsightVM role exists
        :param console_url: URL to the InsightVM console
        :param role_id: ID of the role to validate
        :return: The role provided that it exists, if it does not exist a detailed error is raised
        """
        endpoint = endpoints.Role.roles(console_url, role_id)
        try:
            response = self.resource_request(endpoint=endpoint)
            return response
        except ResourceNotFound:
            # Get roles to provide a better error
            endpoint = endpoints.Role.roles(console_url)
            roles = self.resource_request(endpoint=endpoint)['resources']
            role_ids = [r['id'] for r in roles]

            error = f"ERROR: Specified role ID ({role_id}) does not exist, valid role IDs: {role_ids}"
            self.logger.error(error)
            raise ResourceNotFound(error)

    def validate_user_permissions(self, console_url: str, user: dict) -> dict:
        """
        Validate that user permissions are appropriate given the user's role.
        This is useful when updating a user's role or create a new user as
        some roles required the allSites, allAssetGroups, or superuser parameters
        to be set.
        :param console_url: URL to the InsightVM console
        :param user: dict containing the details for a user (from the InsightVM API or matching the format)
        :return: The user dict with updated permissions if required
        """
        endpoint = endpoints.Role.roles(console_url, user['role']['id'])
        role = self.resource_request(endpoint=endpoint)

        # Set All Sites permission if required and not set
        if not user['role']['allSites']:
            for permission in ("all-permissions", "manage-sites", "manage-tags"):
                if permission in role['privileges']:
                    self.logger.info(
                        f"Setting 'Access All Sites' to 'true' as it is required based "
                        f"on the permissions for the role '{user['role']['id']}'"
                    )
                    user['role']['allSites'] = True
                    break

        # Set All Asset Groups permission if required and not set
        if not user['role']['allAssetGroups']:
            for permission in ("all-permissions", "manage-dynamic-asset-groups"):
                if permission in role['privileges']:
                    self.logger.info(
                        f"Setting 'Access All Asset Groups' to 'true' as it is required based "
                        f"on the permissions for the role '{user['role']['id']}'"
                    )
                    user['role']['allAssetGroups'] = True
                    break

        # Set superuser permission if required and not set
        # Do this silently as it isn't exposed to the user of the plugin and
        # appears to simply be an internal setting that custom roles cannot have

        if not user['role']['superuser'] and (user['role']['id'] == 'global-admin'):
            user['role']['superuser'] = True

        return user

    def validate_user_email(self, email: str) -> None:
        """
        Validate a user email address string.
        :param email: Email address to validate
        :return: None, raises an error if validation fails
        """
        email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')

        if not email_regex.match(email):
            error = 'ERROR: Email address for user account was not valid!'
            self.logger.error(error)
            raise Exception(error)

    def validate_user(self, console_url: str, user: dict) -> dict:
        """
        Runs multiple user account data validators pertinent to performing
        user account creation/update operations
        :param console_url: URL to the InsightVM console
        :param user: dict containing the details for a user (from the InsightVM API or matching the format)
        :return: The user dict with updated values if required for validation
        """
        self.validate_role_exists(console_url, user['role']['id'])
        self.validate_user_email(user['email'])
        user = self.validate_user_permissions(console_url, user)
        return user
