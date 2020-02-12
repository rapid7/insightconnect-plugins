import komand
from .schema import ConnectionSchema, Input
# Custom imports below

import requests
from requests.auth import HTTPBasicAuth

from icon_trendmicro_deepsecurity.util.shared import tryJSON
from icon_trendmicro_deepsecurity.util.shared import checkResponse


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        """
        Get all connection parameters
        """
        self.dsm_url = params.get("dsm_url")
        self.dsm_api_key = params.get('dsm_api_key').get("secretKey")

    def test(self):
        """
        Test connection to the Deep Security Manager
        """

        # Prepare request
        url = f'{self.dsm_url}/api/policies'
        
        post_header = {
                        "Content-type": "application/json",
                        "api-secret-key": self.dsm_api_key,
                        "api-version": "v1"
                        }

        # Get list of policies
        response = requests.get(url,
                                 headers=post_header,
                                 verify=True)                                
        response.close()

        # Try to convert the response data to JSON
        response_data=tryJSON(response)

        # Check response errors
        checkResponse(response)

        self.logger.info("Found " + str(len(response_data['policies'])) + " policies!")
        for policy in response_data['policies']:
          self.logger.info(policy['name'])

        return {'data': response.ok}
