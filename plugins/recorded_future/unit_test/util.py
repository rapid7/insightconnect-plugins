import json
import logging
import os
import sys
from unittest import mock
from unittest.mock import MagicMock

import insightconnect_plugin_runtime

sys.path.append(os.path.abspath("../"))

from komand_recorded_future.connection import Connection
from komand_recorded_future.connection.schema import Input

GZIP_CONTENT = b"\x1f\x8b\x08\x08\xf0\x159f\x02\xffrf_hash_threatfeed_trending_in_recorded_future_analyst_community_stix_1.2.xml\x00u\xd3\xcfo\x820\x14\x07\xf0\xfb\xfe\n\xc2\xce\x85\xc2\xea\x0f\x88p\xd9B\xe6iF\xc9\xb2\xecbJ)ZG\xa9i\x8ba\xff\xfd\xc0TQ\x1c7^\xf9|_\xfa\xc8c\xa14k\xc2M\xba\xfc\xda\xae0\xf9\xc1;j\xb1<\xb2\xd7IhJ\x80\x02D\x83\xc0\x87`\x8e\xbc\x19@x\x8a\x01F\xb4\x00\xb0\xc8\x82l:\xf3^\xbc\xc9\xdc\xb64\xe3Ti\xcc\x8f\x91\xedC\x1f\x018\x01\x10\xa5\x10\x86\x08\x86\x10:\xde\xdc\xfb\xb6\xad\x13\x95\x8a\x89*\xb2=\xc7\xb7\xad\x86\x97\x95\x8a\xec\xbd\xd6\xc7\xd0u\xdb\xca\xe5T\xe3\x1ck\xbc\xd9c\xc9\xaa\x9d\xd3\xa8\xdc\xb0p\x9d\\ewcGR\"dN\xf3\xa2\xd6\xb5\xa4\x0e\x11\xdc\xbd\xd0\x84\x95\xf4#;\\=\xf9\xcdD\xe3p\xa6['\xe4\xce\x15\xd9\x81\x12\xad\x9e\x8dk\x9f\xc1\xe56\xe1\xd9~\n\x8235\x9a\xcfi\x81\xebRoO\x1d\xab\xcb\xf6\xaaT\r:\xbc\n\xce\xbb9G:\x90\xf3\xebAf\\wu\x8f[t\xff)z\x99\xa6+\xe0]\x1c\xabrF\xb0\x16rL//\xa0\xef\xdd\x89\xc1\xf4\x83\xd0\xbf\xc3{\xb7\xf9\xc1\xec\x83\xbc\x19\xfd.1f\xbb\xb2\x95\xf1\xa2\xdf\xd1w\x8as*\xcd\xc9\x1bUD\xb2\xa3nW*^\x9b}\xb0\x92\xf3BX\x9d^\xb8\x0f\xcc\x1c=\xf6\xba~\x0c\x15?\x19tst\x1b3\xffE\xfc\x07J\n\x9c\x10:\x03\x00\x00"


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
    def return_magic_mock(content: bytes, status_code: int) -> MagicMock:
        mock_response = MagicMock()
        type(mock_response).status_code = mock.PropertyMock(return_value=status_code)
        mock_response.iter_content.return_value = [bytes(content)]
        return mock_response

    @staticmethod
    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None, contains_content: bool = False) -> None:
                self.status_code = status_code
                if filename:
                    self.text = Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{filename}.json.resp")
                    )
                else:
                    self.text = ""
                if contains_content:
                    self.content = GZIP_CONTENT
                else:
                    self.content = ""

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
            return Util.return_magic_mock(GZIP_CONTENT, 200)
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/domain/riskrules":
            return MockResponse(200, "list_domain_risk_rules")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/domain/search":
            return MockResponse(200, "search_domains")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/hash/risklist":
            return Util.return_magic_mock(GZIP_CONTENT, 200)
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/hash/riskrules":
            return MockResponse(200, "list_hash_risk_rules")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/hash/search":
            return MockResponse(200, "search_hashes")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/ip/risklist":
            return Util.return_magic_mock(GZIP_CONTENT, 200)
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/ip/riskrules":
            return MockResponse(200, "list_ip_addresses_risk_rules")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/ip/search":
            return MockResponse(200, "search_ip_addresses")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/url/risklist":
            return Util.return_magic_mock(GZIP_CONTENT, 200)
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/url/riskrules":
            return MockResponse(200, "list_url_risk_rules")
        if kwargs.get("url") == "https://api.recordedfuture.com/v2/vulnerability/risklist":
            return Util.return_magic_mock(GZIP_CONTENT, 200)
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
