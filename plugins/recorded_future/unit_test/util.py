import json
import logging
import os
import sys

import insightconnect_plugin_runtime

sys.path.append(os.path.abspath("../"))

from komand_recorded_future.connection import Connection
from komand_recorded_future.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params=None):
        if not params:
            params = {Input.API_KEY: {"secretKey": "***REMOVED***"}}
        action.connection = Connection()
        action.connection.meta = "{}"
        action.connection.logger = logging.getLogger("connection logger")
        action.connection.connect(params)
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename, "r", encoding="utf-8") as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename):
        return json.loads(Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)))

    @staticmethod
    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                if filename:
                    self.text = Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{filename}.json.resp")
                    )
                else:
                    self.text = ""

            def json(self):
                return json.loads(self.text)

        if kwargs.get("headers", {}).get("X-RFToken") == "bad_api_key":
            return MockResponse(401)
        if kwargs.get("headers", {}).get("X-RFToken") == "unauthorized":
            return MockResponse(403)
        if kwargs.get("headers", {}).get("X-RFToken") == "unknown":
            return MockResponse(407)
        if kwargs.get("headers", {}).get("X-RFToken") == "server_error":
            return MockResponse(700)
        if kwargs.get("headers", {}).get("X-RFToken") == "invalid_json":
            return MockResponse(200, "invalid_json")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/ip/151.10.1.8":
            return MockResponse(200, "lookup_ip_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/ip/151.14.112.855":
            return MockResponse(404, "lookup_ip_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/ip/151.1014.112.855":
            return MockResponse(404, "lookup_ip_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/domain/coffee-break.pl":
            return MockResponse(200, "lookup_domain_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/domain/valid_not_found_domain.com":
            return MockResponse(404, "lookup_domain_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/domain/not_valid_not_found_domain.com":
            return MockResponse(404, "lookup_domain_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/url/https%3A%2F%2Fbbc.com":
            return MockResponse(200, "lookup_url_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/url/https%3A%2F%2Fsome_url_not_found":
            return MockResponse(404, "lookup_url_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/url/https%3A%2F%2Fsome_invalid_url_not_found":
            return MockResponse(404, "lookup_url_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/hash/44d88612fea8a8f36de82e1278abb02f":
            return MockResponse(200, "lookup_hash_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/hash/5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8":
            return MockResponse(404, "lookup_hash_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/hash/44d88612fea8a8f36devxcvfxcd82e1278abb02f":
            return MockResponse(404, "lookup_hash_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/alert/fhS1El":
            return MockResponse(200, "lookup_alert_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/alert/fhS2El":
            return MockResponse(404, "lookup_alert_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/alert/fhSghfn5431El":
            return MockResponse(404, "lookup_alert_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/vulnerability/CVE-2009-0001":
            return MockResponse(200, "lookup_vulnerability_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/vulnerability/CVE-2009-0002":
            return MockResponse(404, "lookup_vulnerability_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/vulnerability/CVE-209-001":
            return MockResponse(404, "lookup_vulnerability_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/malware/ShciZX":
            return MockResponse(200, "lookup_malware_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/malware/ShciYX":
            return MockResponse(404, "lookup_malware_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/malware/Shcfg345iZX":
            return MockResponse(404, "lookup_malware_not_found")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/domain/risklist":
            return MockResponse(200, "domain_risk_list")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/domain/riskrules":
            return MockResponse(200, "list_domain_risk_rules")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/domain/search":
            return MockResponse(200, "search_domains")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/hash/risklist":
            return MockResponse(200, "hash_risk_list")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/hash/riskrules":
            return MockResponse(200, "list_hash_risk_rules")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/hash/search":
            return MockResponse(200, "search_hashes")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/ip/risklist":
            return MockResponse(200, "ip_risk_list")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/ip/riskrules":
            return MockResponse(200, "list_ip_addresses_risk_rules")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/ip/search":
            return MockResponse(200, "search_ip_addresses")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/url/risklist":
            return MockResponse(200, "url_risk_list")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/url/riskrules":
            return MockResponse(200, "list_url_risk_rules")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/vulnerability/risklist":
            return MockResponse(200, "vulnerability_risk_list")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/vulnerability/riskrules":
            return MockResponse(200, "list_vulnerability_risk_rules")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/vulnerability/search":
            return MockResponse(200, "search_vulnerabilities")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/entitylist/search":
            return MockResponse(200, "search_entity_lists")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/malware/search":
            return MockResponse(200, "search_malware")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/url/search":
            return MockResponse(200, "search_urls")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/entitylist/report:Oe5eg5":
            return MockResponse(200, "lookup_entity_list")
        raise NotImplementedError("Not implemented", kwargs)
