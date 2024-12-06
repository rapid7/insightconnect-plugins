import json
import os

from greynoise import GreyNoise

PAYLOAD_MAPPING = {
    "community_lookup": "payloads/community_ip.json",
    "context_lookup": "payloads/context_ip.json",
    "gnql_query": "payloads/gnql_query.json",
    "quick_lookup": "payloads/quick_ip.json",
    "riot_lookup": "payloads/riot_ip.json",
    "similar_lookup": "payloads/similar_ip.json",
    "timeline_lookup": "payloads/timeline_ip.json",
    "vulnerability_lookup": "payloads/cve_details.json",
}


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def mocked_requests_get(*args, **kwargs):
    if len(args) == 0:
        filepath = "payloads/tag_details.json"
    else:
        filepath = PAYLOAD_MAPPING[args[0]]
    actual_path = os.path.dirname(os.path.realpath(__file__))
    actual_joined_path = os.path.join(actual_path, filepath)
    get_messages_from_user_payload = read_file_to_string(actual_joined_path)
    return json.loads(get_messages_from_user_payload)


class MockConnection:
    def __init__(self):
        self.server = "test_server"
        self.api_key = "test_api_key"
        self.user_agent = "test_user_agent"
        self.gn_client = GreyNoise(api_key=self.api_key, api_server=self.server, integration_name=self.user_agent)
