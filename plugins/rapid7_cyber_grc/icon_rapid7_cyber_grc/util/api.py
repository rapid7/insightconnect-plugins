import json
from typing import Any, Dict, List, Optional, Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

# The API returns every collection in one response, but follow @odata.nextLink if a
# future release starts server-side paging. Bounded so a paging bug cannot hang a job.
MAX_PAGES = 1000

ODATA_PREFIX = "@odata."

STATUS_CODE_ERRORS = {
    400: {
        "cause": "Bad request.",
        "assistance": "Cyber GRC rejected the request. Check any OData query options, such as Filter "
        "and Order By, against the Compyl API reference.",
        "include_data": True,
    },
    401: {
        "cause": "Unauthorized.",
        "assistance": "The API key was rejected. Verify the key is correct and has not been revoked, "
        "and that the URL points at your Cyber GRC API host.",
    },
    403: {
        "cause": "Forbidden.",
        "assistance": "The API key authenticated but is not permitted to perform this operation. "
        "An API key inherits the permissions of the user it is assigned to.",
    },
    404: {
        "cause": "Not found.",
        "assistance": "The requested record does not exist. Verify the record type and ID.",
    },
    429: {
        "cause": "Too many requests.",
        "assistance": "Cyber GRC is rate limiting this API key. Retry the workflow after a delay.",
    },
}


def clean_record(record: Any) -> Any:
    """Normalise a record body for InsightConnect.

    Two things need removing before a record can satisfy a plugin output schema. The
    API mixes @odata.* annotations into record bodies, and it returns an explicit null
    for every field a record has not set. A plugin output schema types each field, and
    the runtime validates action output against it, so a null would fail validation.
    Omitting the field instead is how InsightConnect represents a value that is unset.
    """
    if isinstance(record, dict):
        return {
            key: clean_record(value)
            for key, value in record.items()
            if value is not None and not key.startswith(ODATA_PREFIX)
        }
    if isinstance(record, list):
        return [clean_record(item) for item in record]
    return record


class CyberGrcAPI:
    def __init__(self, url: str, api_key: str, ssl_verify: bool, logger):
        self.url = url.rstrip("/")
        self.ssl_verify = ssl_verify
        self.logger = logger
        self.session = requests.Session()
        # The documented Authorization: Bearer alternative rejects cpyl_ keys on the
        # live API, so authenticate with the X-API-Key header only.
        self.session.headers.update({"X-API-Key": api_key, "Accept": "application/json"})

    # ------------------------------------------------------------------ v2 API

    def list_records(
        self,
        record_type: str,
        filter_: str = None,
        select: str = None,
        expand: str = None,
        order_by: str = None,
        top: int = None,
        skip: int = None,
    ) -> List[dict]:
        params = self._odata_params(
            {"$filter": filter_, "$select": select, "$expand": expand, "$orderby": order_by, "$top": top, "$skip": skip}
        )
        response = self._request("GET", f"/api/v2/{record_type}", params=params)
        records = self._unwrap_collection(response)

        # An explicit Top is a caller-imposed ceiling, so do not page past it.
        next_link = response.get(f"{ODATA_PREFIX}nextLink") if not top else None
        for _ in range(MAX_PAGES):
            if not next_link:
                break
            response = self._request("GET", next_link)
            records.extend(self._unwrap_collection(response))
            next_link = response.get(f"{ODATA_PREFIX}nextLink")
        else:
            self.logger.warning(
                f"Stopped paging {record_type} after the maximum of {MAX_PAGES} pages; results may be incomplete."
            )

        return records

    def count_records(self, record_type: str, filter_: str = None) -> int:
        # /$count answers with a text/plain integer rather than JSON.
        params = self._odata_params({"$filter": filter_})
        response = self._request("GET", f"/api/v2/{record_type}/$count", params=params, as_text=True)
        try:
            return int(response.strip())
        except ValueError:
            raise PluginException(
                cause="Cyber GRC returned an unexpected record count.",
                assistance="The API responded to a count request with a value that is not a number.",
                data=response,
            )

    def get_record(self, record_type: str, record_id: int, select: str = None, expand: str = None) -> dict:
        params = self._odata_params({"$select": select, "$expand": expand})
        response = self._request("GET", f"/api/v2/{record_type}/{record_id}", params=params)
        return clean_record(response)

    def create_record(self, record_type: str, record: dict, expand: str = None) -> dict:
        params = self._odata_params({"$expand": expand})
        response = self._request("POST", f"/api/v2/{record_type}", params=params, json_body=record)
        return clean_record(response)

    def update_record(self, record_type: str, record_id: int, record: dict, expand: str = None) -> dict:
        # Some record types reject a body whose id does not match the route key, so
        # supply the key the caller already gave us rather than making them repeat it.
        body = dict(record)
        body.setdefault("id", record_id)

        response = self._request(
            "PUT", f"/api/v2/{record_type}/{record_id}", params=self._odata_params({"$expand": expand}), json_body=body
        )
        if response:
            return clean_record(response)

        # A successful update answers 204 with no body, but the action promises to
        # return the updated record, so read it back.
        return self.get_record(record_type, record_id, expand=expand)

    def delete_record(self, record_type: str, record_id: int) -> dict:
        response = self._request("DELETE", f"/api/v2/{record_type}/{record_id}")
        if not response:
            # A successful delete answers 204 with no body.
            return {"success": True}
        return clean_record(response)

    def get_record_history(self, record_type: str, record_id: int) -> List[dict]:
        # The spec writes this as History(), but the OData function-call form is routed to
        # an interactive-only authentication scheme that rejects API keys.
        response = self._request("GET", f"/api/v2/{record_type}/{record_id}/History")
        return self._unwrap_collection(response)

    # ------------------------------------------------------------------ v1 API

    def upload_flat_file(
        self, file_name: str, contents: str, operation_type: str, description: str = None, record_id: int = 0
    ) -> dict:
        body = {
            "ID": record_id or 0,
            "FileName": file_name,
            "bytes": contents,
            "operationType": operation_type,
            "Description": description or "",
        }
        response = self._request("POST", "/api/flatfile-integrations", json_body=body)
        return clean_record(response) if isinstance(response, dict) else {"response": response}

    # ------------------------------------------------------------------ helpers

    @staticmethod
    def _odata_params(candidates: Dict[str, Any]) -> Dict[str, Any]:
        """Keep only the query options the caller actually set. Top of 0 means no ceiling."""
        return {key: value for key, value in candidates.items() if value not in (None, "", 0)}

    @staticmethod
    def _unwrap_collection(response: Any) -> List[dict]:
        """Collections arrive as {"@odata.context": ..., "value": [...]}."""
        if isinstance(response, dict):
            values = response.get("value", [])
        else:
            values = response
        if not isinstance(values, list):
            return []
        return [clean_record(record) for record in values]

    def _request(
        self,
        method: str,
        path: str,
        params: dict = None,
        json_body: dict = None,
        as_text: bool = False,
    ) -> Union[dict, list, str]:
        # @odata.nextLink is absolute, every other caller passes a path.
        url = path if path.startswith("http") else f"{self.url}{path}"
        try:
            response = self.session.request(
                method, url, params=params, json=json_body, verify=self.ssl_verify, timeout=120
            )
        except requests.exceptions.Timeout as error:
            raise PluginException(preset=PluginException.Preset.TIMEOUT, data=str(error))
        except requests.exceptions.SSLError as error:
            raise PluginException(
                cause="Could not verify the TLS certificate presented by the Cyber GRC API host.",
                assistance="Verify the URL is correct, or disable SSL Verify if the host uses a private certificate.",
                data=str(error),
            )
        except requests.exceptions.RequestException as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=str(error))

        if response.status_code in STATUS_CODE_ERRORS:
            error = dict(STATUS_CODE_ERRORS[response.status_code])
            include_data = error.pop("include_data", False)
            raise PluginException(**error, data=response.text if include_data else None)
        if response.status_code >= 500:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)
        if not response.ok:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response.text)

        if as_text:
            return response.text
        if not response.content:
            return {}
        try:
            return response.json()
        except json.JSONDecodeError:
            raise PluginException(preset=PluginException.Preset.INVALID_JSON, data=response.text)
