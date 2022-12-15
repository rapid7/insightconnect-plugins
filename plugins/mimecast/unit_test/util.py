import json
import logging
import os.path
import sys

sys.path.append(os.path.abspath("../"))
from komand_mimecast.connection import Connection
from komand_mimecast.connection.schema import Input
from komand_mimecast.util.constants import DATA_FIELD, DEFAULT_REGION


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.REGION: DEFAULT_REGION,
            Input.ACCESS_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
            Input.SECRET_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
            Input.APP_ID: "9de5069c5afe602b2ea0a04b66beb2c0",
            Input.APP_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
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
            def __init__(self, filename: str = None):
                self.filename = filename

            def json(self):
                return Util.load_json(f"responses/{self.filename}")

        if kwargs.get("url") == "https://eu-api.mimecast.com/api/directory/add-group-member":
            if "test4@rapid7.com" in kwargs.get(DATA_FIELD):
                return MockResponse("add_group_member.json.resp")
            elif "bad@rapid7.com" in kwargs.get(DATA_FIELD):
                return MockResponse("add_group_member_bad.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/policy/blockedsenders/create-policy":
            if "some test policy" in kwargs.get(DATA_FIELD):
                return MockResponse("create_blocked_sender_policy.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/policy/blockedsenders/delete-policy":
            if "1234" in kwargs.get(DATA_FIELD):
                return MockResponse("delete_blocked_sender_policy.json.resp")
            else:
                return MockResponse("delete_blocked_sender_policy_bad.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/message-finder/search":
            return MockResponse("search_message_tracking.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/ttp/url/create-managed-url":
            if "https://www.test.net/" in kwargs.get(DATA_FIELD):
                return MockResponse("create_managed_url.json.resp")
            if "https://www.bad.net/" in kwargs.get(DATA_FIELD):
                return MockResponse("create_managed_url_bad.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/ttp/url/decode-url":
            if "https://protect-xx.mimecast.com/" in kwargs.get(DATA_FIELD):
                return MockResponse("decode_url.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/directory/remove-group-member":
            if "test4@rapid7.com" in kwargs.get(DATA_FIELD):
                return MockResponse("delete_group_member.json.resp")
            elif "bad@rapid7.com" in kwargs.get(DATA_FIELD):
                return MockResponse("delete_group_member_bad.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/ttp/url/delete-managed-url":
            if "wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3I" in kwargs.get(DATA_FIELD):
                return MockResponse("delete_managed_url.json.resp")
            elif "bad_id" in kwargs.get(DATA_FIELD):
                return MockResponse("delete_managed_url_bad.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/directory/find-groups":
            if "test_query" in kwargs.get(DATA_FIELD):
                return MockResponse("find_groups_empty_groups.json.resp")
            elif "500" in kwargs.get(DATA_FIELD):
                return MockResponse("find_groups_500.json.resp")
            elif "403" in kwargs.get(DATA_FIELD):
                return MockResponse("find_groups_403.json.resp")
            elif "404" in kwargs.get(DATA_FIELD):
                return MockResponse("find_groups_404.json.resp")
            else:
                return MockResponse("find_groups.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/audit/get-audit-events":
            return MockResponse("get_audit_events.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/ttp/url/get-all-managed-urls":
            if "test_domain" in kwargs.get(DATA_FIELD):
                return MockResponse("get_managed_url_empty_response.json.resp")
            else:
                return MockResponse("get_managed_url.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/ttp/url/get-logs":
            return MockResponse("get_ttp_url_logs.json.resp")
        elif kwargs.get("url") == "https://eu-api.mimecast.com/api/managedsender/permit-or-block-sender":
            if "permit" in kwargs.get(DATA_FIELD):
                return MockResponse("permit_or_block_sender.json.resp")
            elif "block" in kwargs.get(DATA_FIELD):
                if "bad_email" in kwargs.get(DATA_FIELD):
                    return MockResponse("permit_or_block_sender_bad.json.resp")
                else:
                    return MockResponse("block_sender.json.resp")
        return "Not implemented"
