import komand
from .schema import SearchRulesInput, SearchRulesOutput, Input, Output, Component
# Custom imports below

import json
from icon_trendmicro_deepsecurity.util.shared import tryJSON
from icon_trendmicro_deepsecurity.util.shared import checkResponse


class SearchRules(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name="search_rules",
                description=Component.DESCRIPTION,
                input=SearchRulesInput(),
                output=SearchRulesOutput())

    def run(self, params={}):
        '''
        Searches for IPS rules by CVE number in Deep Security
        '''

        # Get parameters
        self.vulnerabilities = params.get(Input.VULNERABILITIES)

        matched_cves = set()
        missed_cves = set()
        ips_rules = set()

        for cve in self.vulnerabilities:

            # Prepare request
            url = f"{self.connection.dsm_url}/api/intrusionpreventionrules/search"

            data = {"maxItems": 100,
                    "searchCriteria": [{"fieldName": "CVE",
                                        "stringWildcards": True,
                                        "stringValue": f"%{cve}%"}]}

            # Search for IPS rules
            response = self.connection.session.post(url,
                                                    data=json.dumps(data),
                                                    verify=self.connection.dsm_verify_ssl)

            self.logger.info(f"CVE: {cve}")
            self.logger.info(f"url: {response.url}")
            self.logger.info(f"status: {response.status_code}")
            self.logger.info(f"reason: {response.reason}")

            # Try to convert the response data to JSON
            response_data = tryJSON(response)

            # Check response errors
            checkResponse(response)

            # Check if matching IPS rules were found
            if response_data["intrusionPreventionRules"]:
                hits = len(response_data["intrusionPreventionRules"])
                self.logger.info(f"{cve}: Found {hits} rules!")
                for rule in response_data["intrusionPreventionRules"]:
                    self.logger.info(f"{rule['ID']}: {rule['name']}")
                    ips_rules.add(rule["ID"])
                    matched_cves.add(cve)
            else:
                self.logger.info(f"{cve}: No rules found!")
                missed_cves.add(cve)

        self.logger.info("Found rules for the following CVEs: " + ", ".join(matched_cves))

        return {Output.IPS_RULES: list(ips_rules),
                Output.MATCHED_CVES: list(matched_cves),
                Output.MISSED_CVES: list(missed_cves)}
