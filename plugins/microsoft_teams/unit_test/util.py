import json
import logging
import sys
import os

sys.path.append(os.path.abspath("../"))


class MockConnection:
    def __init__(self):
        self.tenant_id = "1"

    def get_headers(self):
        return


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = MockConnection()
        default_connection.logger = logging.getLogger("connection logger")
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_data(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                if self.filename == "not_found":
                    self.text = 'Response was: {"message": "Not Found"}'
                elif self.filename == "already_exists":
                    self.text = 'Response was: {"message": "Already Exists"}'
                else:
                    self.text = "Error message"

            def json(self):
                return Util.load_data(self.filename)

            def raise_for_status(self):
                return

        print(args[0])
        if (
            args[0]
            == "https://graph.microsoft.com/beta/groups?$filter=resourceProvisioningOptions/Any(x:x eq 'Team') and displayName eq 'Example Team'"
        ):
            return MockResponse("get_teams", 200)
        if args[0] == "https://graph.microsoft.com/beta/1/teams/12345/channels":
            return MockResponse("get_channels", 200)
        if args[0] == "https://graph.microsoft.com/beta/teams/12345/channels/56789/messages":
            return MockResponse("send_message_channel", 200)
        if args[0] == "https://graph.microsoft.com/beta/teams/12345/channels/56789/messages/1636037542013/replies":
            return MockResponse("send_message_thread", 200)
        if args[0] == "https://graph.microsoft.com/beta/chats/19:10000_20000@unq.gbl.spaces/messages":
            return MockResponse("send_message_chat", 200)
        raise Exception("Not implemented")
