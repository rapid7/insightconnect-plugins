from typing import Tuple
import komand
import requests
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
            output=SearchRulesOutput(),
        )

    def search_rule_by_cve(self, cve: str) -> Tuple[set, set, set]:
        """
        Search IPS rules for one CVE
        """

        matched_cves = set()
        missed_cves = set()
        ips_rules = set()

        # Prepare Search Criteria
        data = {
            "maxItems": 100,
            "searchCriteria": [{"fieldName": "CVE", "stringWildcards": True, "stringValue": f"%{cve}%"}],
        }

        # Prepare request
        url = f"{self.connection.dsm_url}/api/intrusionpreventionrules/search"

        # Search for IPS rules
        response = requests.post(
            url, data=json.dumps(data), verify=self.connection.dsm_verify_ssl, headers=self.connection.headers
        )

        # Check response errors
        checkResponse(response)

        # Try to convert the response data to JSON
        response_data = tryJSON(response)

        # Check if matching IPS rules were found
        if response_data["intrusionPreventionRules"]:
            for rule in response_data["intrusionPreventionRules"]:
                self.logger.info(f"{cve} -> {rule['ID']}: {rule['name']}")
                ips_rules.add(rule["ID"])
                matched_cves.add(cve)
        else:
            self.logger.info(f"{cve}: No rules found!")
            missed_cves.add(cve)

        return ips_rules, matched_cves, missed_cves

    def collect_all_ips_rules(self) -> list:
        """
        Receive all IPS rules from Deep Security
        """

        ips_rules = []
        ips_id = 0
        step = 5000  # <= 5000

        while True:
            # Prepare Search Criteria
            data = {
                "maxItems": step,
                "sortByObjectID": True,
                "searchCriteria": [{"idTest": "greater-than", "idValue": ips_id}],
            }

            # Send Request
            url = f"{self.connection.dsm_url}/api/intrusionpreventionrules/search"
            response = requests.post(
                url, data=json.dumps(data), verify=self.connection.dsm_verify_ssl, headers=self.connection.headers
            )

            # Check response errors
            checkResponse(response)

            # Convert to JSON
            response_data = tryJSON(response)

            # Check if there are results
            if response_data["intrusionPreventionRules"]:
                ips_id = response_data["intrusionPreventionRules"][-1]["ID"]
            else:
                break

            ips_rules.extend(response_data["intrusionPreventionRules"])

        self.logger.info(f"Received {len(ips_rules)} IPS rules!")
        return ips_rules

    def match_rules_and_cve(self, all_ips_rules: list, cves: list) -> Tuple[list, set, set]:
        """
        Look for IPS rules that match the given CVEs
        """

        matched = set()
        missed = set()
        ips_rules = []

        for cve in cves:
            for rule in all_ips_rules:
                if "CVE" in rule.keys():
                    if cve in rule["CVE"]:
                        self.logger.info(f"{cve}: {rule['name']}")
                        matched.add(cve)
                        ips_rules.append(rule["ID"])

            if cve not in matched:
                missed.add(cve)

        self.logger.info(f"{len(matched)} matched!")
        self.logger.info(f"{len(missed)} missed!")

        return ips_rules, matched, missed

    def run(self, params={}):
        """
        Searches for IPS rules by CVE number in Deep Security
        """

        # Get parameters
        self.vulnerabilities = params.get(Input.VULNERABILITIES)

        if len(self.vulnerabilities) == 1:
            ips_rules, matched_cves, missed_cves = self.search_rule_by_cve(self.vulnerabilities[0])
        else:
            all_ips_rules = self.collect_all_ips_rules()
            ips_rules, matched_cves, missed_cves = self.match_rules_and_cve(all_ips_rules, self.vulnerabilities)

        # Return matched rules
        return {
            Output.IPS_RULES: list(ips_rules),
            Output.MATCHED_CVES: list(matched_cves),
            Output.MISSED_CVES: list(missed_cves),
        }
