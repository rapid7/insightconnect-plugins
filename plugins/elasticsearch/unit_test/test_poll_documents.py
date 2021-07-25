import sys
import os
import timeout_decorator
from komand_elasticsearch.triggers import PollDocuments
from komand_elasticsearch.actions.index_document.schema import Input
from unit_test.util import Util
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))


actual = None


def timeout_pass(error_callback=None):
    def func_timeout(func):
        def func_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except timeout_decorator.timeout_decorator.TimeoutError as e:
                if error_callback:
                    return error_callback()

                return None

        return func_wrapper

    return func_timeout


class MockTrigger:
    actual = None

    @staticmethod
    def send(params):
        MockTrigger.actual = params


def check_error():
    expected = {
        "hits": [
            {
                "_index": "test-index",
                "_type": "_doc",
                "_id": "VWx5O3oBrBTgS4Hhf6Hp",
                "_score": 1.0,
                "_source": {"id": 1, "message": "Some message"},
            },
            {
                "_index": "test-index",
                "_type": "_doc",
                "_id": "Vmx6O3oBrBTgS4HhWKFJ",
                "_score": 1.0,
                "_source": {"id": 1, "message": "Some message"},
            },
        ]
    }
    if MockTrigger.actual == expected:
        return True

    TestCase.assertDictEqual(TestCase(), MockTrigger.actual, expected)


class TestPollDocuments(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(PollDocuments())

    @timeout_pass(error_callback=check_error)
    @timeout_decorator.timeout(2)
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    @patch("insightconnect_plugin_runtime.Trigger.send", side_effect=MockTrigger.send)
    def test_poll_documents(self, mock_request, ss):
        self.action.run({Input.INDEX: "trigger-index"})
