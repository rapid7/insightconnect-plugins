import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from komand_redhat_advisory.connection.connection import Connection


class Util:
    @staticmethod
    def default_connector(action):
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connection.connect({})
        action.connection = connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def _load_response(filename):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{filename}.json.resp")
        with open(path) as fp:
            return json.load(fp)

    @staticmethod
    def mocked_session_send(prepared_request, **_kwargs):
        class MockResponse:
            def __init__(self, payload, status_code=200):
                self._payload = payload
                self.status_code = status_code
                self.text = json.dumps(payload)
                self.content = self.text.encode()
                self.headers = {"content-type": "application/json"}

            def json(self):
                return self._payload

            def raise_for_status(self):
                return None

        url = prepared_request.url
        if url.startswith("https://access.redhat.com/hydra/rest/securitydata/csaf.json"):
            return MockResponse(Util._load_response("csaf_list_page1"))
        raise Exception(f"Unmocked URL: {url}")
