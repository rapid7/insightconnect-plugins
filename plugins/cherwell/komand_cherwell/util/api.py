import json

import requests.exceptions
from requests import Session, Request, request, Response
from json import JSONDecodeError
from urllib.parse import urlencode
from insightconnect_plugin_runtime.exceptions import PluginException


class Cherwell:

    TOKEN = ""  # noqa: B105

    def __init__(self, base_url, logger, username, password, client_id, authentication_mode, ssl_verify):
        self._base_url = base_url
        self.logger = logger
        self.username = username
        self.password = password
        self.client_id = client_id
        self.authentication_mode = authentication_mode
        self.ssl_verify = ssl_verify
        self.session = Session()

    def _call_api(
        self,
        method,
        endpoint,
        params=None,
        data=None,
        json=None,
        action_name=None,
        custom_error=None,
    ):
        url = self._base_url + endpoint

        if "Authorization" not in self.session.headers:
            self.logger.info("Authorization not in session headers, generating token...")
            self.logger.info(f"Using authentication mode {self.authentication_mode}")
            Cherwell.TOKEN = self._token(
                self.client_id,
                self.username,
                self.password,
                self.authentication_mode,
                self.ssl_verify,
            )
            self.session.headers.update(
                {
                    "Authorization": f"Bearer {Cherwell.TOKEN}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                }
            )

        # Build request
        req = Request(
            url=url,
            method=method,
            params=params,
            data=data,
            json=json,
            headers=self.session.headers,
        )

        try:
            # Prep request
            req = req.prepare()
            resp = self.session.send(req, verify=self.ssl_verify)
            self.response_handler(resp, action_name, custom_error)
            results = resp.json()
            return results
        except requests.exceptions.HTTPError as exception:
            self.logger.error(f"An error had occurred : {exception}" "If the issue persists please contact support")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=exception)
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=resp.text)

    def response_handler(self, resp: Response, action_name: str = "", custom_error=None) -> None:
        if resp.status_code in range(200, 299):
            return
        cause_info = f"An error was received when running {action_name}."
        assistance_info = f"Request status code of {resp.status_code} was returned."
        data = None
        if resp.status_code == 405:
            assistance_info += " Please make sure connections have been configured correctly."
        elif custom_error and resp.status_code not in range(200, 299):
            data = f"{custom_error.get(resp.status_code, custom_error.get(000))}"
        else:
            assistance_info += (
                " Please make sure connections have been configured correctly as well as the correct "
                "input for the action."
            )
            data = f"Response was: {resp.text}"
        raise PluginException(cause=cause_info, assistance=assistance_info, data=data)

    def _token(self, client_id: str, username: str, password: str, authentication_mode: str, verify: bool) -> str:
        """
        Issues an authorization request to the Cherwell server asking for an access token.
        :param client_id: Client ID
        :param username: Cherwell account username
        :param password: Cherwell account password
        :param authentication_mode: Authentication mode used by the Cherwell server
        :param verify: SSL Verification bool
        :return: Access token as a string
        """
        url = self._base_url + "/CherwellAPI/token"

        querystring = {"auth_mode": authentication_mode}

        query_params = urlencode(
            {
                "grant_type": "password",
                "client_id": client_id,
                "username": username,
                "password": password,
            }
        )

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }
        response = request("POST", url=url, data=query_params, headers=headers, params=querystring, verify=verify)

        # Check status code - this is a great early indicator of success/failure. If non-2xx, bail early.
        if response.status_code not in range(200, 299):
            raise PluginException(
                cause=f"Error: Received HTTP {response.status_code} status code from Cherwell."
                "Please verify your Cherwell server status and try again.",
                assistance="If the issue persists please contact support.",
                data=response.text,
            )

        # Let's see if we actually have a JSON response from the server. It looks bad if we dump a JSONDecodeError
        # on the user. Plus, this will allow us to print out the server response in lieu of the proper JSON one.
        try:
            response_data = response.json()
        except JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)

        # Verify the access token is present in the response. If not, there is something wrong.
        if "access_token" in response_data:
            return response_data.get("access_token")
        else:
            raise PluginException(
                cause="Error: Authentication access token was not present in the authentication response from "
                "the Cherwell server.",
                assistance="Please verify the status of your Cherwell server and try again. "
                "If the issue persists please contact support.",
            )

    def get_businessobjectsummary(self, busOb):
        return self._call_api("GET", f"/CherwellAPI/api/V1/getbusinessobjectsummary/busobname/{busOb}")

    def get_businessobjectschema(self, busObId):
        return self._call_api("GET", f"/CherwellAPI/api/V1/getbusinessobjectschema/busobid/{busObId}")

    def get_searchresults(self, search_params):
        ERROR_MESSAGES = {
            400: "Action input was incorrect. Please check to ensure all required parameters are present and "
            "try again. If the issue persists please contact support",
            402: "Request to Cherwell failed. Please ensure all required parameters are correct and try again. "
            "If the issue persists please contact support",
            404: "A requested Cherwell resource was not found. Please verify that it exists in your Cherwell "
            "environment and try again. If the issue persists please contact support",
            000: "An unknown error occurred. Please contact support for assistance",
        }

        return self._call_api(
            "POST",
            "/CherwellAPI/api/V1/getsearchresults",
            data=json.dumps(search_params),
            action_name="Ad Hoc Search",
            custom_error=ERROR_MESSAGES,
        )

    def get_businessobjecttemplate(self, bo_template):
        return self._call_api("POST", "/CherwellAPI/api/V1/GetBusinessObjectTemplate", data=json.dumps(bo_template))

    def get_incident(self, busobid, publicid):
        return self._call_api(
            "GET",
            f"/CherwellAPI/api/V1/getbusinessobject/busobid/{busobid}/publicid/{publicid}",
            action_name="Lookup Incident",
        )

    def create_incident(self, busOb):
        return self._call_api(
            "POST",
            "/CherwellAPI/api/V1/SaveBusinessObject",
            data=json.dumps(busOb),
            action_name="Create Incident",
        )

    def get_serviceinfo(self):
        return self._call_api("GET", "/CherwellAPI/api/V1/serviceinfo", action_name="Connection Test")

    def update_incident(self, business_object):
        return self._call_api(
            "POST",
            "/CherwellAPI/api/V1/SaveBusinessObject",
            data=json.dumps(business_object),
            action_name="Update Incident",
        )
