import json
from requests import Session, Request, request
from json import JSONDecodeError
from urllib.parse import urlencode


class Cherwell:

    TOKEN = ""

    def __init__(self, base_url, logger, username, password, client_id, authentication_mode):
        self._base_url = base_url
        self.logger = logger
        self.username = username
        self.password = password
        self.client_id = client_id
        self.authentication_mode = authentication_mode
        self.session = Session()

    def _call_api(self, method, endpoint, params=None, data=None, json=None, action_name=None, custom_error=None):
        url = self._base_url + endpoint

        if "Authorization" not in self.session.headers:
            Cherwell.TOKEN = self._token(self.client_id, self.username, self.password, self.authentication_mode)
            self.session.headers.update({"Authorization": f"Bearer {Cherwell.TOKEN}",
                                         "Content-Type": "application/json",
                                         "Accept": "application/json"})

        # Build request
        req = Request(
            url=url,
            method=method,
            params=params,
            data=data,
            json=json,
            headers=self.session.headers
        )

        try:
            # Prep request
            req = req.prepare()
            resp = self.session.send(req)
            # Check for custom errors
            if custom_error and resp.status_code not in range(200, 299):
                raise Exception(
                    f"An error was received when running {action_name}."
                    f"Request status code of {resp.status_code} was returned."
                    f"{custom_error.get(resp.status_code, custom_error.get(000))}"
                )
            elif resp.status_code == 405:
                raise Exception(
                    f"An error was received when running {action_name}."
                    f"Request status code of {resp.status_code} was returned."
                    "Please make sure connections have been configured correctly")
            elif resp.status_code != 200:
                raise Exception(
                    f"An error was received when running {action_name}."
                    f" Request status code of {resp.status_code} was returned."
                    " Please make sure connections have been configured correctly "
                    f"as well as the correct input for the action. Response was: {resp.text}")

        except Exception as e:
            self.logger.error(f"An error had occurred : {e}"
                              "If the issue persists please contact support")
            raise

        try:
            results = resp.json()
            return results
        except JSONDecodeError:
            raise Exception(
                f"Error: Received an unexpected response from {action_name}"
                f"(non-JSON or no response was received). Response was: {resp.text}")

    def _token(self, client_id: str, username: str, password: str, authentication_mode: str, debug=False) -> str:
        """
        Issues an authorization request to the Cherwell server asking for an access token.
        :param client_id: Client ID
        :param username: Cherwell account username
        :param password: Cherwell account password
        :param authentication_mode: Authentication mode used by the Cherwell server
        :param debug: If true, log the response data
        :return: Access token as a string
        """
        url = self._base_url + "/CherwellAPI/token"

        querystring = {"auth_mode": authentication_mode}

        query_params = urlencode({
            "grant_type": "password",
            "client_id": client_id,
            "username": username,
            "password": password
        })

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }

        response = request("POST", url=url, data=query_params, headers=headers, params=querystring)

        # Check status code - this is a great early indicator of success/failure. If non-2xx, bail early.
        if response.status_code not in range(200, 299):
            raise Exception(
                "Error: Received HTTP %d status code from Cherwell. Please verify your Cherwell server "
                "status and try again. If the issue persists please contact support. "
                "Get Access Token - Server response was: %s" % (response.status_code, response.text))

        # Let's see if we actually have a JSON response from the server. It looks bad if we dump a JSONDecodeError
        # on the user. Plus, this will allow us to print out the server response in lieu of the proper JSON one.
        try:
            response_data = response.json()
        except JSONDecodeError:
            raise Exception("Error: Received an unexpected response from Cherwell during authentication "
                            "(non-JSON or no response was received). Response was: %s" % response.text)

        if debug:
            self.logger.debug(f"Auth Request Response: {response_data}")

        # Verify the access token is present in the response. If not, there is something wrong.
        if "access_token" in response_data:
            return response_data["access_token"]
        else:
            raise Exception("Error: Authentication access token was not present in the authentication response from "
                            "the Cherwell server. Please verify the status of your Cherwell server and try again. "
                            "If the issue persists please contact support.")

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
            000: "An unknown error occurred. Please contact support for assistance"
        }

        return self._call_api("POST", "/CherwellAPI/api/V1/getsearchresults", data=json.dumps(search_params), action_name="Ad Hoc Search", custom_error=ERROR_MESSAGES)

    def get_businessobjecttemplate(self, bo_template):
        return self._call_api("POST", "/CherwellAPI/api/V1/GetBusinessObjectTemplate", data=json.dumps(bo_template))

    def get_incident(self, busobid, publicid):
        return self._call_api("GET", f"/CherwellAPI/api/V1/getbusinessobject/busobid/{busobid}/publicid/{publicid}", action_name="Lookup Incident")

    def create_incident(self, busOb):
        return self._call_api("POST", "/CherwellAPI/api/V1/SaveBusinessObject", data=json.dumps(busOb), action_name="Create Incident")

    def get_serviceinfo(self):
        return self._call_api("GET", "/CherwellAPI/api/V1/serviceinfo", action_name="Connection Test")

    def update_incident(self, business_object):
        return self._call_api("POST", "/CherwellAPI/api/V1/SaveBusinessObject",
                              data=json.dumps(business_object),
                              action_name="Update Incident")
