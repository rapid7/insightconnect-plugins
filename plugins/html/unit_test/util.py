import json
import os
import sys

STUB_VALID_INPUT = "<!DOCTYPE html><html><title>Example</title><body><h1>Rapid7 InsightConnect</h1><p>Automate with InsightConnect!</p></body></html>"
sys.path.append(os.path.abspath("../"))


class Util:
    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_data(filename, path="payloads"):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    f"{path}/{filename}.json.resp",
                )
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.headers = Util.load_data(self.filename).get("headers", {})
                self.text = str(self.json())

            def json(self):
                return Util.load_data(self.filename).get("json", {})

            def raise_for_status(self):
                return

        data = kwargs.get("data")

        if (
            data
            == b"<!DOCTYPE html><html><title>Example</title><body><h1>Rapid7 InsightConnect</h1><p>Automate with InsightConnect!</p></body></html>"
        ):
            return MockResponse("validate_json_body", 200)
        if data == b"bad input, expecting false validation":
            return MockResponse("validate_error", 400)
        if data == "":
            return MockResponse(Exception, 400)
        raise Exception("Not Implemented")
