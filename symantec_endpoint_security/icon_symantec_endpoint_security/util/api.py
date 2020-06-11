import requests
import json

from typing import Optional
from typing import Dict
from typing import Any

from logging import Logger

Agent = Dict[str: Any]


class APIException(Exception):

    def __init__(self, status_code: Optional[int], message: str):
        self.status_code = status_code
        self.message = message


class APIClient(object):
    """
    API client for Symantec Endpoint Protection
    """

    STATUS_CODES = {
        400: APIException(status_code=400, message="The parameters are invalid."),
        401: APIException(status_code=401, message="The user that is currently logged on has insufficient rights "
                                                   "to execute the web method, or the user is unauthorized."),
        404: APIException(status_code=404, message="The requested resource was not found."),
        500: APIException(status_code=500, message="The web service encountered an error while processing the web "
                                                   "request.")
    }

    def __init__(self, base_url: str, auth_token: str, logger: Logger):
        self.base_url = base_url
        self.auth_token = auth_token
        self.logger = logger

        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json",
                                "Authorization": f"Bearer {self.auth_token}"}

    @classmethod
    def new_client(cls, host: str, username: str, password: str, domain: str, port: str, logger: Logger):
        """
        Authenticates with Symantec Endpoint Protection and returns an API client
        :param host: Console host
        :param username: Console username
        :param password: Console password
        :param domain: Console domain
        :param port: Console port
        :param logger: Logger to use
        :return: API Client
        """

        url = f"https://{host}:{port}/sepm/api/v1"
        auth_url = f"{url}/identity/authenticate"

        logger.info(f"Authenticating with Symantec Endpoint Protection console at '{url}'")

        auth_body = {"username": username, "password": password, "domain": domain}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=auth_url,
                                 json=auth_body,
                                 headers=headers,
                                 verify=False)
        logger.info(f"Received status code '{response.status_code}' from Symantec Endpoint Protection console.")

        if response.status_code == 200:
            try:
                auth_token = response.json()["token"]
            except json.JSONDecodeError:
                raise APIException(status_code=None, message="Symantec Endpoint Protection server returned a "
                                                             "non-JSON response!")
            except KeyError:
                raise APIException(status_code=None, message="Symantec Endpoint Protection did not return the "
                                                             "authentication token!")
            logger.info("Authentication with Symantec Endpoint Protection console successful!")
            return cls(base_url=url,
                       auth_token=auth_token,
                       logger=logger)
        elif cls.STATUS_CODES.get(response.status_code) is not None:
            raise cls.STATUS_CODES[response.status_code]
        else:
            raise APIException(status_code=None, message=f"An unhandled response was received from Symantec Endpoint "
                                                         f"Protection: {response.text}")

    def get_computer(self, computer_name: str = "*", mac_address: str = "*") -> Optional[Agent]:
        """
        Gets a computer by search with either computer name or MAC address, or both
        :param computer_name: Computer name to search with. Default is wildcard
        :param mac_address: MAC address to search with. Default is wildcard
        :return: First agent that matches the search criteria if one is found, else None
        """

        url = f"{self.base_url}/computers"

        query_params = {"computerName": computer_name, "mac": mac_address}

        response = self.session.get(url=url,
                                    verify=False,
                                    params=query_params)

        if response.status_code == 200:
            try:
                match = response.json()["content"][0]
                return match
            except json.JSONDecodeError:
                raise APIException(status_code=None, message="Symantec Endpoint Protection server returned a "
                                                             "non-JSON response!")
            except (KeyError, IndexError):
                return None
        elif self.STATUS_CODES.get(response.status_code) is not None:
            raise self.STATUS_CODES[response.status_code]
        else:
            raise APIException(status_code=None, message=f"An unhandled response was received from Symantec Endpoint "
                                                         f"Protection: {response.text}")