import json
import logging
from typing import Any, Optional

from icon_halo_itsm.connection.connection import Connection
from icon_halo_itsm.util.api import HaloItsmApi

BASE_URL = "https://example.haloitsm.com"
LOGGER_NAME = "halo_itsm_test"

RAW_TICKET = {
    "id": 101,
    "summary": "Server is unresponsive",
    "details": "The production server has been unresponsive since 10:00 AM",
    "status_id": 1,
    "priority_id": 3,
    "tickettype_id": 1,
    "client_name": "ACME Corp",
    "datecreated": "2025-07-10T10:05:00Z",
    "lastupdate": None,
    "not_in_the_output_schema": "dropped",
}

CLEAN_TICKET = {
    "id": 101,
    "summary": "Server is unresponsive",
    "details": "The production server has been unresponsive since 10:00 AM",
    "status_id": 1,
    "priority_id": 3,
    "tickettype_id": 1,
    "client_name": "ACME Corp",
    "datecreated": "2025-07-10T10:05:00Z",
}


class MockResponse:
    def __init__(self, status_code: int = 200, json_data: Any = None, text: Optional[str] = None) -> None:
        self.status_code = status_code
        self._json_data = json_data
        if text is not None:
            self.text = text
        else:
            self.text = "" if json_data is None else json.dumps(json_data)

    def json(self) -> Any:
        if self._json_data is None:
            raise ValueError("Response has no JSON body")
        return self._json_data


def token_response() -> MockResponse:
    return MockResponse(200, {"access_token": "token-value", "token_type": "Bearer"})


class Util:
    @staticmethod
    def default_connector(action: Any, tenant: str = "") -> Any:
        logger = logging.getLogger(LOGGER_NAME)
        connection = Connection()
        connection.logger = logger
        connection.client = HaloItsmApi(
            base_url=BASE_URL, client_id="client-id", client_secret="client-secret", tenant=tenant, logger=logger
        )
        action.connection = connection
        action.logger = logger
        return action
