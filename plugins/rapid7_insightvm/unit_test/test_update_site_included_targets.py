import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_rapid7_insightvm.actions.update_site_included_targets import UpdateSiteIncludedTargets
from komand_rapid7_insightvm.actions.update_site_included_targets.schema import Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.sessions.Session.put", side_effect=Util.mocked_requests)
class TestUpdateSiteIncludedTargets(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateSiteIncludedTargets())

    @parameterized.expand(
        [
            [
                "add_single_address",
                1,
                ["198.51.100.100"],
                False,
                {"id": 1, "links": [{"href": "https://example.com/api/3/sites/1/included_targets", "rel": "self"}]},
            ],
            [
                "add_several_addresses",
                1,
                ["198.51.100.100", "198.51.100.102", "example.com"],
                False,
                {"id": 1, "links": [{"href": "https://example.com/api/3/sites/1/included_targets", "rel": "self"}]},
            ],
            [
                "add_empty_list",
                1,
                [],
                False,
                {"id": 1, "links": [{"href": "https://example.com/api/3/sites/1/included_targets", "rel": "self"}]},
            ],
            [
                "add_empty_addresses",
                2,
                [],
                False,
                {"id": 2, "links": [{"href": "https://example.com/api/3/sites/2/included_targets", "rel": "self"}]},
            ],
            [
                "overwrite_single_address",
                1,
                ["198.51.100.100"],
                True,
                {"id": 1, "links": [{"href": "https://example.com/api/3/sites/1/included_targets", "rel": "self"}]},
            ],
            [
                "overwrite_several_addresses",
                1,
                ["198.51.100.100", "198.51.100.102", "example.com"],
                True,
                {"id": 1, "links": [{"href": "https://example.com/api/3/sites/1/included_targets", "rel": "self"}]},
            ],
            [
                "overwrite_empty_list",
                1,
                [],
                True,
                {"id": 1, "links": [{"href": "https://example.com/api/3/sites/1/included_targets", "rel": "self"}]},
            ],
        ]
    )
    def test_update_site_included_targets(
        self, mock_get, mock_put, name, site_id, included_targets, overwrite, expected
    ) -> None:
        actual = self.action.run(
            {Input.ID: site_id, Input.INCLUDED_TARGETS: included_targets, Input.OVERWRITE: overwrite}
        )
        self.assertEqual(actual, expected)
