import os
import sys

from icon_azure_sentinel.util.endpoints import Endpoint

sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase, mock

from icon_azure_sentinel.util.helpers import AzureSentinelClient
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized
from unit_test.mock import mock_request_200, mock_request_408, mock_request_500

FAKE_AZURE_URL = "https://fake.azure.com"


class TestClient(TestCase):
    def setUp(self) -> None:
        self.client = AzureSentinelClient("12345", "2022-01-01", "123-123-123")

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test__call_api_ok(self, mock_get):
        url = "https://fake.azure.com"
        payload = {"fake": "data"}
        response = self.client._call_api("POST", url, headers=self.client.headers, payload=payload)
        self.assertEqual(response["fake_data"], "1234")

    @parameterized.expand(
        [
            (mock_request_500, PluginException(cause="HTTP Error"), FAKE_AZURE_URL),
            (mock_request_408, PluginException(cause="Timeout error"), FAKE_AZURE_URL),
            (mock_request_200, PluginException.Preset.INVALID_JSON, FAKE_AZURE_URL + "/invalid"),
        ],
    )
    def test__call_api_raises(self, mock_request, exception, url):
        payload = {"fake": "payload"}
        with self.assertRaises(PluginException) as ctx:
            self.client._call_api("POST", url, headers=self.client.headers, payload=payload)
            self.assertEqual(
                ctx.exception.cause,
                exception.cause,
            )

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_create_incident(self, mock_get):
        payload = {
            "properties": {
                "lastActivityTimeUtc": "2019-01-01T13:05:30Z",
                "firstActivityTimeUtc": "2019-01-01T13:00:30Z",
                "description": "This is a demo incident",
                "title": "Test incident",
                "severity": "Low",
                "classification": "FalsePositive",
                "classificationComment": "Not a malicious activity",
                "classificationReason": "IncorrectAlertLogic",
                "status": "Closed",
            }
        }
        incident_id = "incident1"
        group = "group1"
        workspace = "workspace1"
        self.client.create_incident(incident_id, group, workspace, **payload)
        result_url = Endpoint.CREATEINCIDENT.format(
            self.client.subscription_id,
            group,
            workspace,
            incident_id,
            self.client.api_version,
        )

        mock_get.assert_called_once_with("PUT", result_url, self.client.headers, payload=payload)

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_get_incident(self, mock_get):
        incident_id = "incident1"
        group = "group1"
        workspace = "workspace1"
        self.client.get_incident(incident_id, group, workspace)
        result_url = Endpoint.GETINCIDENT.format(
            self.client.subscription_id,
            group,
            workspace,
            incident_id,
            self.client.api_version,
        )

        mock_get.assert_called_once_with("GET", result_url, self.client.headers)

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_delete_incident(self, mock_get):
        incident_id = "incident1"
        group = "group1"
        workspace = "workspace1"
        self.client.delete_incident(incident_id, group, workspace)
        result_url = Endpoint.DELETEINCIDENT.format(
            self.client.subscription_id,
            group,
            workspace,
            incident_id,
            self.client.api_version,
        )

        mock_get.assert_called_once_with("DELETE", result_url, self.client.headers)

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_list_incident(self, mock_get):
        mock_get.side_effect = [{"nextLink": "1234"}, {}]
        group = "group1"
        workspace = "workspace1"
        mock_get.return_value = {}
        self.client.list_incident(group, workspace, {"top": 3})
        result_url = (
            Endpoint.LISTINCIDENTS.format(
                self.client.subscription_id,
                group,
                workspace,
                self.client.api_version,
            )
            + "&$top=3"
        )

        mock_get.assert_has_calls(
            [
                mock.call("GET", result_url, self.client.headers),
                mock.call("GET", "1234", self.client.headers),
            ]
        )

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_list_bookmarks(self, mock_get):
        group = "group1"
        incident_id = "incident1"
        workspace = "workspace1"
        mock_get.return_value = {}
        self.client.list_bookmarks(incident_id, group, workspace)
        result_url = (
            Endpoint.LISTBOOKMARKS.format(
                self.client.subscription_id,
                group,
                workspace,
                incident_id,
                self.client.api_version,
            )
        )

        mock_get.assert_has_calls(
            [
                mock.call("POST", result_url, self.client.headers),
            ]
        )

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_list_alerts(self, mock_get):
        group = "group1"
        incident_id = "incident1"
        workspace = "workspace1"
        mock_get.return_value = {}
        self.client.list_alerts(incident_id, group, workspace)
        result_url = (
            Endpoint.LISTALERTS.format(
                self.client.subscription_id,
                group,
                workspace,
                incident_id,
                self.client.api_version,
            )
        )

        mock_get.assert_has_calls(
            [
                mock.call("POST", result_url, self.client.headers),
            ]
        )

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_list_entities(self, mock_get):
        mock_get.return_value = {}
        group = "group1"
        incident_id = "incident1"
        workspace = "workspace1"
        self.client.list_entities(incident_id, group, workspace)
        result_url = (
            Endpoint.LISTENTITIES.format(
                self.client.subscription_id,
                group,
                workspace,
                incident_id,
                self.client.api_version,
            )
        )

        mock_get.assert_has_calls(
            [
                mock.call("POST", result_url, self.client.headers),
            ]
        )
