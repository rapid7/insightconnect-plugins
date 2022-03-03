import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.activities_list import ActivitiesList
from komand_sentinelone.actions.activities_list.schema import Input
from unit_test.util import Util
from unittest import TestCase


class TestActivitiesList(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(
            ActivitiesList(),
            {"url": "https://rapid7.com", "credentials": {"username": "params", "password": "password"}},
        )
        Util.mock_response_params = {}

    def setUp(self) -> None:
        Util.mock_response_params = {}

    @patch("requests.post", side_effect=Util.mocked_requests_get)
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_without_inputs(self, mock_request, mock_request_post):
        actual = Util.default_connector(ActivitiesList()).run()
        expected = {
            "data": [
                {
                    "accountId": "433241117337583618",
                    "accountName": "SentinelOne",
                    "activityType": 19,
                    "agentId": "901345720792880606",
                    "createdAt": "2020-12-17T22:39:24.305435Z",
                    "data": {
                        "accountName": "SentinelOne",
                        "computerName": "so-agent-win12",
                        "confidenceLevel": "malicious",
                        "fileContentHash": "a2138f21ea96d97ce00cd51971696f7464e5db89",
                        "fileDisplayName": "test.txt",
                        "filePath": "\\Device\\HarddiskVolume2\\Users\\Administrator\\Desktop\\test.txt",
                        "groupName": "Default Group",
                        "siteName": "Rapid7",
                        "threatClassification": "Trojan",
                        "threatClassificationSource": "Cloud",
                        "username": None,
                    },
                    "groupId": "521580416411822676",
                    "groupName": "Default Group",
                    "id": "1048709918296672060",
                    "primaryDescription": "Threat with confidence level malicious " "detected: test.txt",
                    "secondaryDescription": "a2138f21ea96d97ce00cd51971696f7464e5db89",
                    "siteId": "521580416395045459",
                    "siteName": "Rapid7",
                    "threatId": "1048709918179231544",
                    "updatedAt": "2020-12-17T22:39:24.299235Z",
                },
                {
                    "accountId": "433241117337583618",
                    "accountName": "SentinelOne",
                    "activityType": 2001,
                    "agentId": "901345720792880606",
                    "createdAt": "2020-12-17T22:39:24.423814Z",
                    "data": {
                        "accountName": "SentinelOne",
                        "computerName": "so-agent-win12",
                        "fileContentHash": "a2138f21ea96d97ce00cd51971696f7464e5db89",
                        "fileDisplayName": "test.txt",
                        "filePath": "\\Device\\HarddiskVolume2\\Users\\Administrator\\Desktop\\test.txt",
                        "fullScopeDetails": "Group Default Group in Site Rapid7 of " "Account SentinelOne",
                        "globalStatus": "success",
                        "groupName": "Default Group",
                        "scopeLevel": "Group",
                        "scopeName": "Default Group",
                        "siteName": "Rapid7",
                        "threatClassification": "Trojan",
                        "threatClassificationSource": "Cloud",
                    },
                    "groupId": "521580416411822676",
                    "groupName": "Default Group",
                    "id": "1048709919294916416",
                    "primaryDescription": "The agent so-agent-win12 successfully killed " "the threat: test.txt.",
                    "secondaryDescription": "\\Device\\HarddiskVolume2\\Users\\Administrator\\Desktop\\test.txt",
                    "siteId": "521580416395045459",
                    "siteName": "Rapid7",
                    "threatId": "1048709918179231544",
                    "updatedAt": "2020-12-17T22:39:24.419607Z",
                },
            ]
        }
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_with_inputs(self, mock_request):
        for test in [
            {"in": Input.LIMIT, "val": 2, "out": "limit", "outVal": 2},
            {"in": Input.LIMIT, "val": 0, "out": "limit", "outVal": 0},
            {"in": Input.LIMIT, "val": -2, "out": "limit", "outVal": -2},
            {"in": Input.IDS, "val": [], "out": "ids", "outVal": None},
            {"in": Input.IDS, "val": ["1"], "out": "ids", "outVal": "1"},
            {"in": Input.IDS, "val": ["1", "2", "3"], "out": "ids", "outVal": "1,2,3"},
            {"in": Input.SKIP, "val": 0, "out": "skip", "outVal": 0},
            {"in": Input.SKIP, "val": 2, "out": "skip", "outVal": 2},
            {"in": Input.SKIP, "val": -2, "out": "skip", "outVal": -2},
            {"in": Input.SKIP_COUNT, "val": 0, "out": "skipCount", "outVal": 0},
            {"in": Input.SKIP_COUNT, "val": 2, "out": "skipCount", "outVal": 2},
            {"in": Input.SKIP_COUNT, "val": -2, "out": "skipCount", "outVal": -2},
            {"in": Input.COUNT_ONLY, "val": True, "out": "countOnly", "outVal": True},
            {"in": Input.COUNT_ONLY, "val": True, "out": "countOnly", "outVal": True},
            {"in": Input.ACCOUNT_IDS, "val": [], "out": "accountIds", "outVal": None},
            {"in": Input.ACCOUNT_IDS, "val": ["1"], "out": "accountIds", "outVal": "1"},
            {"in": Input.ACCOUNT_IDS, "val": ["1", "2", "3"], "out": "accountIds", "outVal": "1,2,3"},
            {"in": Input.ACTIVITY_TYPES, "val": [], "out": "activityTypes", "outVal": None},
            {"in": Input.ACTIVITY_TYPES, "val": ["activity1"], "out": "activityTypes", "outVal": "activity1"},
            {
                "in": Input.ACTIVITY_TYPES,
                "val": ["activity1", "activity2", "activity1"],
                "out": "activityTypes",
                "outVal": "activity1,activity2,activity1",
            },
            {"in": Input.AGENT_IDS, "val": [], "out": "agentIds", "outVal": None},
            {"in": Input.AGENT_IDS, "val": ["1"], "out": "agentIds", "outVal": "1"},
            {"in": Input.AGENT_IDS, "val": ["1", "2", "3"], "out": "agentIds", "outVal": "1,2,3"},
            {"in": Input.CREATED_AT_BETWEEN, "val": "", "out": "createdAt__between", "outVal": None},
            {
                "in": Input.CREATED_AT_BETWEEN,
                "val": "1514978764288-1514978999999",
                "out": "createdAt__between",
                "outVal": "1514978764288-1514978999999",
            },
            {"in": Input.CREATED_AT_GT, "val": "", "out": "createdAt__gt", "outVal": None},
            {"in": Input.CREATED_AT_GT, "val": "1514978764288", "out": "createdAt__gt", "outVal": "1514978764288"},
            {"in": Input.CREATED_AT_GTE, "val": "", "out": "createdAt__gte", "outVal": None},
            {"in": Input.CREATED_AT_GTE, "val": "1514978764288", "out": "createdAt__gte", "outVal": "1514978764288"},
            {"in": Input.CREATED_AT_LT, "val": "", "out": "createdAt__lt", "outVal": None},
            {"in": Input.CREATED_AT_LT, "val": "1514978764288", "out": "createdAt__lt", "outVal": "1514978764288"},
            {"in": Input.CREATED_AT_LTE, "val": "", "out": "createdAt__lte", "outVal": None},
            {"in": Input.CREATED_AT_LTE, "val": "1514978764288", "out": "createdAt__lte", "outVal": "1514978764288"},
            {"in": Input.GROUP_IDS, "val": [], "out": "groupIds", "outVal": None},
            {"in": Input.GROUP_IDS, "val": ["1"], "out": "groupIds", "outVal": "1"},
            {"in": Input.GROUP_IDS, "val": ["1", "2", "3"], "out": "groupIds", "outVal": "1,2,3"},
            {"in": Input.INCLUDE_HIDDEN, "val": False, "out": "includeHidden", "outVal": False},
            {"in": Input.INCLUDE_HIDDEN, "val": True, "out": "includeHidden", "outVal": True},
            {"in": Input.SITE_IDS, "val": [], "out": "siteIds", "outVal": None},
            {"in": Input.SITE_IDS, "val": ["1"], "out": "siteIds", "outVal": "1"},
            {"in": Input.SITE_IDS, "val": ["1", "2", "3"], "out": "siteIds", "outVal": "1,2,3"},
            {"in": Input.SORT_BY, "val": "id", "out": "sortBy", "outVal": "id"},
            {"in": Input.SORT_BY, "val": "activityType", "out": "sortBy", "outVal": "activityType"},
            {"in": Input.SORT_BY, "val": "createdAt", "out": "sortBy", "outVal": "createdAt"},
            {"in": Input.SORT_ORDER, "val": "asc", "out": "sortOrder", "outVal": "asc"},
            {"in": Input.SORT_ORDER, "val": "desc", "out": "sortOrder", "outVal": "desc"},
            {"in": Input.THREAT_IDS, "val": [], "out": "threatIds", "outVal": None},
            {"in": Input.THREAT_IDS, "val": ["1"], "out": "threatIds", "outVal": "1"},
            {"in": Input.THREAT_IDS, "val": ["1", "2", "3"], "out": "threatIds", "outVal": "1,2,3"},
            {"in": Input.USER_EMAILS, "val": [], "out": "userEmails", "outVal": None},
            {"in": Input.USER_EMAILS, "val": ["user@example.com"], "out": "userEmails", "outVal": "user@example.com"},
            {
                "in": Input.USER_EMAILS,
                "val": ["user@example.com", "user2@example.com"],
                "out": "userEmails",
                "outVal": "user@example.com,user2@example.com",
            },
            {"in": Input.USER_IDS, "val": [], "out": "userIds", "outVal": None},
            {"in": Input.USER_IDS, "val": ["1"], "out": "userIds", "outVal": "1"},
            {"in": Input.USER_IDS, "val": ["1", "2"], "out": "userIds", "outVal": "1,2"},
        ]:
            with self.subTest(f"Running activites list with parameter: {test['in']} and value: {test['val']}"):
                self.action.run({test["in"]: test["val"]})
                self.assertEqual(test["outVal"], Util.mock_response_params.get("kwargs").get("params").get(test["out"]))
