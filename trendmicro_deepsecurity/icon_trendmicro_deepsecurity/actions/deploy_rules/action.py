import komand
from .schema import DeployRulesInput, DeployRulesOutput, Input, Output, Component
# Custom imports below

import requests
import json

from icon_trendmicro_deepsecurity.util.shared import tryJSON
from icon_trendmicro_deepsecurity.util.shared import checkResponse

class DeployRules(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="deploy_rules",
                description=Component.DESCRIPTION,
                input=DeployRulesInput(),
                output=DeployRulesOutput())

    def run(self, params={}):
        """
        Set IPS rules in Deep Security
        """

        # Get parameters
        self.computer_or_policy = params.get(Input.COMPUTER_OR_POLICY)
        self.id = params.get(Input.ID)
        self.rules = params.get(Input.RULES)

        self.logger.info("Setting rules: ")
        self.logger.info(self.rules)

        
        # Prepare request
        # Check if the rules should be assigned to a computer or policy
        if self.computer_or_policy == "computer":
            url = f"{self.connection.dsm_url}/api/computers/{self.id}/intrusionprevention/assignments"
        else:
            url = f"{self.connection.dsm_url}/api/policies/{self.id}/intrusionprevention/assignments"
        
        data = { "ruleIDs": self.rules }

        # Set rules
        response = self.connection.session.post(url,
                                                data=json.dumps(data),
                                                verify=self.connection.dsm_verify_ssl)

        self.logger.info(f"status: {response.status_code}")
        self.logger.info(f"reason: {response.reason}")

        # Try to convert the response data to JSON
        response_data = tryJSON(response)

        # Check response errors
        checkResponse(response)

        # Get a list of all rules assigned to the asset or policy
        rules_assigned = response_data["assignedRuleIDs"]
        rules_not_assigned = []

        # Check if the new rules were successfully assigned
        for rule in self.rules:
            if rule not in rules_assigned:
                rules_not_assigned.append(rule)

        # Return assigned and failed rules
        return {Output.RULES_ASSIGNED: rules_assigned,
                Output.RULES_NOT_ASSIGNED: rules_not_assigned}
