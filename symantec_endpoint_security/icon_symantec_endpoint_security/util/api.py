import requests
import json
from typing import Optional


class APIException(Exception):

    def __init__(self, status_code: Optional[int], message: str):
        self.status_code = status_code
        self.message = message


class APIClient(object):
    """
    API client for Symantec Endpoint Protection
    """

    def __init__(self, base_url: str, auth_token: str):
        self.base_url = base_url
        self.auth_token = auth_token
        self.session = requests.Session()

    @classmethod
    def new_client(cls, host: str, username: str, password: str, domain: str, port: str):
        """
        Authenticates with Symantec Endpoint Protection and returns an API client
        :param host: Console host
        :param username: Console username
        :param password: Console password
        :param domain: Console domain
        :param port: Console port
        :return: API Client
        """

        url = f"https://{host}:{port}/sepm/api/v1"
        auth_url = f"{url}/identity/authenticate"

        auth_body = {"username": username, "password": password, "domain": domain}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=auth_url,
                                 json=auth_body,
                                 headers=headers,
                                 verify=False)

        status_codes = {
            400: APIException(status_code=400, message="The parameters are invalid."),
            401: APIException(status_code=401, message="The user that is currently logged on has insufficient rights "
                                                       "to execute the web method, or the user is unauthorized."),
            404: APIException(status_code=404, message="The requested resource was not found."),
            500: APIException(status_code=500, message="The web service encountered an error while processing the web "
                                                       "request.")
        }

        if response.status_code == 200:
            try:
                auth_token = response.json()["token"]
            except json.JSONDecodeError:
                raise APIException(status_code=None, message="Symantec Endpoint Protection server returned a "
                                                             "non-JSON response!")
            except KeyError:
                raise APIException(status_code=None, message="Symantec Endpoint Protection did not return the "
                                                             "authentication token!")
            return cls(base_url=url,
                       auth_token=auth_token)
        elif status_codes.get(response.status_code) is not None:
            raise status_codes[response.status_code]
        else:
            raise APIException(status_code=None, message=f"An unhandled response was received from Symantec Endpoint "
                                                         f"Protection: {response.text}")