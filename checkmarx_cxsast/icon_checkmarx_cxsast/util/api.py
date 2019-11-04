from requests import Session, Request, HTTPError
import json
from komand.exceptions import PluginException


class CheckmarxCxSAST:
    def __init__(self, base_url, logger, username, password):
        self.logger = logger
        self._base_url = base_url
        self._username = username
        self._password = password
        self._auth_token = None
        self.session = Session()
        token = self.fetch_token()
        self.session.headers.update({
            "Authorization": f"{token.get('token_type')} {token.get('access_token')}",
            "Accept": "application/json",
            "Content-Type": "application/json;v=1.0",
            "cxOrigin": "Rapid7 - InsightConnect"
        })

    def _call_api(
        self,
        method,
        endpoint,
        params=None,
        data=None,
        action_name=None,
        custom_error=None,
    ):
        url = self._base_url + "/cxrestapi" + endpoint
        req = Request(
            url=url,
            headers=self.session.headers,
            method=method,
            params=params,
            data=data,
        )

        try:
            # Prep request
            req = self.session.prepare_request(req)
            resp = self.session.send(req)
            # Check for custom errors
            if custom_error and resp.status_code not in range(200, 299):
                raise PluginException(
                    cause=f"An error was received when running {action_name}.",
                    assistance=f"""Request status code of {resp.status_code}
                        was returned.\n{custom_error.get(resp.status_code, 000)}""",
                    data=resp.text
                )

            try:
                resp.raise_for_status()
            except HTTPError as e:
                assistance = "Checkmarx CxSAST request failed."
                if resp.status_code in range(401, 403):
                    assistance = f"${assistance} Check your API key. \n"

                raise PluginException(
                    cause=f"Checkmarx CxSAST request for {action_name} failed.",
                    assistance=assistance,
                    data=f"Exception returned was: {e}\nResponse was {resp.text} ",
                )

        except Exception as e:
            self.logger.error(
                f"An error had occurred : {e}"
                "If the issue persists please contact support"
            )
            raise

        try:
            results = resp.json()
            return results
        except json.JSONDecodeError:
            raise PluginException(
                f"Error: Received an unexpected response from {action_name}"
                f"(non-JSON or no response was received). Response was: {resp.text}"
            )

    def fetch_token(self):
        self.auth_token = self._call_api(
            "POST",
            "/auth/identity/connect/token",
            data={
                "username": self._username,
                "password": self._password,
                # all values below must be the same for each request; yes, even the client_secret, which is
                # available in the documentation below:
                # https://checkmarx.atlassian.net/wiki/spaces/KC/pages/1187774721/Using+the+CxSAST+REST+API+v8.6.0+and+up
                "grant_type": "password",
                "scope": "sast_rest_api",
                "client_id": "resource_owner_client",
                "client_secret": "014DF517-39D1-4453-B7B3-9930C563627C",
            }
        )
        return self.auth_token

    def test_api(self):
        return self.fetch_token()

    def create_project(self, project):
        return self._call_api(
            "POST",
            "/projects",
            action_name="Create Project",
            data=json.dumps(project),
        )

    def create_branched_project(self, id, project):
        return self._call_api(
            "POST",
            f"/projects/{id}/branch",
            action_name="Create Branched Project",
            data=json.dumps(project),
        )

    def define_scan_settings(self, scan_settings):
        return self._call_api(
            "POST",
            "/sast/scanSettings",
            action_name="Define Scan Settings",
            data=json.dumps(scan_settings),
        )

    def create_scan(self, scan):
        return self._call_api(
            "POST",
            "/sast/scans",
            action_name="Create Scan",
            data=json.dumps(scan),
        )

    def get_scan_details(self, id):
        return self._call_api(
            "GET",
            f"/sast/scans/{id}",
            action_name="Get Scan Details",
        )
