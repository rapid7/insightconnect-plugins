import insightconnect_plugin_runtime

from .schema import ConnectionSchema, Input

# Custom imports below
from komand_salesforce.util.api import SalesforceAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from komand_salesforce.util.exceptions import ApiException
from komand_salesforce.tasks.monitor_users.task import MonitorUsers
from datetime import datetime, timedelta, timezone
from requests.exceptions import ConnectionError as con_err


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")

        client_id = params.get(Input.CLIENTID, "").strip()
        client_secret = params.get(Input.CLIENTSECRET, {}).get("secretKey")
        oauth_url = params.get(Input.LOGINURL, "").strip()
        username = params.get(Input.SALESFORCEACCOUNTUSERNAMEANDPASSWORD, {}).get("username")
        password = params.get(Input.SALESFORCEACCOUNTUSERNAMEANDPASSWORD, {}).get("password")
        security_token = params.get(Input.SECURITYTOKEN).get("secretKey")

        self.api = SalesforceAPI(client_id, client_secret, oauth_url, username, password, security_token, self.logger)

    def test(self):
        try:
            self.api.simple_search("test")
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)

    def test_task(self):
        now = datetime.now(timezone.utc)
        start_time = (now - timedelta(minutes=5)).isoformat()
        end_time = now.isoformat()

        endpoint_mapping = {
            "Get Updated Users": [
                self.api.query,
                MonitorUsers.UPDATED_USERS_QUERY.format(start_timestamp=start_time, end_timestamp=end_time),
            ],
            "Get Users": [self.api.query, MonitorUsers.USERS_QUERY],
            "Get User Login History": [
                self.api.query,
                MonitorUsers.USER_LOGIN_QUERY.format(start_timestamp=start_time, end_timestamp=end_time),
            ],
        }
        self.logger.info("Running a connection test to Salesforce")
        return_message = "The connection test to Salesforce was successful \n"
        error_message = ""

        # Validate credentials across all task endpoints
        for endpoint, values in endpoint_mapping.items():
            try:
                self.logger.info(f"Running test for {endpoint}")
                return_message += f"Running test for {endpoint} \n"
                method_execute, method_params = values[0], values[1]
                _ = method_execute(method_params)
                return_message += f"{endpoint} has passed \n"
            except ApiException as error:
                self.logger.info(f"API Exception has been hit. cause = {error.cause}, assistance = {error.assistance}")
                error_message += f"An error occurred in the following test: {endpoint}. \nThis can be fixed by: {error.assistance} \n"
            except con_err as error:
                self.logger.error(error)
                error_message += f"The URL provided in the connection for the {endpoint} test is unreachable. Please ensure you are providing a valid URL when trying to connect."
        if not error_message:
            self.logger.info(return_message)
            return {"success": True}, return_message
        else:
            raise ConnectionTestException(
                cause=f"The connection test to Salesforce failed due to: \n {error_message} ",
                assistance="The connection test to Salesforce failed. Please ensure all fields are set and have the correct values before attempting again.",
                data=error_message,
            )
