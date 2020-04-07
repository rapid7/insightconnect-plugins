import komand
from .schema import ConnectionSchema, Input
# Custom imports below

import requests
from icon_trendmicro_deepsecurity.util.shared import tryJSON
from icon_trendmicro_deepsecurity.util.shared import checkResponse


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        """
        Get all connection parameters
        """
        self.dsm_url = params.get(Input.DSM_URL)
        self.dsm_api_key = params.get(Input.DSM_API_KEY).get("secretKey")
        self.dsm_verify_ssl = params.get(Input.DSM_VERIFY_SSL)

        self.session = requests.session()
        self.session.headers.update({"Content-type": "application/json",
                                     "api-secret-key": self.dsm_api_key,
                                     "api-version": "v1"})

    def test(self):
        """
        Test connection to the Deep Security Manager
        """

        # Prepare request
        url = f"{self.dsm_url}/api/policies"

        # Get list of policies
        response = self.session.get(url, verify=self.dsm_verify_ssl)

        # Try to convert the response data to JSON
        response_data = tryJSON(response)

        # Check response errors
        checkResponse(response)

        self.logger.info("Found " + str(len(response_data["policies"])) + " policies!")
        for policy in response_data["policies"]:
            self.logger.info(policy["name"])

        return {"data": response.ok}
