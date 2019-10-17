import json
import logging
import re
from unittest import TestCase, mock

import maya
import requests
import timeout_decorator
from komand.exceptions import PluginException

from icon_bmc_remedy_itsm.triggers import NewIncidentFound


# This will catch timeout errors and return None, which will make tests pass
def timeout_pass(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except timeout_decorator.timeout_decorator.TimeoutError as e:
            print(f"Test timed out as expected: {e}")
            return None

    return func_wrapper


# Get a real payload from file
def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, headers):
    class MockResponse:
        def __init__(self, data, status_code):
            self.status_code = status_code
            self.text = data

        def raise_for_status(self):
            if self.status_code >= 400:
                raise requests.HTTPError(f"{self.status_code}")

        def json(self):
            return json.loads(self.text)

    print(f"Headers: {headers}")

    mock_get_new_incidents_payload = read_file_to_string('./payloads/get_new_incidents.json')

    if args[0] == 'http://test.url/api/arsys/v1/entry/HPD:IncidentInterface?sort=Submit Date.desc':
        return MockResponse(mock_get_new_incidents_payload, 200)
    if args[0] == 'http://test.url/api/arsys/v1/entry/HPD:IncidentInterface?sort=Submit Date.desc&limit=1':
        return MockResponse(mock_get_new_incidents_payload, 200)

    print(f"Attempted to get:\n{args[0]}")
    return MockResponse(None, 404)


def mock_send(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


class MockConnection():
    def __init__(self):
        self.url = "http://test.url"

    def make_headers_and_refresh_token(self):
        return {"headers": "test_headers"}


class TestNewIncidentFound(TestCase):
    def setUp(self) -> None:
        self.test_return_value = {}

    # This is a live test
    @timeout_pass
    @timeout_decorator.timeout(15)
    def test_new_incident_found(self):
        # log = logging.getLogger("Test")
        #
        # test_connection = Connection()
        # test_new_incident_found = NewIncidentFound()
        #
        # test_connection.logger = log
        # test_new_incident_found.logger = log
        #
        # with open("../tests/get_incident_information.json") as file:
        #     data = json.load(file)
        #     connection_params = data.get("body").get("connection")
        #
        # test_connection.connect(connection_params)
        # test_new_incident_found.connection = test_connection
        #
        # incident_found_params = {
        #     "short_description_query": "",
        #     "interval": 5
        # }
        #
        # test_new_incident_found.run(incident_found_params)
        pass

    def test_check_new_incidents_and_send(self):
        log = logging.getLogger("Test")
        nif = NewIncidentFound()
        nif.logger = log

        new_incidents_json = json.loads(read_file_to_string('./payloads/get_new_incidents.json'))

        nif._check_new_incidents_and_send("", maya.now(), new_incidents_json)
        pass  # We are just making sure the last call didn't throw an exception.

    @mock.patch('icon_bmc_remedy_itsm.triggers.NewIncidentFound.send', side_effect=mock_send)
    def test_check_new_incidents_and_send_valid_return(self, mockSend):
        log = logging.getLogger("Test")
        nif = NewIncidentFound()
        nif.logger = log

        new_incidents_json = json.loads(read_file_to_string('./payloads/get_new_incidents.json'))
        test_for_time = maya.parse("2019-09-19T15:00:00.000+0000")
        nif._check_new_incidents_and_send(None, test_for_time, new_incidents_json)

        self.assertEqual(mockSend.call_count, 2)

        actual_call = mockSend.call_args_list
        incident1 = actual_call[0][0][0].get('incident').get('values')
        incident2 = actual_call[1][0][0].get('incident').get('values')

        self.assertEqual(incident1.get("Entry ID"), 'INC000000000109')
        self.assertEqual(incident2.get("Entry ID"), 'INC000000000108')

    @mock.patch('icon_bmc_remedy_itsm.triggers.NewIncidentFound.send', side_effect=mock_send)
    def test_check_new_incidents_and_send_with_query(self, mockSend):
        log = logging.getLogger("Test")
        nif = NewIncidentFound()
        nif.logger = log

        new_incidents_json = json.loads(read_file_to_string('./payloads/get_new_incidents.json'))
        test_for_time = maya.parse("2019-09-19T15:00:00.000+0000")

        compiled_query = re.compile("Testing Incident Trigger for Query")

        nif._check_new_incidents_and_send(compiled_query, test_for_time, new_incidents_json)

        self.assertEqual(mockSend.call_count, 1)

        actual_call = mockSend.call_args_list
        incident1 = actual_call[0][0][0].get('incident').get('values')
        self.assertEqual(incident1.get("Entry ID"), 'INC000000000109')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_new_incidents(self, mock_get):
        log = logging.getLogger("Test")
        nif = NewIncidentFound()
        nif.connection = MockConnection()
        nif.logger = log

        actual = nif._get_new_incidents()

        self.assertEqual(actual.get('entries')[0].get('values').get('Entry ID'), "INC000000000109")

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_initial_incident_info(self, mock_get):
        log = logging.getLogger("Test")
        nif = NewIncidentFound()
        nif.connection = MockConnection()
        nif.logger = log

        actual = nif._get_initial_incident_info()
        expected = maya.parse('Tue, 24 Sep 2019 18:08:11 GMT')

        self.assertEqual(actual, expected)

    def test_check_and_compile_query(self):
        log = logging.getLogger("Test")
        nif = NewIncidentFound()
        nif.connection = MockConnection()
        nif.logger = log

        actual = nif._check_and_compile_query(".*")
        expected = re.compile(".*")

        self.assertEqual(actual, expected)

    def test_check_and_compile_query_bad_regex(self):
        log = logging.getLogger("Test")
        nif = NewIncidentFound()
        nif.connection = MockConnection()
        nif.logger = log

        with self.assertRaises(PluginException):
            nif._check_and_compile_query("[")
