import komand
import requests
import xmltodict
from .schema import DownloadUrlRiskListInput, DownloadUrlRiskListOutput, Input, Output, Component
from komand.exceptions import PluginException
# Custom imports below


class DownloadUrlRiskList(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='download_url_risk_list',
            description=Component.DESCRIPTION,
            input=DownloadUrlRiskListInput(),
            output=DownloadUrlRiskListOutput())

    def run(self, params={}):
        try:
            riskListMap = {
                "Historically Reported by Insikt Group": "cncUrl",
                "Compromised URL": "compromisedUrl",
                "Historically Reported as a Defanged URL": "defangedURL",
                "Historically Reported by DHS AIS": "dhsAis",
                "Historically Reported Fraudulent Content": "fraudulentContent",
                "Historically Reported in Threat List": "historicalThreatListMembership",
                "Large": "large",
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
            risk_list = riskListMap.get(params.get(Input.LIST))
            query_params = {"format": "xml/stix/1.2", "gzip": "false"}
            if risk_list:
                query_params[Input.LIST] = risk_list

            query_headers = {"X-RFToken": self.connection.token}
            results = requests.get(
                "https://api.recordedfuture.com/v2/url/risklist",
                params=query_params,
                headers=query_headers,
            )
            return {
                Output.RISK_LIST: dict(xmltodict.parse(results.text))
            }
        except Exception as e:
            self.logger.error("Error: " + str(e))
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
