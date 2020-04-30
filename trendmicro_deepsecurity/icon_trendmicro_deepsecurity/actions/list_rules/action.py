import komand
from .schema import ListRulesInput, ListRulesOutput, Input, Output, Component
# Custom imports below

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
        self.scope = params.get(Input.SCOPE)
        self.id = params.get(Input.ID)

        ips_rules = set()
        covered_cves = set()
        hits = 0

        self.logger.info(f"Getting rules from {self.scope} {self.id}")

        # Prepare request
        # Check if the rules should be assigned to a computer or policy
        if self.scope == "computer":
            url = f"{self.connection.dsm_url}/api/computers/{self.id}/intrusionprevention/rules"
        else:
            url = f"{self.connection.dsm_url}/api/policies/{self.id}/intrusionprevention/rules"

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

        # Check if matching IPS rules were found
        if response_data["intrusionPreventionRules"]:
            for rule in response_data["intrusionPreventionRules"]:
                ips_rules.add(rule["ID"])
                if 'CVE' in rule.keys():
                    self.logger.info(f"{rule['ID']}:\t{rule['name']} - " + ", ".join(rule['CVE']))
                    covered_cves.update(rule['CVE'])
                else:
                    self.logger.info(f"{rule['ID']}:\t{rule['name']}")
        else:
            self.logger.info(f"No rules found!")

        hits = len(response_data["intrusionPreventionRules"])
        self.logger.info(f"Found {hits} rules covering the following CVEs: \n" + ", ".join(covered_cves))

        # Return assigned and failed rules
        return {Output.RULES_ASSIGNED: list(ips_rules),
                Output.COVERED_CVES: list(covered_cves),
                Output.RESPONSE_JSON: response_data}
