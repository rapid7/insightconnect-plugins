import unittest
import json

from pathlib import Path
from icon_aws_ec2.util.common import PaginationHelper


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.pagination_helper = PaginationHelper(
            input_token=["next_token"],
            output_token=["next_token"],
            result_key=["Reservations"],
            limit_key="max_results",
        )
        return super().setUp()

    def test_handle_pagination_True(self):
        path = Path(__file__).parent / f"payloads/output_handle_pagination.json"
        with open(path) as file:
            output = json.load(file)

        is_paginated = self.pagination_helper.handle_pagination(
            input_={"dry_run": False, "instance_ids": ["i-0dd117dc6df90be2e"]}, output=output
        )
        self.assertEqual(is_paginated, True)

    def test_handle_merge_responses(self):
        path = Path(__file__).parent / f"payloads/output_handle_pagination.json"
        with open(path) as file:
            output = json.load(file)

        input_ = {"max_results": 6}
        b = {"Reservations": [1, 2, 3, 4]}
        a = {"Reservations": [5, 6, 7, 8]}

        a, max_hit = self.pagination_helper.merge_responses(input_, a, b)
        self.assertEqual(a, {"Reservations": [1, 2, 3, 4, 5, 6]})
        self.assertEqual(max_hit, True)

    def test_remove_keys(self):
        self.pagination_helper.keys_to_remove = ["key1", "key2"]
        params = {"key1": 1, "key2": 2}
        self.pagination_helper.remove_keys(params)
        self.assertEqual(params, {})
