import json
import os

import requests.models

from unit_test.util import Util

STUB_IDENTIFIER = "3395856ce81f2b7382dee72602f798b642f14140-cve"
STUB_404_IDENTIFIER = "4416967df92g3c8493eff83513g819c753g23241-cve"
STUB_504_IDENTIFIER = "5527178eg13h4d9514egg94624h921d864h34352-cve"
STUB_SEARCH_IDENTIFIER = "4416967df92g3c8493eff83513g819c753g23241-cve"
STUB_SEARCH_NO_RESULTS_IDENTIFIER = "5527178eg13h4d9514egg94624h921d864h34352-cve"
STUB_SEARCH_404_IDENTIFIER = "3395856ce81f2b7382dee72602f798b642f14140-cve"
STUB_SEARCH_504_IDENTIFIER = "6628289fh24g5e1625fhh15735i132e97i45463-cve"
STUB_SEARCH_CONTENT_IDENTIFIER_1 = "test_identifier_3"
STUB_SEARCH_CONTENT_IDENTIFIER_2 = "test_identifier_2"
STUB_SEARCH_CONTENT_IDENTIFIER_3 = "test_identifier_5"
STUB_SEARCH_CONTENT_IDENTIFIER_4 = "test_identifier_6"
STUB_ORG_KEY_FORBIDDEN = "org_key_forbidden"
REQUEST_GET = "GET"
REQUEST_POST = "POST"


# Define and return mock API responses based on request type and endpoint
def mock_request(*args, **kwargs):
    class MockResponse:
        def __init__(self, filename: str, status_code: int) -> None:
            self.status_code = status_code
            if filename:
                self.text = Util.read_file_to_string(
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
                )
            else:
                self.text = ""

        def json(self):
            return json.loads(self.text)

    # Check reqeust type and endpoint. Return appropriate file name to be loaded and response code
    if args[0] == f"https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/{STUB_IDENTIFIER}":
        return MockResponse("get_content", 200)
    if args[0] == f"https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/{STUB_SEARCH_CONTENT_IDENTIFIER_1}":
        return MockResponse("search_db_test_identifier_3", 200)
    if args[0] == f"https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/{STUB_SEARCH_CONTENT_IDENTIFIER_2}":
        return MockResponse("search_db_test_identifier_4", 200)
    if args[0] == f"https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/{STUB_SEARCH_CONTENT_IDENTIFIER_3}":
        return MockResponse("search_db_test_identifier_5", 200)
    if args[0] == f"https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/{STUB_SEARCH_CONTENT_IDENTIFIER_4}":
        return MockResponse("search_db_test_identifier_6", 200)
    if args[0] == f"https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/{STUB_404_IDENTIFIER}":
        return MockResponse("get_content_bad", 404)
    if args[0] == f"https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/{STUB_504_IDENTIFIER}":
        return MockResponse("get_content_bad2", 504)
    if args[0] == f"https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/search":
        query = kwargs.get("params").get("query")
        page = kwargs.get("params").get("page")
        type_ = kwargs.get("params").get("type")
        if query == STUB_SEARCH_NO_RESULTS_IDENTIFIER:
            return MockResponse("search_db_no_results", 200)
        if query == STUB_SEARCH_404_IDENTIFIER:
            return MockResponse("search_db_bad", 404)
        if query == STUB_SEARCH_504_IDENTIFIER:
            return MockResponse("search_db_bad", 504)
        if query == STUB_SEARCH_IDENTIFIER and type_ == "Metasploit":
            if page == 0:
                return MockResponse("search_db_metasploit_page_0", 200)
            return MockResponse("search_db_metasploit", 200)
        if query == STUB_SEARCH_IDENTIFIER and type_ == "Nexpose":
            if page == 0:
                return MockResponse("search_db_nexpose_page_0", 200)
            return MockResponse("search_db_nexpose", 200)
        if query == STUB_SEARCH_IDENTIFIER:
            if page == 0:
                return MockResponse("search_db_page_0", 200)
            if page == 1:
                return MockResponse("search_db_page_1", 200)
            return MockResponse("search_db", 200)
        return MockResponse("search_db", 200)
    raise Exception("Response has been not implemented")
