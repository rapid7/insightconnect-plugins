import os
import sys

sys.path.append(os.path.abspath("../"))

import json
import logging
from unittest import TestCase

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightvm.util import resource_helpers

# Mock user dictionary
user = {
    "type": "ldap",
    "authentication": {"id": 7},
    "role": {"allAssetGroups": False, "allSites": False, "id": "manage-sites"},
    "email": "jdoe@rapid7.com",
    "login": "jdoe",
    "enabled": True,
    "name": "John Doe",
}


class MockResponse:
    def __init__(self) -> None:
        self.text = '{"resources": [{"thing1": "data"},{"thing2": "data"}], "page": {"number": 0, "totalPages": 2}}'
        self.status_code = 200

    def json(self):
        return json.loads(self.text)


class MockSession:
    def __init__(self) -> None:
        self.counter = 0
        self.headers = dict()

    def get(self, url, verify, **kwargs):
        mock_response = MockResponse()
        if url == "exception.com":
            raise requests.HTTPError

        if url == "bad password":
            mock_response.status_code = 401
        if url == "paged_request":
            if self.counter > 0:
                temp = json.loads(mock_response.text)
                temp["page"]["number"] += 1
                mock_response.text = json.dumps(temp)
            self.counter += 1

        return mock_response


class TestValidateUser(TestCase):
    def test_init(self) -> None:
        logger = logging.getLogger("logger")
        session = requests.session()
        test_object = resource_helpers.ValidateUser(logger=logger, session=session, ssl_verify=False)
        self.assertIsNotNone(test_object)
        self.assertTrue(test_object.logger.name == "logger")

    def test_validate_role_exists(self) -> None:
        logger = logging.getLogger("logger")
        session = requests.session()
        test_object = resource_helpers.ValidateUser(logger=logger, session=session, ssl_verify=False)
        test_object.validate_user_email(user["email"])
        with self.assertRaises(PluginException) as error:
            test_object.validate_user_email("foo")
        self.assertEqual(error.exception.cause, "The email address for user account was not valid")
        self.assertEqual(error.exception.assistance, "Ensure that the email address is correct")
