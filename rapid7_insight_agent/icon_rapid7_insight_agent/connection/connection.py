import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from icon_rapid7_insight_agent.util.region_map import region_map
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
        self.api_key = params.get(Input.API_KEY).get("secretKey")
        self.org_key = params.get(Input.ORG_ID).get("secretKey")
        region_string = params.get(Input.REGION)
        region_code = region_map.get(region_string)

        if region_code:
            self.endpoint = f"https://{region_code}.api.insight.rapid7.com/graphql"
        else:
            # It's an enum, hopefully this never happens.
            raise PluginException(cause="Region not found.",
                                  assistance="Region code was not found for selected region. Please contact support.")

        self.logger.info("Setup Complete")
        self.session = requests.Session()
        self.session.headers = self.get_headers()
        self.logger.info("Setup complete.")

    def get_headers(self):
        """
        This build and returns headers for the request session

        :return: dict
        """
        return {
            "X-Api-key": self.api_key,
            "Accept-Version": "kratos",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br"
        }

    def post_payload(self, payload):
        """
        This will post a given payload to the API using the connection session

        :param payload: dict
        :return: dict
        """
        result = self.session.post(self.endpoint, json=payload)

        try:
            result.raise_for_status()
        except:
            raise PluginException(cause="Error connecting to the Insight Agent API.",
                                  assistance="Please check your Org ID, and API key.\n",
                                  data=result.text)

        results_object = result.json()

        if results_object.get("errors"):
            raise PluginException(cause="Insight Agent API returned errors",
                                  assistance=results_object.get("errors"))

        return results_object

    def test(self):
        """
        connection test

        :return: dict
        """

        # Return the first org to verify the connection works
        graph_ql_payload = "{ organizations(first: 1) { edges { node { id } } totalCount } }"
        result = self.session.post(self.endpoint, data=graph_ql_payload)

        try:
            result.raise_for_status()
        except:
            raise ConnectionTestException(cause="Connection Test Failed",
                                          assistance="Please check your X API Key and Organization Key",
                                          data=result.text)
        return {}
