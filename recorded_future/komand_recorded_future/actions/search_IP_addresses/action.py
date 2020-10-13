import komand
import json
from .schema import SearchIPAddressesInput, SearchIPAddressesOutput, Input
from komand.exceptions import PluginException


class SearchIPAddresses(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_IP_addresses",
            description="This action is used to query for data related to a specified IP range",
            input=SearchIPAddressesInput(),
            output=SearchIPAddressesOutput(),
        )

    def run(self, params={}):
        params["fields"] = ["analystNotes", "counts", "entity", "intelCard", "location", "metrics", "relatedEntities",
                            "risk", "riskyCIDRIPs", "sightings", "threatLists", "timestamps"]
        riskRuleMap = {
            "Threat Actor Used Infrastructure": "actorInfrastructure",
            "Historically Reported by Insikt Group": "analystNote",
            "Inside Possible Bogus BGP Route": "bogusBgp",
            "Historical Botnet Traffic": "botnet",
            "Nameserver for C&C Server": "cncNameserver",
            "Historical C&C Server": "cncServer",
            "Cyber Exploit Signal - Critical": "cyberSignalCritical",
            "Cyber Exploit Signal - Important": "cyberSignalHigh",
            "Cyber Exploit Signal - Medium": "cyberSignalMedium",
            "Recent Host of Many DDNS Names": "ddnsHost",
            "Historically Reported as a Defanged IP": "defanged",
            "Historically Reported by DHS AIS": "dhsAis",
            "Resolution of Fast Flux DNS Name": "fastFluxResolution",
            "Historically Reported in Threat List": "historicalThreatListMembership",
            "Historical Honeypot Sighting": "honeypot",
            "Honeypot Host": "honeypotHost",
            "Recently Active C&C Server": "intermediateActiveCnc",
            "Recent C&C Server": "intermediateCncServer",
            "Historically Linked to Intrusion Method": "linkedIntrusion",
            "Historically Linked to APT": "linkedToAPT",
            "Historically Linked to Cyber Attack": "linkedToCyberAttack",
            "Malicious Packet Source": "maliciousPacketSource",
            "Malware Delivery": "malwareDelivery",
            "Historical Multicategory Blacklist": "multiBlacklist",
            "Historical Open Proxies": "openProxies",
            "Phishing Host": "phishingHost",
            "Historical Positive Malware Verdict": "positiveMalwareVerdict",
            "Recorded Future Predictive Risk Model": "predictionModelVerdict",
            "Actively Communicating C&C Server": "recentActiveCnc",
            "Recently Reported by Insikt Group": "recentAnalystNote",
            "Recent Spam Source": "recentSpam",
            "Recent SSH/Dictionary Attacker": "recentSshDictAttacker",
            "Recent Bad SSL Association": "recentSsl",
            "Recent Threat Researcher": "recentThreatResearcher",
            "Recently Defaced Site": "recentlyDefaced",
            "Historically Referenced by Insikt Group": "relatedNote",
            "Trending in Recorded Future Analyst Community": "rfTrending",
            "Historical Spam Source": "spam",
            "Historical SSH/Dictionary Attacker": "sshDictAttacker",
            "Historical Bad SSL Association": "ssl",
            "Historical Threat Researcher": "threatResearcher",
            "Tor Node": "tor",
            "Unusual IP": "unusualIP",
            "Vulnerable Host": "vulnerableHost"
        }
        risk_rule = riskRuleMap.get(params.get(Input.RISKRULE))
        if risk_rule:
            params[Input.RISKRULE] = risk_rule
        else:
            params[Input.RISKRULE] = None
        try:
            results = self.connection.client.search_ips(**params)
            return json.loads(results._req_response._content.decode("utf-8"))
        except Exception as e:
            self.logger.error("Error: " + str(e))
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)
