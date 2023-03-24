import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from unit_test.util import Util
from icon_rapid7_intsights.actions.get_cves_for_cyber_term import GetCvesForCyberTerm
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_rapid7_intsights.actions.get_cves_for_cyber_term.schema import Input


@patch("requests.request", side_effect=Util.mock_request)
class TestGetCvesForCyberTerm(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetCvesForCyberTerm())

    @parameterized.expand(
        [
            [
                "existing_cyber_term_with_cves",
                {Input.CYBERTERMID: "621a1a11aa1aa22222bb2b33"},
                Util.read_file_to_dict("expecteds/get_cves_for_cyber_term_existing_with_cves.json.resp"),
            ],
            [
                "non_existing_cyber_term",
                {Input.CYBERTERMID: "621a1a11aa1cc22222bb2b33"},
                Util.read_file_to_dict("expecteds/get_cves_for_cyber_term_empty_cves_list.json.resp"),
            ],
            [
                "existing_cyber_term_with_no_cves",
                {Input.CYBERTERMID: "621a1a11aa1dd22222bb2b33"},
                Util.read_file_to_dict("expecteds/get_cves_for_cyber_term_empty_cves_list.json.resp"),
            ],
        ]
    )
    def test_test_get_cves_for_cyber_term(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_cyber_term_id_1",
                {Input.CYBERTERMID: "221a1a11a21c322fd22bb2b33"},
                PluginException(preset=PluginException.Preset.NOT_FOUND),
            ],
            [
                "invalid_cyber_term_id_2",
                {Input.CYBERTERMID: "invalid_id"},
                PluginException(preset=PluginException.Preset.NOT_FOUND),
            ],
        ]
    )
    def test_test_get_cves_for_cyber_term_raise_exception(
        self, mock_request, test_name, input_parameters, expected_exception
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, expected_exception.cause)
        self.assertEqual(error.exception.assistance, expected_exception.assistance)
