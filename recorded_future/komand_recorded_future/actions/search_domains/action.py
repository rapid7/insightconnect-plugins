import komand
import json
from .schema import SearchDomainsInput, SearchDomainsOutput, Input
from komand.exceptions import PluginException


class SearchDomains(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_domains",
            description="This action is used to search for results related to a specific parent domain",
            input=SearchDomainsInput(),
            output=SearchDomainsOutput(),
        )

    def run(self, params={}):
        params["fields"] = ["analystNotes", "counts", "entity", "intelCard", "metrics", "relatedEntities", "risk",
                            "sightings", "threatLists", "timestamps"]
        riskRuleMap = {
            "Historically Reported by Insikt Group": "analystNote",
            "Newly Registered Certificate With Potential for Abuse - DNS Sandwich": "certTyposquatSandwich",
            "Newly Registered Certificate With Potential for Abuse - Typo or Homograph": "certTyposquatTypo",
            "C&C Nameserver": "cncNameserver",
            "C&C DNS Name": "cncSite",
            "C&C URL": "cncUrl",
            "Compromised URL": "compromisedUrl",
            "Historical COVID-19-Related Domain Lure": "covidLure",
            "Recently Resolved to Host of Many DDNS Names": "ddns",
            "Historically Reported as a Defanged DNS Name": "defanged",
            "Historically Reported by DHS AIS": "dhsAis",
            "Recent Fast Flux DNS Name": "fastFlux",
            "Historically Reported Fraudulent Content": "fraudulentContent",
            "Historically Reported in Threat List": "historicalThreatListMembership",
            "Historically Linked to Cyber Attack": "linkedToCyberAttack",
            "Historical Malware Analysis DNS Name": "malwareAnalysis",
            "Historically Detected Malware Operation": "malwareSiteDetected",
            "Historically Detected Cryptocurrency Mining Techniques": "miningSiteDetected",
            "Blacklisted DNS Name": "multiBlacklist",
            "Historical Phishing Lure": "phishingLure",
            "Historically Detected Phishing Techniques": "phishingSiteDetected",
            "Active Phishing URL": "phishingUrl",
            "Recorded Future Predictive Risk Model": "predictionModelVerdict",
            "Historical Punycode Domain": "punycode",
            "Ransomware Distribution URL": "ransomwareDistribution",
            "Ransomware Payment DNS Name": "ransomwarePayment",
            "Recently Reported by Insikt Group": "recentAnalystNote",
            "Recent COVID-19-Related Domain Lure - Malicious": "recentCovidLure",
            "Recent COVID-19-Related Domain Lure - Suspicious": "recentCovidSpam",
            "Recently Reported as a Defanged DNS Name": "recentDefanged",
            "Recently Reported by DHS AIS": "recentDhsAis",
            "Recently Reported Fraudulent Content": "recentFraudulentContent",
            "Recently Linked to Cyber Attack": "recentLinkedToCyberAttack",
            "Recent Malware Analysis DNS Name": "recentMalwareAnalysis",
            "Recently Detected Malware Operation": "recentMalwareSiteDetected",
            "Recently Detected Cryptocurrency Mining Techniques": "recentMiningSiteDetected",
            "Recent Phishing Lure: Malicious": "recentPhishingLureMalicious",
            "Recent Phishing Lure: Suspicious": "recentPhishingLureSuspicious",
            "Recently Detected Phishing Techniques": "recentPhishingSiteDetected",
            "Recent Punycode Domain": "recentPunycode",
            "Recently Referenced by Insikt Group": "recentRelatedNote",
            "Recently Reported Spam or Unwanted Content": "recentSpamSiteDetected",
            "URL Recently Linked to Suspicious Content": "recentSuspiciousContent",
            "Recent Threat Researcher": "recentThreatResearcher",
            "Recent Typosquat Similarity - DNS Sandwich": "recentTyposquatSandwich",
            "Recent Typosquat Similarity - Typo or Homograph": "recentTyposquatTypo",
            "Recently Active Weaponized Domain": "recentWeaponizedDomain",
            "Recently Defaced Site": "recentlyDefaced",
            "Historically Referenced by Insikt Group": "relatedNote",
            "Recently Resolved to Malicious IP": "resolvedMaliciousIp",
            "Recently Resolved to Suspicious IP": "resolvedSuspiciousIp",
            "Recently Resolved to Unusual IP": "resolvedUnusualIp",
            "Recently Resolved to Very Malicious IP": "resolvedVeryMaliciousIp",
            "Trending in Recorded Future Analyst Community": "rfTrending",
            "Historically Reported Spam or Unwanted Content": "spamSiteDetected",
            "URL Historically Linked to Suspicious Content": "suspiciousContent",
            "Historical Threat Researcher": "threatResearcher",
            "Historical Typosquat Similarity - DNS Sandwich": "typosquatSandwich",
            "Historical Typosquat Similarity - Typo or Homograph": "typosquatTypo",
            "Historically Active Weaponized Domain": "weaponizedDomain"
        }
        risk_rule = riskRuleMap.get(params.get(Input.RISKRULE))
        if risk_rule:
            params[Input.RISKRULE] = risk_rule
        else:
            params[Input.RISKRULE] = None
        try:
            results = self.connection.client.search_domains(**params)
            return json.loads(results._req_response._content.decode("utf-8"))
        except Exception as e:
            self.logger.error("Error: " + str(e))
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
