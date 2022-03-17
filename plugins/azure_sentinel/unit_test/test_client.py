import os
import sys

from icon_azure_sentinel.util.endpoints import Endpoint

sys.path.append(os.path.abspath("../"))
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

import logging
from icon_azure_sentinel.util.api import AzureClient, AzureSentinelClient
from unit_test.mock import mock_request_200, mock_request_408, mock_request_500

FAKE_AZURE_URL = "https://fake.azure.com"

logger = logging.getLogger(__name__)


@mock.patch.object(AzureSentinelClient, "__init__", lambda x, y, z, w, v: None)
class TestClient(TestCase):
    @mock.patch("requests.request", side_effect=mock_request_200)
    def test__call_api_ok(self, mock_get):
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        url = "https://fake.azure.com"
        payload = {"fake": "data"}
        response = self.client._call_api("POST", url, headers=self.client.headers, payload=payload)
        self.assertEqual(response[1]["fake_data"], "1234")

    @parameterized.expand(
        [
            (mock_request_500, PluginException(cause="HTTP Error"), FAKE_AZURE_URL),
            (mock_request_408, PluginException(cause="Timeout error"), FAKE_AZURE_URL),
            (mock_request_200, PluginException.Preset.INVALID_JSON, FAKE_AZURE_URL + "/invalid"),
        ],
    )
    def test__call_api_raises(self, mock_request, exception, url):
        payload = {"fake": "payload"}
        with mock.patch.object(AzureSentinelClient, "__init__", lambda x, y, z, w, v: None):
            with self.assertRaises(PluginException) as ctx:
                with mock.patch("requests.request", mock_request):
                    self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
                    self.client.headers = {"content-type": "application/json; charset=utf-8"}
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
        subscription_id = "123-123-123"
        api_version = "2021-04-01"
        mock_get.return_value = (200, {})
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        self.client.create_incident(incident_id, group, workspace, subscription_id, **payload)
        result_url = Endpoint.CREATEINCIDENT.format(subscription_id, group, workspace, incident_id, api_version)

        mock_get.assert_called_once_with("PUT", result_url, self.client.headers, payload=payload)

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_get_incident(self, mock_get):
        incident_id = "incident1"
        group = "group1"
        workspace = "workspace1"
        subscription_id = "1234"
        mock_get.return_value = (200, {})
        api_version = "2021-04-01"
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        self.client.get_incident(incident_id, group, workspace, subscription_id)
        result_url = Endpoint.GETINCIDENT.format(
            subscription_id,
            group,
            workspace,
            incident_id,
            api_version,
        )
        mock_get.assert_called_once_with("GET", result_url, self.client.headers)

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_delete_incident(self, mock_get):
        incident_id = "incident1"
        group = "group1"
        workspace = "workspace1"
        subscription_id = "1234"
        api_version = "2021-04-01"
        mock_get.return_value = (204, {})
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        self.client.delete_incident(incident_id, group, workspace, subscription_id)
        result_url = Endpoint.DELETEINCIDENT.format(
            subscription_id,
            group,
            workspace,
            incident_id,
            api_version,
        )

        mock_get.assert_called_once_with("DELETE", result_url, self.client.headers)

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_list_incident(self, mock_get):
        mock_get.side_effect = [(200, {})]
        group = "group1"
        workspace = "workspace1"
        subscription_id = "1234"
        api_version = "2021-04-01"
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.logger = logger
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        self.client.list_incident(group, workspace, {}, subscription_id)
        result_url = Endpoint.LISTINCIDENTS.format(subscription_id, group, workspace, api_version)

        mock_get.assert_has_calls(
            [
                mock.call("GET", result_url, self.client.headers, params={}),
            ]
        )

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_list_bookmarks(self, mock_get):
        group = "group1"
        incident_id = "incident1"
        workspace = "workspace1"
        subscription_id = "1234"
        mock_get.return_value = (204, {})
        api_version = "2021-04-01"
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        self.client.logger = logger
        self.client.list_bookmarks(incident_id, group, workspace, subscription_id)
        result_url = Endpoint.LISTBOOKMARKS.format(
            subscription_id,
            group,
            workspace,
            incident_id,
            api_version,
        )
        mock_get.assert_has_calls(
            [
                mock.call("POST", result_url, self.client.headers, params={}),
            ]
        )

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_list_alerts(self, mock_get):
        group = "group1"
        incident_id = "incident1"
        workspace = "workspace1"
        subscription_id = "1234"
        mock_get.return_value = (204, {})
        api_version = "2021-04-01"
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.logger = logger
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        self.client.list_alerts(incident_id, group, workspace, subscription_id)
        result_url = Endpoint.LISTALERTS.format(
            subscription_id,
            group,
            workspace,
            incident_id,
            api_version,
        )

        mock_get.assert_has_calls(
            [
                mock.call("POST", result_url, self.client.headers, params={}),
            ]
        )

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_list_entities(self, mock_get):
        mock_get.return_value = {}
        group = "group1"
        incident_id = "incident1"
        workspace = "workspace1"
        subscription_id = "1234"
        mock_get.return_value = (204, {})
        api_version = "2021-04-01"
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        self.client.logger = logger
        self.client.list_entities(incident_id, group, workspace, subscription_id)
        result_url = Endpoint.LISTENTITIES.format(
            subscription_id,
            group,
            workspace,
            incident_id,
            api_version,
        )

        mock_get.assert_has_calls(
            [
                mock.call("POST", result_url, self.client.headers, params={}),
            ]
        )

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_get_comment(self, mock_get):
        incident_comment_id = "comment1"
        incident_id = "incident1"
        group = "group1"
        workspace = "workspace1"
        subscription_id = "1234"
        mock_get.return_value = (200, {})
        api_version = "2021-04-01"
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        self.client.get_comment(incident_id, incident_comment_id, group, workspace, subscription_id)
        result_url = Endpoint.GETCOMMENT.format(
            subscription_id,
            group,
            workspace,
            incident_id,
            incident_comment_id,
            api_version,
        )
        mock_get.assert_called_once_with("GET", result_url, self.client.headers)

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_list_entities(self, mock_get):
        mock_get.return_value = {}
        group = "group1"
        incident_id = "incident1"
        workspace = "workspace1"
        subscription_id = "1234"
        mock_get.return_value = (204, {})
        api_version = "2021-04-01"
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        self.client.logger = logger
        self.client.list_comments(incident_id, group, workspace, subscription_id)
        result_url = Endpoint.LISTCOMMENTS.format(
            subscription_id,
            group,
            workspace,
            incident_id,
            api_version,
        )

        mock_get.assert_has_calls(
            [
                mock.call("GET", result_url, self.client.headers, params={}),
            ]
        )

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_create_update_incident(self, mock_get):
        payload = {
            "properties": {
                "message": "Gallia est omnis divisa in partes tres, quarum unam incolunt Belgae, aliam Aquitani, tertiam qui ipsorum lingua Celtae, nostra Galli appellantur."
            }
        }
        incident_id = "incident1"
        incident_comment_id = "comment1"
        group = "group1"
        workspace = "workspace1"
        subscription_id = "123-123-123"
        api_version = "2021-04-01"
        mock_get.return_value = (200, {})
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        self.client.create_update_comment(
            incident_id, incident_comment_id, group, workspace, subscription_id, **payload
        )
        result_url = Endpoint.CREATEUPDATECOMMENT.format(
            subscription_id, group, workspace, incident_id, incident_comment_id, api_version
        )

        mock_get.assert_called_once_with("PUT", result_url, headers=self.client.headers, payload=payload)

    @mock.patch(__name__ + ".AzureSentinelClient._call_api")
    def test_delete_comment(self, mock_get):
        incident_comment_id = "comment1"
        incident_id = "incident1"
        group = "group1"
        workspace = "workspace1"
        subscription_id = "1234"
        mock_get.return_value = (200, {})
        api_version = "2021-04-01"
        self.client = AzureSentinelClient(logger, "12345", "123-123-123", "secret")
        self.client.headers = {"content-type": "application/json; charset=utf-8"}
        self.client.delete_comment(incident_id, incident_comment_id, group, workspace, subscription_id)
        result_url = Endpoint.DELETECOMMENT.format(
            subscription_id,
            group,
            workspace,
            incident_id,
            incident_comment_id,
            api_version,
        )
        mock_get.assert_called_once_with("DELETE", result_url, self.client.headers)
