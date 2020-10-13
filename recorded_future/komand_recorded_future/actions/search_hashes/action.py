import komand
import json
from .schema import SearchHashesInput, SearchHashesOutput, Input
from komand.exceptions import PluginException


class SearchHashes(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_hashes",
            description="This action is used to search for data related to hashes of a specified type",
            input=SearchHashesInput(),
            output=SearchHashesOutput(),
        )

    def run(self, params={}):
        params["fields"] = ["analystNotes", "counts", "entity", "hashAlgorithm", "intelCard", "metrics",
                            "relatedEntities", "risk", "sightings", "threatLists", "timestamps"]
        riskRuleMap = {
            "Reported by Insikt Group": "analystNote",
            "Historically Reported in Threat List": "historicalThreatListMembership",
            "Linked to Cyber Attack": "linkedToCyberAttack",
            "Linked to Malware": "linkedToMalware",
            "Linked to Attack Vector": "linkedToVector",
            "Linked to Vulnerability": "linkedToVuln",
            "Malware SSL Certificate Fingerprint": "malwareSsl",
            "Observed in Underground Virus Testing Sites": "observedMalwareTesting",
            "Positive Malware Verdict": "positiveMalwareVerdict",
            "Recently Active Targeting Vulnerabilities in the Wild": "recentActiveMalware",
            "Referenced by Insikt Group": "relatedNote",
            "Trending in Recorded Future Analyst Community": "rfTrending",
            "Threat Researcher": "threatResearcher"
        }
        risk_rule = riskRuleMap.get(params.get(Input.RISKRULE))
        if risk_rule:
            params[Input.RISKRULE] = risk_rule
        else:
            params[Input.RISKRULE] = None
        try:
            results = self.connection.client.search_hashes(**params)
            return json.loads(results._req_response._content.decode("utf-8"))
        except Exception as e:
            self.logger.error("Error: " + str(e))
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
