# These will be used if the live test is uncommented
import json
from icon_bmc_remedy_itsm.connection import Connection

import logging
from unittest import TestCase, mock
import requests
from icon_bmc_remedy_itsm.actions import UpdateIncidentStatus


class MockConnection():
    def __init__(self):
        self.url = "http://test.url"

    def make_headers_and_refresh_token(self):
        return {"headers": "test_headers"}

    def connect(self, params):
        pass


# This method will be used by the mock to replace requests.get
# json is a named arg that we're overriding, it must be named json
def mocked_requests_get(*args, headers, json=None):
    class MockResponse:
        def __init__(self, data, status_code):
            self.status_code = status_code
            self.json_ = data
            self.text = "There was an error"

        def raise_for_status(self):
            if self.status_code >= 400:
                raise requests.HTTPError(f"{self.status_code}")

        def json(self):
            return self.json_

    mock_object = {
        'values': {
            'Status': 'Assigned',
            'Entry ID': 'INC000000000108'
        }
    }

    if args[0] == 'http://test.url/api/arsys/v1/entry/HPD%3AIncidentInterface/INC000000000108|INC000000000108':
        if not json:  # If there's no body, this is a get, else it's a put
            return MockResponse(mock_object, 200)
        return MockResponse(mock_object, 204)

    print(f"Attempted to get:\n{args[0]}")
    return MockResponse(None, 404)


class TestUpdateIncidentStatus(TestCase):
    def test_update_incident_status_live_test(self):
        # # This is a live test. Run icon-lab set and uncomment to run

        # log = logging.getLogger("Test")
        #
        # test_connection = Connection()
        # test_update_incident_status = UpdateIncidentStatus()
        #
        # test_connection.logger = log
        # test_update_incident_status.logger = log
        #
        # with open("../tests/get_incident_information.json") as file:
        #     data = json.load(file)
        #     connection_params = data.get("body").get("connection")
        #
        # test_connection.connect(connection_params)
        # test_update_incident_status.connection = test_connection
        #
        # new_status = "Assigned"
        # update_incident_params = {
        #     "incident_id": "INC000000000108",
        #     "status": new_status
        # }
        #
        # result = test_update_incident_status.run(update_incident_params)
        # actual = result.get("incident").get("values")
        #
        # self.assertEqual(actual.get("Status"), new_status)
        # self.assertEqual(actual.get("Entry ID"), "INC000000000108")
        pass

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('requests.put', side_effect=mocked_requests_get)
    def test_update_incident_status(self, mockGet, mockPut):
        log = logging.getLogger("Test")

        test_connection = MockConnection()
        test_update_incident_status = UpdateIncidentStatus()

        test_connection.logger = log
        test_update_incident_status.logger = log

        connection_params = {
            "credentials": {
                "password": "password",
                "username": "username"
            },
            "port": "8008",
            "ssl_verify": True,
            "url": "http://remd-itsm1902.vuln.lax.rapid7.com"
        }

        test_connection.connect(connection_params)
        test_update_incident_status.connection = test_connection

        new_status = "Assigned"
        update_incident_params = {
            "incident_id": "INC000000000108",
            "status": new_status
        }

        result = test_update_incident_status.run(update_incident_params)
        actual = result.get("incident").get("values")

        self.assertEqual(actual.get("Status"), new_status)
        self.assertEqual(actual.get("Entry ID"), "INC000000000108")
