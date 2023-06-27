import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from komand_rest.actions.put import Put
from util import Util
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


class TestPut(TestCase):
    @parameterized.expand(Util.load_data("put", "expected").get("parameters"))
    @mock.patch("requests.request", side_effect=Util.mocked_requests)
    def test_put_unit(self, name, _input, status_code, body_object, body_string, headers, connection, mock_requests):
        test_action = Util.default_connector(action=Put(), connect_params=connection)
        results = test_action.run(_input)
        self.assertEqual(status_code, results["status"])
        self.assertEqual(body_object, results["body_object"])
        self.assertEqual(
            body_string,
            results["body_string"],
        )
        self.assertEqual(
            headers,
            results["headers"],
        )

    @parameterized.expand(Util.load_data("put_error", "expected").get("parameters"))
    @mock.patch("requests.request", side_effect=Util.mocked_requests)
    def test_put_error_unit(self, name, _input, cause, assistance, data, connection, mock_requests):
        with self.assertRaises(PluginException) as error:
            test_action = Util.default_connector(action=Put(), connect_params=connection)
            test_action.run(_input)
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
        self.assertEqual(data, error.exception.data)
