import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_rapid7_insightcloudsec.actions.list_clouds import ListClouds
from icon_rapid7_insightcloudsec.actions.list_clouds.schema import Input
from util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestListClouds(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListClouds())

    # Excluded 'badges' field from input
    @parameterized.expand(Util.load_parameters("list_clouds").get("parameters"))
    def test_list_clouds(
        self,
        mock_request,
        name: str,
        filters: list,
        limit: int,
        offset: int,
        order_by: str,
        badge_filter_operator: str,
        search_string: str,
        advanced_search: bool,
        empty_badges: bool,
        exclusion_badges: list,
        expected: dict,
    ):

        actual = self.action.run(
            {
                Input.FILTERS: filters,
                Input.LIMIT: limit,
                Input.OFFSET: offset,
                Input.ORDER_BY: order_by,
                Input.BADGE_FILTER_OPERATOR: badge_filter_operator,
                Input.SEARCH_STRING: search_string,
                Input.ADVANCED_SEARCH: advanced_search,
                Input.EMPTY_BADGES: empty_badges,
                Input.EXCLUSION_BADGES: exclusion_badges,
            }
        )

        self.assertEqual(actual, expected)
