from unittest import TestCase, mock

import requests

from icon_html.actions.validate import Validate
from icon_html.actions.validate.schema import Input
from unit_test.util import Util, STUB_VALID_INPUT

import sys
import os

sys.path.append(os.path.abspath("../"))


class TestValidate(TestCase):
    @mock.patch("requests.post", side_effect=Util.mocked_requests)
    def test_validate(self, mocked_requests):
        test_validate = Validate()
        input_params = {Input.HTML_CONTENTS: STUB_VALID_INPUT}
        results = test_validate.run(input_params)
        expected_response = {"validated": True}
        self.assertEqual(results, expected_response)

    @mock.patch("requests.post", side_effect=Util.mocked_requests)
    def test_validate_false(self, mocked_requests):
        test_validate = Validate()
        input_params = {Input.HTML_CONTENTS: "bad input, expecting false validation"}
        results = test_validate.run(input_params)
        expected_response = {"validated": False}
        self.assertEqual(results, expected_response)

    # @mock.patch("requests.post", side_effect=Util.mocked_requests)
    # def test_validate_exception(self, mocked_requests, cause, assistance):
    #
    #     test_validate = Validate()
    #     print(test_validate)
    #
    #     input_params = {Input.HTML_CONTENTS: ""}
    #     results = test_validate.run(input_params)
    #     print(results)
    #     # expected_response = {"validated": False}
    #     # self.assertEqual(results, expected_response)
    #     self.assertEqual(results, requests.exceptions.RequestException)
    #     self.assertEqual(cause, "IO Error: ")
    #     self.assertEqual(assistance, "Please check logs.")
