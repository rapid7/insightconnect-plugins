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

    def get_headers(self):
        return {
            "X-Api-key": self.api_key,
            "Accept-Version": "kratos",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br"
        }

    def test(self):
        # Return the first org to verify the connection works
        graph_ql_payload = "{ organizations(first: 1) { edges { node { id } } totalCount } }"

        headers = self.get_headers()
        result = requests.post(self.endpoint, headers=headers, data=graph_ql_payload)

        try:
            result.raise_for_status()
        except:
            raise ConnectionTestException(cause="Connection Test Failed",
                                          assistance="Please check your X API Key and Organization Key",
                                          data=result.text)

        return {}
