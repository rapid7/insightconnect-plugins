import komand
from .schema import GetRuleDetailsInput, GetRuleDetailsOutput, Input, Output, Component
# Custom imports below

from icon_trendmicro_deepsecurity.util.shared import tryJSON
from icon_trendmicro_deepsecurity.util.shared import checkResponse


class GetRuleDetails(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_rule_details',
                description=Component.DESCRIPTION,
                input=GetRuleDetailsInput(),
                output=GetRuleDetailsOutput())

    def run(self, params={}):
        """
        Get IPS rule details
        """

        # Get parameters
        self.id = params.get(Input.ID)

        self.logger.info(f"Getting details for rule: {self.id}")

        # Prepare request
        url = f"{self.connection.dsm_url}/api/intrusionpreventionrules/{self.id}"

        # Send request
        response = self.connection.session.get(url,
                                               verify=self.connection.dsm_verify_ssl)

        self.logger.info(f"url: {response.url}")
        self.logger.info(f"status: {response.status_code}")
        self.logger.info(f"reason: {response.reason}")

        # Check response errors
        checkResponse(response)

        # Try to convert the response data to JSON
        response_data = tryJSON(response)

        cves = []

        name = response_data["name"]
        description = response_data["description"]
        severity = response_data["severity"]
        rule_type = response_data["type"]
        cvss_score = response_data["CVSSScore"]
        if "CVE" in response_data.keys():
            cves = response_data["CVE"]

        # Return rule details
        return {Output.NAME: name,
                Output.DESCRIPTION: description,
                Output.SEVERITY: severity,
                Output.TYPE: rule_type,
                Output.CVSS_SCORE: cvss_score,
                Output.CVES: cves,
                Output.RESPONSE_JSON: response_data}
