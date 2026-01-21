import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from urllib.parse import parse_qs, urlparse

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightidr.connection import Connection
from komand_rapid7_insightidr.connection.schema import Input
from requests.models import HTTPError


class Meta:
    version = "0.0.0"


class Util:
    STUB_URL_API = "https://us.api.insight.rapid7.com"
    STUB_URL_REST = "https://us.rest.logs.insight.rapid7.com"

    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.meta = Meta()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.REGION: "United States 1",
                Input.API_KEY: {"secretKey": "4472f2g7-991z-4w70-li11-7552w8qm0266"},
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    def read_file_to_dict(filename):
        with open(filename, "rt", encoding="utf8"):
            return json.loads(
                Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))
            )

    @staticmethod
    def read_file_to_string(filename):
        with open(filename, "rt", encoding="utf8") as my_file:
            return my_file.read()

    @staticmethod
    async def mocked_async_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code) -> None:
                self.filename = filename
                self.status = status_code
                self.text = "This is some error text"

            def raise_for_status(self):
                if self.status == 404:
                    raise HTTPError("Not found", response=self)

            async def json(self):
                if self.filename == "error":
                    raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
                if self.filename == "empty":
                    return {}

                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

        if args[0] == f"{Util.STUB_URL_API}/log_search/management/labels/00000000-0000-0000-0000-000000000006":
            return MockResponse("label_006", 200)
        elif args[0] == f"{Util.STUB_URL_API}/log_search/management/labels/00000000-0000-0000-0000-000000000007":
            return MockResponse("label_007", 200)
        elif args[0] == f"{Util.STUB_URL_API}/log_search/management/labels/not exist label - 404":
            return MockResponse("label_404", 404)

        raise Exception("Not implemented")

    @staticmethod
    def load_parameters(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"parameters/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code) -> None:
                self.filename = filename
                self.status_code = status_code
                self.text = "This is some error text"
                self.content = None
                if self.filename == "not_found":
                    self.text = "Not found."
                if self.filename == "download_attachment":
                    self.content = b"test"
                if self.filename in [
                    "test_search_alerts_rrns_true",
                    "test_search_alerts_rrns_false",
                    "test_search_accounts_1",
                    "test_search_accounts_2",
                    "close_investigations_in_bulk",
                    "get_a_log",
                    "create_a_threat",
                ]:
                    self.text = Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )

            def _get_params(self, url):
                parsed_url = urlparse(url)
                params = parse_qs(parsed_url.query)
                return {k: v[0] for k, v in params.items()} if params else {}

            def raise_for_status(self):
                if self.status_code == 404:
                    raise HTTPError("Not found", response=self)

            def json(self):
                if self.filename == "error":
                    raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
                if self.filename == "empty":
                    return {}

                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

        # TODO: this should be addressed and mocked properly within the test and not needing the conversion below
        # Re-build a fake args list of the urls based on the `ResourceHelper` calls this either pos 0 or pos 1
        # New logic to remove sessions remaining open passes a prepared request object and needs converted for mocking

        # First grab the request URL and kwargs from the prepared request
        req_url, kwargs = args[0].url.split("?")[0], args[0].__dict__

        # Rebuild this full URL to just the connection URL + endpoint
        parsed_url = urlparse(args[0].path_url)
        args = [req_url, req_url]
        kwargs["url"] = req_url

        # Now convert the params of the query back into a dict for comparison below
        params = parse_qs(parsed_url.query)
        kwargs["params"] = {k: v[0] for k, v in params.items()} if params else {}

        # Some tests are testing `filenames` so we need to allow for this on the body param
        content_type = kwargs.get("headers", {}).get("Content-Type", "")
        if kwargs.get("body") and "multipart/form-data" not in content_type:
            kwargs["json"] = json.loads(kwargs.get("body"))

        if kwargs.get("params") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890",
            "index": "0",
            "size": "0",
        }:
            return MockResponse("invalid_size", 400)
        if kwargs.get("params") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890",
            "index": "0",
            "size": "1",
        }:
            return MockResponse("list_comments", 200)
        if kwargs.get("params") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567899",
            "index": "0",
            "size": "1",
        }:
            return MockResponse("list_attachments", 200)
        if kwargs.get("params") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:9876543210",
            "index": "0",
            "size": "1",
        }:
            return MockResponse("list_empty", 200)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/attachments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890/metadata"
        ):
            return MockResponse("get_attachment_information", 200)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/attachments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:123456789/metadata"
        ):
            return MockResponse("get_attachment_information", 404)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/users/rrn:uba:us:934b454a-1b32-40fa-80be-7bb11cd3ccf9:user:U0NRGPV7LPFV"
        ):
            return MockResponse("get_user_information", 200)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/users/rrn:uba:us:934b454a-1b32-40fa-80be-7bb11cd3ccf9:user:123456789"
        ):
            return MockResponse("get_user_information", 404)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/assets/rrn:uba:us:934b454a-1b32-40fa-80be-7bb11cd3ccf9:asset:D6OGUBJGRVHF"
        ):
            return MockResponse("get_asset_information", 200)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/assets/rrn:uba:us:934b454a-1b32-40fa-80be-7bb11cd3ccf9:asset:123456789"
        ):
            return MockResponse("get_asset_information", 404)
        if kwargs.get("json") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890",
            "body": "test",
            "attachments": ["rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890"],
        }:
            return MockResponse("create_comment", 200)
        if kwargs.get("json") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890",
            "body": "test",
            "attachments": [],
        }:
            return MockResponse("create_comment_without_attachment", 200)
        if kwargs.get("json") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890",
            "body": "",
            "attachments": ["rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890"],
        }:
            return MockResponse("create_comment_without_body", 200)
        if kwargs.get("json") == {
            "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:not_found",
            "body": "test",
            "attachments": ["rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890"],
        }:
            return MockResponse("create_comment", 404)
        if kwargs.get("url") == "https://us.api.insight.rapid7.com/idr/v2/investigations":
            if "INVALID_SOURCE" in kwargs.get("params", {}).get("sources"):
                return MockResponse("empty", 400)
            return MockResponse("list_investigations", 200)
        if (
            kwargs.get("method") == "DELETE"
            and kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/comments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:comment:not_found"
        ):
            return MockResponse("not_found", 404)
        if (
            kwargs.get("method") == "DELETE"
            and kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/attachments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:comment:not_found"
        ):
            return MockResponse("not_found", 404)
        if kwargs.get("method") == "DELETE":
            return MockResponse("success", 204)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/attachments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890"
        ):
            return MockResponse("download_attachment", 200)
        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/attachments/rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:not_found"
        ):
            return MockResponse("not_found", 404)
        if 'filename="test.txt"' in str(kwargs.get("body", "")):
            return MockResponse("upload_attachment", 200)
        if 'filename="test"' in str(kwargs.get("body", "")):
            return MockResponse("upload_attachment_without_file_extension", 200)

        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/at/alerts/rrn:alerts:us1:cf946362-0809-426d-987c-849bde704c16:alert:1:1c961b2402751096126c72ca3e07d7d6/actors"
        ):
            return MockResponse("test_get_alert_actors_minimum", 200)

        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/at/alerts/rrn:alerts:us1:cf946362-0809-426d-987c-849bde704c16:alert:1:1c961b2402751096126c72ca3e07d7d7/actors"
        ):
            return MockResponse("not_found", 404)

        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/at/alerts/rrn:alerts:us1:cf946362-0809-426d-987c-849bde704c16:alert:1:1c961b2402751096126c72ca3e07d7d6/evidences"
        ):
            return MockResponse("test_get_alert_evidence_minimum", 200)

        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/at/alerts/rrn:alerts:us1:cf946362-0809-426d-987c-849bde704c16:alert:1:1c961b2402751096126c72ca3e07d7d7/evidences"
        ):
            return MockResponse("not_found", 404)

        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/at/alerts/rrn:alerts:us1:cf946362-0809-426d-987c-849bde704c16:alert:1:1c961b2402751096126c72ca3e07d7d6"
        ):
            return MockResponse("test_get_alert_information", 200)

        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/at/alerts/rrn:alerts:us1:cf946362-0809-426d-987c-849bde704c16:alert:1:1c961b2402751096126c72ca3e07d7d7"
        ):
            return MockResponse("not_found", 404)

        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/accounts/rrn:uba:us:cf946362-0809-426d-987c-849bde704c16:account:00875N0IK0RJ"
        ):
            return MockResponse("test_get_account_by_rrn", 200)

        if (
            kwargs.get("url")
            == "https://us.api.insight.rapid7.com/idr/v1/accounts/rrn:uba:us:cf946362-0809-426d-987c-849bde704c16:account:123456789"
        ):
            return MockResponse("not_found", 404)

        if args[0] == f"{Util.STUB_URL_API}/log_search/management/logs":
            return MockResponse("logs", 200)
        elif (
            args[0] == f"{Util.STUB_URL_API}/log_search/query/logs/log_id"
            or args[0] == f"{Util.STUB_URL_API}/log_search/query/logsets/log_id"
            or args[0] == f"{Util.STUB_URL_API}/log_search/query/logs/123456-abcd-1234-abcd-123456abc"
        ):
            return MockResponse("log_id", 200)
        elif (
            args[0] == f"{Util.STUB_URL_API}/log_search/query/logs/log_id2"
            or args[0] == f"{Util.STUB_URL_API}/log_search/query/logsets/log_id2"
        ):
            return MockResponse("log_id2", 200)
        elif (
            args[0] == f"{Util.STUB_URL_API}/log_search/query/logs/log_id3"
            or args[0] == f"{Util.STUB_URL_API}/log_search/query/logsets/log_id3"
        ):
            return MockResponse("log_id3", 200)
        elif (
            args[0] == f"{Util.STUB_URL_API}/log_search/query/logs/log_id4"
            or args[0] == f"{Util.STUB_URL_API}/log_search/query/logsets/log_id4"
        ):
            return MockResponse("log_id4", 200)
        elif args[0] == f"{Util.STUB_URL_API}/log_search/management/logsets":
            return MockResponse("logsets", 200)

        elif (
            args[0] == f"{Util.STUB_URL_API}/log_search/query/logs/log_id5"
            or args[0] == f"{Util.STUB_URL_API}/log_search/query/logsets/log_id5"
        ):
            return MockResponse("log_id5", 200)

        elif (
            args[0] == f"{Util.STUB_URL_API}/log_search/query/logs/log_id7"
            or args[0] == f"{Util.STUB_URL_API}/log_search/query/logsets/log_id7"
        ):
            return MockResponse("log_id7", 200)

        if (
            args[0]
            == "https://us.api.insight.rapid7.com/log_search/query/7176face-f659-45a6-bd46-81fdc2b1f74b:1:85f959aecc0a7300f9ad93ddacf3454e36348348::bafefd2e9cf60c699529d5a8cf4493578b0b56dd:"
        ):
            return MockResponse("log_id6", 200)

        if (
            args[0]
            == "https://us.api.insight.rapid7.com/log_search/query/b55a768a-4c0e-449a-84ae-adc70e18eb20:1:8956245765c23b46f1d20322e5c076e53a7ab662::d56c37ab761ff5e65950abd93476f02ffbcb5a45:"
        ):
            return MockResponse("log_id8", 200)

        if args[1] == "https://us.api.insight.rapid7.com/idr/at/alerts/ops/search":
            if kwargs.get("params", {}).get("rrns_only") == "True":
                return MockResponse("test_search_alerts_rrns_true", 200)
            else:
                return MockResponse("test_search_alerts_rrns_false", 200)

        if args[1] == "https://us.api.insight.rapid7.com/idr/v1/accounts/_search":
            if kwargs.get("params", {}).get("size") == "1":
                return MockResponse("test_search_accounts_1", 200)
            elif kwargs.get("params", {}).get("size") == "2":
                return MockResponse("test_search_accounts_2", 200)
        if args[1] == "https://us.api.insight.rapid7.com/log_search/management/logs/test_id":
            return MockResponse("get_a_log", 200)
        if args[1] == "https://us.api.insight.rapid7.com/idr/v1/customthreats":
            return MockResponse("create_a_threat", 200)
        if args[1] == "https://us.api.insight.rapid7.com/idr/v1/investigations/bulk_close":
            return MockResponse("close_investigations_in_bulk", 200)

        raise Exception("Not implemented")
