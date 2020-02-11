import komand
from .schema import DeployRulesInput, DeployRulesOutput, Input, Output, Component
# Custom imports below

import requests
import json

from ...util.shared import tryJSON
from ...util.shared import checkResponse

class DeployRules(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='deploy_rules',
                description=Component.DESCRIPTION,
                input=DeployRulesInput(),
                output=DeployRulesOutput())

    def run(self, params={}):
        """
        Set IPS rules in Deep Security
        """

        # Get parameters
        self.computer_or_policy=params.get("computer_or_policy")
        self.id=params.get("id")
        self.rules=params.get("rules")

        # Check if the rules should be assigned to a computer or policy
        if self.computer_or_policy == "computer":
            url = self.connection.dsm_url + "/api/computers/" + str(self.id) + "/intrusionprevention/assignments"
        else:
            url = self.connection.dsm_url + "/api/policies/" + str(self.id) + "/intrusionprevention/assignments"

        self.logger.info("Setting rules: ")
        self.logger.info(self.rules)

        # Prepare request
        data = { "ruleIDs": self.rules }

        post_header = {
                        "Content-type": "application/json",
                        "api-secret-key": self.connection.dsm_api_key,
                        "api-version": "v1"
                        }

        # Set rules
        response = requests.post(url,
                                data=json.dumps(data),
                                headers=post_header,
                                verify=True)
        response.close()

        self.logger.info('status: ' + str(response.status_code))
        self.logger.info('reason: ' + response.reason)

        # Try to convert the response data to JSON
        response_data=tryJSON(response)

        # Check response errors
        checkResponse(response)

        # Get a list of all rules assigned to the asset or policy
        rules_assigned=response_data['assignedRuleIDs']
        rules_not_assigned=[]

        # Check if the new rules were successfully assigned
        for rule in self.rules:
            if rule not in response_data['assignedRuleIDs']:
                rules_not_assigned.append(rule)

        # Return assigned and failed rules
        return {"rules_assigned": rules_assigned,
                'rules_not_assigned': rules_not_assigned}

