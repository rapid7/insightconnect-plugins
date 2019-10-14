# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "This action is used to fetch a risk list of the IP addresses that match a specified filtration rule"


class Input:
    LIST = "list"
    

class Output:
    RISK_LIST = "risk_list"
    

class DownloadIPAddressesRiskListInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "list": {
      "type": "string",
      "title": "List",
      "description": "The risk list to retrieve",
      "enum": [
        "current_cc_server",
        "cyber_exploit_signal_medium",
        "historical_bad_ssl_association",
        "historical_botnet_traffic",
        "historical_cc_server",
        "historical_honeypot_sighting",
        "historical_multicategory_blacklist",
        "historical_open_proxies",
        "historical_positive_malware_verdict",
        "historical_spam_source",
        "historical_sshdictionary_attacker",
        "historical_threat_researcher",
        "historically_linked_to_apt",
        "historically_linked_to_cyber_attack",
        "historically_linked_to_intrusion_method",
        "honeypot_host",
        "inside_possible_bogus_bgp_route",
        "large",
        "malicious_packet_source",
        "malware_delivery",
        "nameserver_for_cc_server",
        "phishing_host",
        "recent_botnet_traffic",
        "recent_cc_server",
        "recent_honeypot_sighting",
        "recent_host_of_many_ddns_names",
        "recent_multicategory_blacklist",
        "recent_open_proxies",
        "recent_positive_malware_verdict",
        "recent_spam_source",
        "recent_sshdictionary_attacker",
        "recent_threat_researcher",
        "recently_linked_to_apt",
        "recently_linked_to_cyber_attack",
        "recently_linked_to_intrusion_method",
        "resolution_of_fast_flux_dns_name",
        "tor_node",
        "unusual_ip",
        "vulnerable_host"
      ],
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DownloadIPAddressesRiskListOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "risk_list": {
      "type": "object",
      "title": "Risk List",
      "description": "Risk List",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
