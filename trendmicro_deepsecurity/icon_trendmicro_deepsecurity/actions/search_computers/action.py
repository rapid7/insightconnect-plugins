import komand
from .schema import SearchComputersInput, SearchComputersOutput, Input, Output, Component
# Custom imports below

import json
from komand.exceptions import PluginException
from icon_trendmicro_deepsecurity.util.shared import tryJSON
from icon_trendmicro_deepsecurity.util.shared import checkResponse


class SearchComputers(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_computers',
                description=Component.DESCRIPTION,
                input=SearchComputersInput(),
                output=SearchComputersOutput())

    def run(self, params={}):
        '''
        Searches for Computers in Deep Security
        '''

        # Get parameters
        self.information = params.get(Input.INFORMATION)
        self.max_items = params.get(Input.MAX_ITEMS)
        self.field_name = params.get(Input.FIELD_NAME)
        self.search_type = params.get(Input.SEARCH_TYPE)
        self.string_value = params.get(Input.STRING_VALUE)
        self.number_value = params.get(Input.NUMBER_VALUE)

        computer_ids = set()

        # Prepare request
        url = f"{self.connection.dsm_url}/api/computers/search?expand={self.information}"

        if self.field_name:
            if self.search_type == "string" and self.string_value:
                # Search for computers by string match
                data = {"maxItems": self.max_items,
                        "searchCriteria": [{"fieldName": self.field_name,
                                            "stringWildcards": True,
                                            "stringValue": self.string_value}]}
            elif self.search_type == "integer" and self.number_value:
                # Search for computers by number match
                data = {"maxItems": self.max_items,
                        "searchCriteria": [{"fieldName": self.field_name,
                                            "stringWildcards": True,
                                            "numericValue": self.number_value}]}
            else:
                raise PluginException(cause="Scan type and matching seach value expected but not found!",
                                      assistance="Please select a search type and pass the matching string/number value to search for.")
        else:
            # List all computers
            data = {"maxItems": self.max_items}

        # Send request
        response = self.connection.session.post(url,
                                                data=json.dumps(data),
                                                verify=self.connection.dsm_verify_ssl)

        self.logger.info(f"url: {response.url}")
        self.logger.info(f"status: {response.status_code}")
        self.logger.info(f"reason: {response.reason}")

        # Check response errors
        checkResponse(response)

        # Try to convert the response data to JSON
        response_data = tryJSON(response)

        # Extract computer IDs
        if response_data["computers"]:
            hits = len(response_data["computers"])
            self.logger.info(f"Found {hits} computer(s)!")
            for computer in response_data["computers"]:
                self.logger.info(f"{computer['ID']} - {computer['hostName']}")
                computer_ids.add(computer['ID'])
        else:
            self.logger.info(f"No computer found!")
    
        # Return matched rules
        return {Output.COMPUTER_IDS: list(computer_ids),
                Output.RESPONSE_JSON: response_data}
