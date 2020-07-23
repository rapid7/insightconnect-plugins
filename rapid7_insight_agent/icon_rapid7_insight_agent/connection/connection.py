import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from icon_rapid7_insight_agent.util.graphql_api.api_connection import ApiConnection

import requests


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        """
        Entry point for connection to the API

        :param params: dict
        :return: none
        """
        self.logger.info("Connect: Connecting...")

        # Setup region
        api_key = params.get(Input.API_KEY).get("secretKey")
        org_key = params.get(Input.ORG_ID).get("secretKey")
        region_string = params.get(Input.REGION)

        self.api = ApiConnection(api_key, org_key, region_string, self.logger)

        self.logger.info("Setup Complete")

    def test(self):
        """
        connection test

        :return: dict
        """
        try:
            success = self.api.run_connection_test()
        except Exception as e:
            raise ConnectionTestException(cause="Connection Test Failed.\n",
                                          assistance="Check that your organization ID and API key are correct.\n") from e
        return {"success": success}
