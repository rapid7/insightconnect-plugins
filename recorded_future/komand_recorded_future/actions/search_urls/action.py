import komand
import json
from .schema import SearchUrlsInput, SearchUrlsOutput, Component, Input
# Custom imports below


class SearchUrls(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_urls',
                description=Component.DESCRIPTION,
                input=SearchUrlsInput(),
                output=SearchUrlsOutput())

    def run(self, params={}):
        riskRuleMap = {
            "Historically Reported by Insikt Group": "analystNote",
            "C&amp;C URL": "cncUrl",
            "Compromised URL": "compromisedUrl",
            "Historically Reported as a Defanged URL": "defangedURL",
            "Historically Reported by DHS AIS": "dhsAis",
            "Historically Reported Fraudulent Content": "fraudulentContent",
            "Historically Reported in Threat List": "historicalThreatListMembership",
            "Historically Detected Malicious Browser Exploits": "maliciousSiteDetected",
            "Historically Detected Malware Distribution": "malwareSiteDetected",
            "Historically Detected Cryptocurrency Mining Techniques": "miningSiteDetected",
            "Historically Detected Phishing Techniques": "phishingSiteDetected",
            "Active Phishing URL": "phishingUrl",
            "Positive Malware Verdict": "positiveMalwareVerdict",
            "Ransomware Distribution URL": "ransomwareDistribution",
            "Recently Reported by Insikt Group": "recentAnalystNote",
            "Recently Reported as a Defanged URL": "recentDefangedURL",
            "Recently Reported by DHS AIS": "recentDhsAis",
            "Recently Reported Fraudulent Content": "recentFraudulentContent",
            "Recently Detected Malicious Browser Exploits": "recentMaliciousSiteDetected",
            "Recently Detected Malware Distribution": "recentMalwareSiteDetected",
            "Recently Detected Cryptocurrency Mining Techniques": "recentMiningSiteDetected",
            "Recently Detected Phishing Techniques": "recentPhishingSiteDetected",
            "Recently Referenced by Insikt Group": "recentRelatedNote",
            "Recently Reported Spam or Unwanted Content": "recentSpamSiteDetected",
            "Recently Detected Suspicious Content": "recentSuspiciousSiteDetected",
            "Recently Active URL on Weaponized Domain": "recentWeaponizedURL",
            "Historically Referenced by Insikt Group": "relatedNote",
            "Historically Reported Spam or Unwanted Content": "spamSiteDetected",
            "Historically Detected Suspicious Content": "suspiciousSiteDetected"
        }
        risk_rule = riskRuleMap.get(params.get(Input.RISKRULE))
        if risk_rule:
            params["riskRule"] = risk_rule

        try:
            results = self.connection.client.search_urls(**params)
            return json.loads(results._req_response._content.decode("utf-8"))
        except Exception as e:
            self.logger.error("Error: " + str(e))
