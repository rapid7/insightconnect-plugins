import json
from requests import Session, Request
from json import JSONDecodeError


class Kolide:

    def __init__(self, base_url, logger, api_token, verify):
        self._base_url = base_url
        self.logger = logger
        self.api_token = api_token
        self.verify = verify
        self.session = Session()
        self._set_header(api_token)

    def _set_header(self, api_token):
        self.session.headers.update({"Authorization": f"Bearer {api_token}"})

    def _call_api(self, method, endpoint, params=None, data=None, json=None, action_name=None, custom_error=None):

        url = self._base_url + endpoint

        req = Request(
            url=url,
            method=method,
            params=params,
            data=data,
            json=json,
            headers=self.session.headers
        )
        # Build request

        try:
            # Prep request
            req = req.prepare()
            resp = self.session.send(req, verify=self.verify)
            # Check for custom errors
            if custom_error and resp.status_code not in range(200, 299):
                raise Exception(
                    f"An error was received when running {action_name}."
                    f"Request status code of {resp.status_code} was returned."
                    f"{custom_error.get(resp.status_code, 000)}"
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

    def get_me(self):
        return self._call_api("GET", "/v1/kolide/me", action_name="Connection Test")

    def create_query(self, payload):
        return self._call_api("POST", "/v1/kolide/queries", json=payload, action_name="Create Query")

    def run_query(self, payload):
        self.logger.info(json.dumps(payload))
        return self._call_api("POST", "/v1/kolide/queries/run", json=payload, action_name="Run Query")

    def get_query(self, queryID):
        return self._call_api("GET", f"/v1/kolide/queries/{queryID}", action_name="Get Query")
