import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_rapid7_insightvm.actions.create_exception import CreateException
from komand_rapid7_insightvm.actions.create_exception.schema import Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestCreateException(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateException())

    @parameterized.expand(
        [
            [
                "create_exception",
                "Global",
                "test_vulnerability",
                None,
                "01-01-2022",
                "Test Exception",
                "False Positive",
                None,
                None,
                {
                    "id": 1,
                    "links": [
                        {"href": "https://example.com/api/3/vulnerability_exceptions", "rel": "self"},
                        {
                            "href": "https://example.com/api/3/vulnerability_exceptions/1",
                            "rel": "Vulenrability Exception",
                        },
                    ],
                },
            ],
            [
                "create_exception_2",
                "Instance",
                "test_vulnerability",
                12345,
                "Jan 13 2022",
                "Test Exception",
                "Other",
                "9de5069c5afe602b2ea0a04b66beb2c0",
                40000,
                {
                    "id": 1,
                    "links": [
                        {"href": "https://example.com/api/3/vulnerability_exceptions", "rel": "self"},
                        {
                            "href": "https://example.com/api/3/vulnerability_exceptions/1",
                            "rel": "Vulenrability Exception",
                        },
                    ],
                },
            ],
            [
                "create_exception_3",
                "Asset",
                "test_vulnerability",
                12345,
                None,
                "Test Exception",
                "Acceptable Use",
                None,
                None,
                {
                    "id": 1,
                    "links": [
                        {"href": "https://example.com/api/3/vulnerability_exceptions", "rel": "self"},
                        {
                            "href": "https://example.com/api/3/vulnerability_exceptions/1",
                            "rel": "Vulenrability Exception",
                        },
                    ],
                },
            ],
        ]
    )
    def test_create_exception(
        self, mock_post, name, exception_type, vulnerability, scope, expiration, comment, reason, key, port, expected
    ) -> None:
        actual = self.action.run(
            {
                Input.TYPE: exception_type,
                Input.VULNERABILITY: vulnerability,
                Input.SCOPE: scope,
                Input.EXPIRATION: expiration,
                Input.COMMENT: comment,
                Input.REASON: reason,
                Input.KEY: key,
                Input.PORT: port,
            }
        )
        self.assertEqual(actual, expected)
