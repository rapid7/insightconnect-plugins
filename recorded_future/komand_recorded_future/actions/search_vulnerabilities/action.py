import komand
import json
from .schema import SearchVulnerabilitiesInput, SearchVulnerabilitiesOutput, Input
from komand.exceptions import PluginException


class SearchVulnerabilities(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_vulnerabilities",
            description="This action is used to search for data related to vulnerabilities",
            input=SearchVulnerabilitiesInput(),
            output=SearchVulnerabilitiesOutput(),
        )

    def run(self, params={}):
        params["fields"] = ["analystNotes", "commonNames", "counts", "cpe", "cvss", "cvssv3", "entity", "intelCard",
                            "metrics", "nvdDescription", "rawrisk", "relatedEntities", "relatedLinks", "risk",
                            "sightings", "threatLists", "timestamps"]
        riskRuleMap = {
            "Historically Reported by Insikt Group": "analystNote",
            "Web Reporting Prior to CVSS Score": "awaitingCvssScore",
            "Cyber Exploit Signal - Critical": "cyberSignalCritical",
            "Cyber Exploit Signal - Important": "cyberSignalHigh",
            "Cyber Exploit Signal - Medium": "cyberSignalMedium",
            "Historical Suspected Exploit/Tool Development in the Wild": "exploitDev",
            "Historical Observed Exploit/Tool Development in the Wild": "historicExploitDev",
            "Historically Exploited in the Wild by Malware": "historicMalwareActivity",
            "Linked to Historical Cyber Exploit": "linkedToCyberExploit",
            "Historically Linked to Exploit Kit": "linkedToExploitKit",
            "Historically Linked to Malware": "linkedToIntrusionMethod",
            "Historically Linked to Remote Access Trojan": "linkedToRAT",
            "Historically Linked to Ransomware": "linkedToRansomware",
            "Linked to Recent Cyber Exploit": "linkedToRecentCyberExploit",
            "Recently Linked to Exploit Kit": "linkedToRecentExploitKit",
            "Recently Linked to Malware": "linkedToRecentIntrusionMethod",
            "Recently Linked to Remote Access Trojan": "linkedToRecentRAT",
            "Recently Linked to Ransomware": "linkedToRecentRansomware",
            "Exploited in the Wild by Malware": "malwareActivity",
            "NIST Severity - Critical": "nistCritical",
            "Duplicate of Vulnerability in NVD": "nistDuplicate",
            "NIST Severity - High": "nistHigh",
            "NIST Severity - Low": "nistLow",
            "NIST Severity - Medium": "nistMedium",
            "Web Reporting Prior to NVD Disclosure": "noCvssScore",
            "Historical Unverified Proof of Concept Available": "pocUnverified",
            "Historical Verified Proof of Concept Available": "pocVerified",
            "Historical Verified Proof of Concept Available Using Remote Execution": "pocVerifiedRemote",
            "Recently Reported by Insikt Group": "recentAnalystNote",
            "Recent Suspected Exploit/Tool Development in the Wild": "recentExploitDev",
            "Exploited in the Wild by Recently Active Malware": "recentMalwareActivity",
            "Recent Unverified Proof of Concept Available": "recentPocUnverified",
            "Recent Verified Proof of Concept Available": "recentPocVerified",
            "Recent Verified Proof of Concept Available Using Remote Execution": "recentPocVerifiedRemote",
            "Recently Referenced by Insikt Group": "recentRelatedNote",
            "Recently Linked to Penetration Testing Tools": "recentScannerUptake",
            "Historically Referenced by Insikt Group": "relatedNote",
            "Historically Linked to Penetration Testing Tools": "scannerUptake"
        }
        risk_rule = riskRuleMap.get(params.get(Input.RISKRULE))
        if risk_rule:
            params[Input.RISKRULE] = risk_rule
        else:
            params[Input.RISKRULE] = None
        try:
            results = self.connection.client.search_vulnerabilities(**params)
            return json.loads(results._req_response._content.decode("utf-8"))
        except Exception as e:
            self.logger.error("Error: " + str(e))
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
