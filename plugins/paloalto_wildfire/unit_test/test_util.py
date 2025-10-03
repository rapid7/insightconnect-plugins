import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from collections import OrderedDict

from komand_paloalto_wildfire.connection.connection import Connection
from komand_paloalto_wildfire.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.HOST: "wildfire.paloaltonetworks.com",
            Input.API_KEY: {"secretKey": "example-wildfire-apikey"},
            Input.VERIFY: True,
            Input.PROXY: {},
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_bytes(filename):
        with open((os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)), "rb") as file:
            return file.read()

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code) -> None:
                self.status_code = status_code
                self.text = "error message"
                self.content = Util.read_file_bytes(f"payloads/{filename}.resp")

        if kwargs.get("url") == "http://www.pdf995.com/samples/pdf.pdf":
            return MockResponse("submit_file_from_url", 200)
        elif kwargs.get("url") == "http://www.pdf995.com/samples/in_db.pdf":
            return MockResponse("submit_file_from_url_in_db", 200)
        if kwargs.get("files").get("url")[1] == "http://www.pdf995.com/samples/pdf.pdf":
            return MockResponse("submit_file_from_url_api", 200)

    @staticmethod
    def mocked_requests_submit(*args, **kwargs):
        if args[1] == "EICAR.pdf":
            return OrderedDict(
                [
                    ("url", None),
                    ("filetype", "PE32 executable"),
                    ("filename", "EICAR.pdf"),
                    ("sha256", "90c943721c01975d0c7b7fda18bf0f7568cc27bd224e06d65cce81ce7cbd15ca"),
                    ("md5", "0b4d7fcf5d7d7b7b18fe445631308b12"),
                    ("size", "55296"),
                ]
            )

    @staticmethod
    def mocked_get_verdict(*args, **kwargs) -> str:
        if args[0] == "81a1bb060af110346cf504c7d80e3dc12f75df5a53a558aa75293d8f87156a5b":
            return "malware"
        elif args[0] == "90c943721c01975d0c7b7fda18bf0f7568cc27bd224e06d65cce81ce7cbd15ca":
            return "not found"
        elif args[0] == "ebb031c3945e884e695dbc63c52a5efcd075375046c49729980073585ee13c52":
            return "not found"
        elif args[0] == "a2b3c64119f82c520394966a2c040bd8385bb4c2cc9500d359db67eff14a7b9a":
            return "malware"
