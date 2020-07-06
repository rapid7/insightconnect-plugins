from .schema import ConnectionSchema, Input
import insightconnect_plugin_runtime
# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
import json
import requests
import time


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.session = requests.Session()
        self.resource_url = "https://api.securitycenter.windows.com"


    def connect(self, params):
        self.logger.info("Connecting...")

        self.app_id = params.get(Input.APPLICATION_ID)
        self.app_secret = params.get(Input.APPLICATION_SECRET).get("secretKey")
        self.tenant = params.get(Input.DIRECTORY_ID)

        self.auth_url = f"https://login.windows.net/{self.tenant}/oauth2/token"

        self.api_token = ""

        # Auth tokens expire after 1 hour. Only make that call if we need to
        self.time_ago = 0  # Jan 1, 1970
        self.time_now = time.time()  # More than 1 hour since 1978

        self.check_and_refresh_api_token()
        self.logger.info("Setup Complete")

    def check_and_refresh_api_token(self, force_refresh_token=False):
        self.time_now = time.time()
        self.logger.info(f"Time Now: {self.time_now}")
        self.logger.info(f"Time Ago: {self.time_ago}")
        self.logger.info(f"Seconds elapsed:{int(self.time_now - self.time_ago)}")

        if (self.time_now - self.time_ago) > 3500 or force_refresh_token:  # 1 hour in seconds (minus some buffer time)
            self.logger.info("Refreshing auth token")
            self.get_token()
            self.time_ago = time.time()
        else:
            self.logger.info("Token is valid, not refreshing.")

    def get_token(self):
        self.logger.info("Updating Auth Token...")
        payload = {
            "resource": self.resource_url,
            "client_id": self.app_id,
            "client_secret": self.app_secret,
            "grant_type": "client_credentials"
        }

        self.logger.info(f"Getting token from: {self.auth_url}")
        result = requests.post(self.auth_url, data=payload)

        try:
            result.raise_for_status()
        except Exception:
            raise PluginException(cause="Authentication to Microsoft Graph failed.",
                                  assistance=f"Some common causes for this error are invalid connection settings."
                                             f"Verify that your Application ID, Application Secret, and Directory ID are correct.\n"
                                             f"The result returned was:\n{result.text}")

        result_json = result.json()
        self.api_token = result_json.get("access_token")
        self.logger.info(f"Authentication was successful, token is: ******************{self.api_token[-5:]}")
        self.update_session_headers()

    def update_session_headers(self):
        self.logger.info("Updating session headers.")
        session_headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        self.session.headers.update(session_headers)
        self.logger.info("Session headers updated successfully.")

    def get_all_alerts(self, query_parameters=""):
        self.check_and_refresh_api_token()

        endpoint = "https://api.securitycenter.windows.com/api/alerts"
        if query_parameters:
            endpoint += query_parameters


        self.logger.info(f"Connecting to: {endpoint}")
        response = self.session.get(endpoint)

        try:
            response.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(cause=f"Connection error occurred while connecting to: {endpoint}.\nError "
                                                f"was: {e}\n",
                                          assistance=response.text)
        return response

    def get_alerts_by_key_value(self, key, value):
        self.check_and_refresh_api_token()

        endpoint = "https://api.securitycenter.windows.com/api/alerts"
        self.logger.info(f"Connecting to: {endpoint}")
        response = self.session.get(endpoint)

        try:
            response.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(cause=f"Connection error occurred while connecting to: {endpoint}.\nError "
                                                f"was: {e}\n",
                                          assistance=response.text)

        self.logger.info("Looking for {} matching {}".format(value, key))

        try:
            matching_alerts = list(filter(lambda a: a.get(key) == value, response.json()))
        except json.JSONDecodeError as e:
            self.logger.error("Alerts returned were in an unexpected format!")
            raise PluginException(PluginException.Preset.INVALID_JSON, data=response.text)

        return insightconnect_plugin_runtime.helper.clean(matching_alerts)

    def isolate_machine(self, id, isolation_type, comment):
        self.check_and_refresh_api_token()

        endpoint_url = f"https://api.securitycenter.windows.com/api/machines/{id}/isolate"
        body = {
            "Comment": comment,
            "IsolationType": isolation_type
        }

        self.logger.info(f"Isolating machine with: {endpoint_url}")
        response = self.session.post(endpoint_url, json=body)

        try:
            response.raise_for_status()
        except Exception as e:
            # TODO: Check to see if action is pending. It will throw a 400 error if it is.
            # It's a pain however, as we'll have to search through all the current actions to find this one
            raise ConnectionTestException(cause=f"Connection error occurred while connecting to: {endpoint_url}. Error "
                                                f"was: {e}",
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Isolate permissions "
                                                     "in the Azure portal.",
                                          data=response.text
                                          )
        return response.json()

    def unisolate_machine(self, id, comment):
        self.check_and_refresh_api_token()
        endpoint_url = f"https://api.securitycenter.windows.com/api/machines/{id}/unisolate"
        body = {
            "Comment": comment
        }

        self.logger.info(f"Isolating machine with: {endpoint_url}")
        response = self.session.post(endpoint_url, json=body)

        try:
            response.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(cause=f"Connection error occurred while connecting to: {endpoint_url}. Error "
                                                f"was: {e}",
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Isolate permissions "
                                                     "in the Azure portal.",
                                          data=response.text
                                          )
        return response.json()

    def stop_and_quarantine_file(self, machine_id, sha1_id, comment):
        self.check_and_refresh_api_token()
        endpoint_url = f"https://api.securitycenter.windows.com/api/machines/{machine_id}/StopAndQuarantineFile"
        body = {
            "Comment": comment,
            "Sha1": sha1_id
        }

        self.logger.info(f"Stop and quarantine file with: {endpoint_url}\n"
                         f"SHA1_ID: {sha1_id}\n"
                         f"Comment: {comment}")
        response = self.session.post(endpoint_url, json=body)

        try:
            response.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(cause=f"Connection error occurred while connecting to: {endpoint_url}. Error "
                                                f"was: {e}",
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Isolate permissions "
                                                     "in the Azure portal.",
                                          data=response.text
                                          )
        return response.json()

    def run_antivirus_scan(self, machine_id, scan_type, comment):
        self.check_and_refresh_api_token()
        endpoint_url = f"https://api.securitycenter.windows.com/api/machines/{machine_id}/runAntiVirusScan"

        body = {
            "Comment": comment,
            "ScanType": scan_type
        }

        self.logger.info(f"Run Antivirus Scan with: {endpoint_url}\n"
                         f"Scan Type: {scan_type}\n"
                         f"Comment: {comment}")
        response = self.session.post(endpoint_url, json=body)

        try:
            response.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(cause=f"Connection error occurred while connecting to: {endpoint_url}. Error "
                                                f"was: {e}",
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Scan permissions "
                                                     "in the Azure portal.",
                                          data=response.text
                                          )
        return response.json()

    def get_machine_action(self, action_id):
        self.check_and_refresh_api_token()
        endpoint_url = f"https://api.securitycenter.windows.com/api/machineactions/{action_id}"

        self.logger.info(f"Get machine action with: {endpoint_url}")
        response = self.session.post(endpoint_url)

        try:
            response.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(cause=f"Connection error occurred while connecting to: {endpoint_url}. Error "
                                                f"was: {e}",
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Read.All permissions "
                                                     "in the Azure portal.",
                                          data=response.text
                                          )
        return response.json()

    def get_files_from_id(self, alert_id):
        self.check_and_refresh_api_token()
        endpoint = f"https://api.securitycenter.windows.com/api/alerts/{alert_id}/files"

        self.logger.info(f"Getting files with: {endpoint}")
        response = self.session.get(endpoint)

        try:
            response.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(cause=f"Connection error occurred while connecting to: {endpoint}. Error "
                                                f"was: {e}",
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Read.All permissions "
                                                     "in the Azure portal.",
                                          data=response.text
                                          )
        return response.json()

    def get_machines_from_alert_id(self, alert_id):
        self.check_and_refresh_api_token()
        endpoint = f"https://api.securitycenter.windows.com/api/alerts/{alert_id}/machines"

        self.logger.info(f"Getting files with: {endpoint}")
        response = self.session.get(endpoint)

        try:
            response.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(cause=f"Connection error occurred while connecting to: {endpoint}. Error "
                                                f"was: {e}",
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Read.All permissions "
                                                     "in the Azure portal.",
                                          data=response.text
                                          )
        return response.json()

    def get_machine_information(self, machine_id):
        self.check_and_refresh_api_token()
        endpoint = f"https://api.securitycenter.windows.com/api/machines/{machine_id}"

        self.logger.info(f"Getting files with: {endpoint}")
        response = self.session.get(endpoint)

        try:
            response.raise_for_status()
        except Exception as e:
            raise ConnectionTestException(cause=f"Connection error occurred while connecting to: {endpoint}. Error "
                                                f"was: {e}",
                                          assistance="Check connection settings for proper resource URL and host "
                                                     "server. Verify application has Machine.Read.All permissions "
                                                     "in the Azure portal.",
                                          data=response.text
                                          )
        return response.json()



    def test(self):
        self.check_and_refresh_api_token()
        endpoint = "https://api.securitycenter.windows.com/api/alerts?$top=1"
        response = self.session.get(endpoint)
        try:
            response.raise_for_status()
        except Exception:
            raise ConnectionTestException(cause=f"Error connecting to {endpoint}",
                                          data=response.text)
        return response.json()
