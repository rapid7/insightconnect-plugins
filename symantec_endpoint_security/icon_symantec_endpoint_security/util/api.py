import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

from typing import Optional
from typing import Dict
from typing import Any

from enum import Enum

from logging import Logger
import logging

Agent = Dict[str, Any]
Domain = Dict[str, Any]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class HashType(Enum):
    md5 = "MD5"
    sha256 = "SHA256"


class APIException(Exception):

    def __init__(self, status_code: Optional[int], message: str):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return f"\nStatus code: {self.status_code}\nMessage: {self.message}"


class APIClient(object):
    """
    API client for Symantec Endpoint Protection
    """

    _STATUS_CODES = {
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
    def new_client(cls, host: str, username: str, password: str, domain: str, port: str,
                   logger: Optional[Logger] = None):
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

        if not logger:
            logger = logging.Logger("symantec_api_client", logging.DEBUG)

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
        elif cls._STATUS_CODES.get(response.status_code) is not None:
            raise cls._STATUS_CODES[response.status_code]
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
        elif self._STATUS_CODES.get(response.status_code) is not None:
            raise self._STATUS_CODES[response.status_code]
        else:
            raise APIException(status_code=None, message=f"An unhandled response was received from Symantec Endpoint "
                                                         f"Protection: {response.text}")

    def blacklist_file(self,
                       blacklist_data: [str],
                       blacklist_description: str,
                       domain_id: str,
                       hash_type: HashType,
                       name: Optional[str] = None):
        """
        Blacklists a file hash
        :param blacklist_data: The blacklist file’s data
        :param blacklist_description: The blacklist file’s description
        :param domain_id: The domain ID to which the blacklist file is applied
        :param hash_type: The blacklist file’s hash type, either MD5 or SHA256
        :param name: The blacklist file's ID, only required when updating an existing blacklist file
        :return:
        """

        url = f"{self.base_url}/policy-objects/fingerprints"

        status_codes = {
            **self._STATUS_CODES,
            409: APIException(status_code=409,
                              message="The request could not be completed due to a conflict with the current state "
                                      "of the target resource. The file fingerprint already exists.")
        }

        body = {
            "data": blacklist_data,
            "description": blacklist_description,
            "domainId": domain_id,
            "hashType": hash_type.value,
            "name": name
        }

        response = self.session.post(url=url,
                                     verify=False,
                                     json=body)

        if response.status_code == 200:
            try:
                id_ = response.json()["id"]
                return id_
            except json.JSONDecodeError:
                raise APIException(status_code=None, message="Symantec Endpoint Protection server returned a "
                                                             "non-JSON response!")
            except (KeyError, IndexError):
                return None
        elif status_codes.get(response.status_code) is not None:
            raise status_codes[response.status_code]
        else:
            raise APIException(status_code=None, message=f"An unhandled response was received from Symantec Endpoint "
                                                         f"Protection: {response.text}")

    def get_all_accessible_domains(self) -> [Domain]:
        """
        Returns a list of all accessible Symantec Endpoint Protection Manager domains
        :return: List of domains
        """

        url = f"{self.base_url}/domains"

        response = self.session.get(url=url,
                                    verify=False)

        if response.status_code == 200:
            try:
                domains = response.json()
                return domains
            except json.JSONDecodeError:
                raise APIException(status_code=None, message="Symantec Endpoint Protection server returned a "
                                                             "non-JSON response!")
            except (KeyError, IndexError):
                return None
        elif self._STATUS_CODES.get(response.status_code) is not None:
            raise self._STATUS_CODES[response.status_code]
        else:
            raise APIException(status_code=None, message=f"An unhandled response was received from Symantec Endpoint "
                                                         f"Protection: {response.text}")
