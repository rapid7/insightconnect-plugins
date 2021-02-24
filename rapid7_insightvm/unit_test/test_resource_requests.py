import sys
import os

sys.path.append(os.path.abspath("../"))

from komand.exceptions import PluginException
from unittest import TestCase
from komand_rapid7_insightvm.util import resource_requests
import logging
import requests
import json
import pytest


class MockResponse:
    def __init__(self):
        self.text = '{"resources": [{"thing1": "data"},{"thing2": "data"}], "page": {"number": 0, "totalPages": 2}}'
        self.status_code = 200

    def json(self):
        return json.loads(self.text)


class MockSession:
    def __init__(self):
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


class TestResourceRequests(TestCase):
    def test_init(self):
        logger = logging.getLogger("logger")
        session = requests.session()
        test_object = resource_requests.ResourceRequests(logger=logger, session=session)
        self.assertIsNotNone(test_object)
        self.assertTrue(test_object.logger.name == "logger")

    # @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_resource_request(self):
        logger = logging.getLogger("logger")
        session = MockSession()
        test_object = resource_requests.ResourceRequests(logger=logger, session=session)
        response = test_object.resource_request("google")
        self.assertIsNotNone(response)
        self.assertEqual(response.get("resources"), [{"thing1": "data"}, {"thing2": "data"}])

    def test_resource_request_requests_exception(self):
        logger = logging.getLogger("logger")
        session = MockSession()
        test_object = resource_requests.ResourceRequests(logger=logger, session=session)
        with pytest.raises(PluginException):
            response = test_object.resource_request("exception.com")

    def test_resource_request_401(self):
        logger = logging.getLogger("logger")
        session = MockSession()
        test_object = resource_requests.ResourceRequests(logger=logger, session=session)
        with pytest.raises(PluginException, match="InsightVM returned an error message. Unauthorized"):
            response = test_object.resource_request("bad password")


class TestPagedResourceRequest(TestCase):
    def test_paged_resource_request_no_params(self):
        logger = logging.getLogger("logger")
        session = MockSession()
        test_object = resource_requests.ResourceRequests(logger=logger, session=session)
        response = test_object.paged_resource_request("paged_request")
        self.assertIsNotNone(response)
        self.assertEqual(
            response,
            [{"thing1": "data"}, {"thing2": "data"}, {"thing1": "data"}, {"thing2": "data"}],
        )

    def test_paged_resource_request_with_params_dict(self):
        logger = logging.getLogger("logger")
        session = MockSession()
        test_object = resource_requests.ResourceRequests(logger=logger, session=session)
        response = test_object.paged_resource_request("paged_request", params={"size": 100})
        self.assertIsNotNone(response)
        self.assertEqual(
            response,
            [{"thing1": "data"}, {"thing2": "data"}, {"thing1": "data"}, {"thing2": "data"}],
        )

    def test_paged_resource_request_with_params_tuple(self):
        logger = logging.getLogger("logger")
        session = MockSession()
        test_object = resource_requests.ResourceRequests(logger=logger, session=session)
        response = test_object.paged_resource_request("paged_request", params=[("size", 100)])
        self.assertIsNotNone(response)
        self.assertEqual(
            response,
            [{"thing1": "data"}, {"thing2": "data"}, {"thing1": "data"}, {"thing2": "data"}],
        )
