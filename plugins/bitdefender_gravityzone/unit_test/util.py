import json
import logging
import os
from typing import Any, Callable, Dict, List, Optional, Tuple

import requests

from icon_bitdefender_gravityzone.connection.connection import Connection
from icon_bitdefender_gravityzone.connection.schema import Input

STUB_URL = "https://cloud.gravityzone.bitdefender.com"
STUB_API_KEY = "9de5069c5afe602b2ea0a04b66beb2c0"
NETWORK_URL = f"{STUB_URL}/api/v1.0/jsonrpc/network"
INCIDENTS_URL = f"{STUB_URL}/api/v1.0/jsonrpc/incidents"


class Util:
    @staticmethod
    def default_connector(action: Any, url: str = STUB_URL) -> Any:
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        default_connection.connect({Input.URL: url, Input.API_KEY: {"secretKey": STUB_API_KEY}})
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_dict(filename: str) -> Dict[str, Any]:
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "payloads", filename)
        with open(path, encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def response(
        status_code: int = 200,
        body: Any = None,
        text: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> requests.Response:
        """Build a real requests.Response, so status checks and JSON parsing run as they do in production."""
        response = requests.Response()
        response.status_code = status_code
        response._content = (text if text is not None else json.dumps(body)).encode("utf-8")
        response.encoding = "utf-8"
        response.headers.update(headers or {})
        return response

    @staticmethod
    def payload_response(filename: str) -> requests.Response:
        return Util.response(body=Util.read_file_to_dict(filename))

    @staticmethod
    def rpc_result(result: Any) -> requests.Response:
        return Util.response(body={"id": "1", "jsonrpc": "2.0", "result": result})

    @staticmethod
    def rpc_error(code: int, message: str, details: str = "") -> requests.Response:
        error = {"code": code, "message": message, "data": {"details": details}}
        return Util.response(body={"id": "1", "jsonrpc": "2.0", "error": error})

    @staticmethod
    def endpoints_page(items: List[Dict[str, Any]], page: int = 1, pages_count: Optional[int] = 1) -> requests.Response:
        result = {"page": page, "perPage": 100, "total": len(items), "items": items}
        if pages_count is not None:
            result["pagesCount"] = pages_count
        return Util.rpc_result(result)

    @staticmethod
    def endpoints_by_name_filter(
        pages_by_name_filter: Dict[str, List[List[Dict[str, Any]]]], with_pages_count: bool = True
    ) -> Callable[..., requests.Response]:
        """
        Return a Session.send side effect that answers getEndpointsList with the pages listed for the exact
        details.name value of each request, the way a case-sensitive server would. Other names get an empty page.
        """

        def send(request: requests.PreparedRequest, **kwargs: Any) -> requests.Response:
            params = json.loads(request.body)["params"]
            pages = pages_by_name_filter.get(params["filters"]["details"]["name"], [[]])
            page = params["page"]
            items = pages[page - 1] if page <= len(pages) else []
            return Util.endpoints_page(items, page=page, pages_count=len(pages) if with_pages_count else None)

        return send

    @staticmethod
    def sent_name_filters(mock_send: Any) -> List[Tuple[str, int]]:
        """Return the (details.name, page) pair of every getEndpointsList request, in order"""
        payloads = [Util.sent_payload(mock_send, index) for index in range(mock_send.call_count)]
        return [(payload["params"]["filters"]["details"]["name"], payload["params"]["page"]) for payload in payloads]

    @staticmethod
    def endpoint(endpoint_id: str, name: str, fqdn: Optional[str] = None, is_isolated: bool = False) -> Dict[str, Any]:
        return {
            "id": endpoint_id,
            "name": name,
            "fqdn": fqdn,
            "ip": "10.0.0.15",
            "macs": ["00:1a:2b:3c:4d:5e"],
            "isManaged": True,
            "isIsolated": is_isolated,
        }

    @staticmethod
    def sent_request(mock_send: Any, call_index: int = 0) -> requests.PreparedRequest:
        """Return the request that was handed to Session.send"""
        return mock_send.call_args_list[call_index][0][0]

    @staticmethod
    def sent_payload(mock_send: Any, call_index: int = 0) -> Dict[str, Any]:
        """Return the JSON-RPC body of the request that was handed to Session.send"""
        return json.loads(Util.sent_request(mock_send, call_index).body)
