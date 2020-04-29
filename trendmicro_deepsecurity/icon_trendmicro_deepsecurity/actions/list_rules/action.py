import komand
from .schema import ListRulesInput, ListRulesOutput, Input, Output, Component
# Custom imports below

import json
from icon_trendmicro_deepsecurity.util.shared import tryJSON
from icon_trendmicro_deepsecurity.util.shared import checkResponse

class ListRules(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_rules',
                description=Component.DESCRIPTION,
                input=ListRulesInput(),
                output=ListRulesOutput())


    def run(self, params={}):
        """
        List IPS rules
        """

        # Get parameters
        self.computer_or_policy = params.get(Input.COMPUTER_OR_POLICY)
        self.id = params.get(Input.ID)

        self.logger.info(f"Getting rules from {self.computer_or_policy} {self.id}")

        # Prepare request
        # Check if the rules should be assigned to a computer or policy
        if self.computer_or_policy == "computer":
            url = f"{self.connection.dsm_url}/api/computers/{self.id}/intrusionprevention/assignments"
        else:
            url = f"{self.connection.dsm_url}/api/policies/{self.id}/intrusionprevention/assignments"

        # Set rules
        response = self.connection.session.get(url,
                                                verify=self.connection.dsm_verify_ssl)

        self.logger.info(f"url: {response.url}")
        self.logger.info(f"status: {response.status_code}")
        self.logger.info(f"reason: {response.reason}")

        # Try to convert the response data to JSON
        response_data = tryJSON(response)

        # Check response errors
        checkResponse(response)

        # Get a list of all assigned rules
        rules_assigned = response_data["assignedRuleIDs"]
        
        # Get a list of recommended rules
        rules_recommended = response_data["recommendedToAssignRuleIDs"]
        
        #Get a list of not recommended rules
        rules_not_recommended = response_data["recommendedToUnassignRuleIDs"]

        # Return assigned and failed rules
        return {Output.RULES_ASSIGNED: rules_assigned,
                Output.RULES_RECOMMENDED: rules_recommended,
                Output.RULES_NOT_RECOMMENDED: rules_not_recommended}
