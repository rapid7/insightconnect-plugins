import uuid

import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

# Custom imports below
import requests
from typing import Optional
from komand_rapid7_insightidr.util.endpoints import Investigations
from komand_rapid7_insightidr.util.util import get_logging_context


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.url = None
        self.session: Optional[requests.Session] = None
        self.cloud_log_values = {}

    def connect(self, params={}):
        api_key = params.get(Input.API_KEY).get("secretKey")
        cloud_request_id = get_logging_context()
        request_uuid = str(uuid.uuid4())
        if cloud_req_id := cloud_request_id.get("R7-Correlation-Id"):
            request_uuid = cloud_req_id
            self.cloud_log_values = cloud_request_id

        self.region = params.get(Input.REGION)
        self.url = Investigations.connection_api_url(self.region)

        if not self.url.endswith("/"):
            self.url = f"{self.url}/"

        self.session = requests.session()
        self.session.headers["X-Api-Key"] = api_key
        self.session.headers["Accept-version"] = "investigations-preview"

        self.session.headers["R7-Correlation-Id"] = request_uuid
        try:
            self.session.headers["User-Agent"] = f"r7:insightconnect-insightidr-plugin/{self.meta.version}"
        except AttributeError:
            self.session.headers["User-Agent"] = "test-version"
        self.logger.info(f"Connect: Connecting...", **self.cloud_log_values)
        self.logger.info(f"Request ID: {request_uuid}", **self.cloud_log_values)

    def test(self):
        response = self.session.get(f"{self.url}validate")
        if response.status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED)
        if response.status_code in range(500, 599):
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        if response.status_code == 200:
            return response.json()
        else:
            self.logger.error(response.text, **self.connection.cloud_log_values)
            raise ConnectionTestException(
                cause=f"An unknown error occurred." f" InsightIDR responded with a {response.status_code} code.",
                assistance="See log for more details. If the problem persists, please contact support.",
            )
