import json
import logging
import os

from icon_hybrid_analysis.actions.lookup_terms.schema import Input as Input_terms
from icon_hybrid_analysis.connection import Connection
from icon_hybrid_analysis.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.URL: "https://www.hybrid-analysis.com",
            Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def load_json(filename):
        with open((os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))) as file:
            return json.loads(file.read())

    @staticmethod
    def mocked_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code

            def json(self):
                return Util.load_json(f"payloads/{self.filename}.json.resp")

        if (
            args[1] == "https://www.hybrid-analysis.com/api/v2/search/hash"
            and kwargs.get("params").get("hash") == "4c740b7f0bdc728daf9fca05241e85d921a54a6e17ae47ed1577a2b30792cf5c"
        ):
            return MockResponse("action_lookup_hash", 200)
        elif args[1] == "https://www.hybrid-analysis.com/api/v2/search/hash" and (
            kwargs.get("params").get("hash") == "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
            or kwargs.get("params").get("hash") == "44d88612fea8a8f36de82e1278abb02f"
        ):
            return MockResponse("action_lookup_hash_sha256_sha1", 200)
        elif (
            args[1]
            == "https://www.hybrid-analysis.com/api/v2/report/30f800f97aeaa8d62bdf3a6fb2b0681179a360c12e127f07038f8521461e5050/state"
        ):
            return MockResponse("action_report", 200)
        elif args[1] == "https://www.hybrid-analysis.com/api/v2/submit/file":
            return MockResponse("action_submit", 200)
        elif args[1] == "https://www.hybrid-analysis.com/api/v2/search/terms":
            request_data = kwargs.get("data")
            if request_data.get(Input_terms.FILENAME) == "test" and request_data.get(Input_terms.VERDICT) == 1:
                return MockResponse("action_lookup_terms_filename", 200)
            elif request_data.get(Input_terms.COUNTRY) == "AFG":
                return MockResponse("action_lookup_terms_country", 200)
            elif request_data.get(Input_terms.DOMAIN) == "example.com":
                return MockResponse("action_lookup_terms_domain", 200)
            elif request_data.get(Input_terms.FILETYPE) == "perl":
                return MockResponse("action_lookup_terms_filetype", 200)
            elif request_data.get(Input_terms.HOST) == "198.51.100.1":
                return MockResponse("action_lookup_terms_host", 200)
            elif (
                request_data.get(Input_terms.SIMILAR_TO)
                == "ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c"
            ):
                return MockResponse("action_lookup_terms_similarto", 200)
            elif request_data.get(Input_terms.TAG) == "ransomware":
                return MockResponse("action_lookup_terms_tag", 200)
            elif request_data.get(Input_terms.URL) == "http://example.com":
                return MockResponse("action_lookup_terms_url", 200)
            elif request_data.get(Input_terms.PORT) == 8080:
                return MockResponse("action_lookup_terms_port", 200)
        else:
            Exception("Not implemented")
