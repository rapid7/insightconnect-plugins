import json
from typing import Any, Dict, List, Optional, Tuple, Union

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

# The API returns every collection in one response, but follow @odata.nextLink if a
# future release starts server-side paging. Bounded so a paging bug cannot hang a job.
MAX_PAGES = 1000

# The API pages collections at 100 records and rejects a larger $top outright, so a
# bigger ceiling has to be honoured client side.
PAGE_LIMIT = 100

ODATA_PREFIX = "@odata."

# The URL of the API host, which is not the URL of the web interface users log in to.
API_HOST_PATTERN = "https://app-<tenant>-<brand>-<region>-api-01.azurewebsites.net"

# How much of an unexpected response body to attach to an exception. Enough to identify
# what came back without pasting an entire record set into the job log.
BODY_EXCERPT = 500

STATUS_CODE_ERRORS = {
    403: {
        "cause": "Forbidden.",
        "assistance": "The API key authenticated but this operation was refused. An API key inherits the "
        "permissions of the user it is assigned to, so this is usually a permission that user does not have; it can "
        "also mean the capability is switched off for the whole tenant. The reason the API gave, if any, follows.",
    },
    404: {
        "cause": "Not found.",
        "assistance": "Cyber GRC has no record with this ID. Verify the ID, and check the record has not already "
        "been deleted by another workflow or user.",
    },
    429: {
        "cause": "Too many requests.",
        "assistance": "Cyber GRC is rate limiting this API key. Lower the trigger frequency or add a delay step, "
        "then retry the workflow.",
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
        self.url = (url or "").strip().rstrip("/")
        # A key pasted from a password manager often carries a newline or a stray space,
        # which requests refuses to put in a header, so normalise it here.
        self.api_key = (api_key or "").strip()
        self.ssl_verify = ssl_verify
        self.logger = logger
        self.session = requests.Session()
        # The documented Authorization: Bearer alternative rejects cpyl_ keys on the
        # live API, so authenticate with the X-API-Key header only.
        self.session.headers.update({"X-API-Key": self.api_key, "Accept": "application/json"})

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
        # $top above PAGE_LIMIT is rejected with a 400, so a larger ceiling is applied by
        # paging and truncating here instead of being passed through to be refused.
        paged_top = top if top and top <= PAGE_LIMIT else None
        params = self._odata_params(
            {
                "$filter": filter_,
                "$select": select,
                "$expand": expand,
                "$orderby": order_by,
                "$top": paged_top,
                "$skip": skip,
            }
        )
        response = self._request("GET", f"/api/v2/{record_type}", params=params)
        records = self._unwrap_collection(response, record_type)

        # A Top the API could satisfy on its own is a caller-imposed ceiling, so do not page past it.
        next_link = None if paged_top else response.get(f"{ODATA_PREFIX}nextLink")
        for _ in range(MAX_PAGES):
            if not next_link or (top and len(records) >= top):
                break
            response = self._request("GET", next_link)
            records.extend(self._unwrap_collection(response, record_type))
            next_link = response.get(f"{ODATA_PREFIX}nextLink")
        else:
            self.logger.warning(
                f"Stopped paging {record_type} after the maximum of {MAX_PAGES} pages; results may be incomplete. "
                "Narrow the results with a Filter."
            )

        return records[:top] if top else records

    def count_records(self, record_type: str, filter_: str = None) -> int:
        # /$count answers with a text/plain integer rather than JSON.
        params = self._odata_params({"$filter": filter_})
        response = self._request("GET", f"/api/v2/{record_type}/$count", params=params, as_text=True)
        try:
            return int(response.strip())
        except ValueError:
            raise PluginException(
                cause="Cyber GRC returned an unexpected record count.",
                assistance=f"A count of {record_type} answered with a value that is not a whole number. The API may "
                "have returned an error page instead of a count; the start of the response is attached below.",
                data=response[:BODY_EXCERPT],
            )

    def get_record(self, record_type: str, record_id: int, select: str = None, expand: str = None) -> dict:
        params = self._odata_params({"$select": select, "$expand": expand})
        response = self._request("GET", f"/api/v2/{record_type}/{record_id}", params=params)
        return clean_record(self._expect_record(response, f"{record_type} {record_id}"))

    def create_record(self, record_type: str, record: dict, expand: str = None) -> dict:
        params = self._odata_params({"$expand": expand})
        response = self._request("POST", f"/api/v2/{record_type}", params=params, json_body=record)
        return clean_record(self._expect_record(response, f"the created {record_type} record"))

    def update_record(self, record_type: str, record_id: int, record: dict, expand: str = None) -> dict:
        # Some record types reject a body whose id does not match the route key, so
        # supply the key the caller already gave us rather than making them repeat it.
        body = dict(record)
        body.setdefault("id", record_id)

        response = self._request(
            "PUT", f"/api/v2/{record_type}/{record_id}", params=self._odata_params({"$expand": expand}), json_body=body
        )
        if response:
            return clean_record(self._expect_record(response, f"the updated {record_type} record"))

        # A successful update answers 204 with no body, but the action promises to
        # return the updated record, so read it back.
        try:
            return self.get_record(record_type, record_id, expand=expand)
        except PluginException as error:
            raise PluginException(
                cause=f"The {record_type} record was updated, but it could not be read back afterwards.",
                assistance="The update itself succeeded: Cyber GRC accepted it and answered 204 No Content. Reading "
                f"the record back then failed, so this step cannot return it. {error.cause} {error.assistance}",
                data=error.data,
            )

    def delete_record(self, record_type: str, record_id: int) -> dict:
        response = self._request("DELETE", f"/api/v2/{record_type}/{record_id}")
        if not response:
            # A successful delete answers 204 with no body.
            return {"success": True}

        result = clean_record(self._expect_record(response, f"the result of deleting {record_type} {record_id}"))
        if result.get("success") is False:
            # A refused delete is reported in the body of a 200, which would otherwise
            # look to the workflow like a step that had succeeded.
            reason = result.get("message") or "The API reported the delete as unsuccessful without giving a reason."
            blocking = ", ".join(result.get("fkViolationTable") or [])
            if blocking:
                reason += (
                    " Records in the following tables still reference it and must be removed or reassigned first: "
                    f"{blocking}."
                )
            raise PluginException(
                cause=f"Cyber GRC refused to delete {record_type} record {record_id}.",
                assistance=reason,
                data=json.dumps(result),
            )
        return result

    def get_record_history(self, record_type: str, record_id: int) -> List[dict]:
        # The spec writes this as History(), but the OData function-call form is routed to
        # an interactive-only authentication scheme that rejects API keys.
        response = self._request("GET", f"/api/v2/{record_type}/{record_id}/History")
        return self._unwrap_collection(response, f"the history of {record_type} {record_id}")

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

    def _unwrap_collection(self, response: Any, subject: str) -> List[dict]:
        """Collections arrive as {"@odata.context": ..., "value": [...]}."""
        values = response.get("value") if isinstance(response, dict) else response
        if not isinstance(values, list):
            # Returning an empty list here would be indistinguishable from a collection
            # that really is empty, which hides an API change behind a successful step.
            raise PluginException(
                cause=f"Cyber GRC returned an unexpected response for {subject}.",
                assistance="A collection is expected to be a JSON object containing a value array, but the API "
                f"returned {self._describe(response)}. If this persists, the API has changed shape and this plugin "
                "needs an update; report it to Rapid7 support with the response below.",
                data=self._excerpt(response),
            )
        return [clean_record(record) for record in values]

    def _expect_record(self, response: Any, subject: str) -> dict:
        """Guard the object endpoints, which must answer with a single JSON object."""
        if not isinstance(response, dict):
            raise PluginException(
                cause=f"Cyber GRC returned an unexpected response for {subject}.",
                assistance="A single record is expected to be a JSON object, but the API returned "
                f"{self._describe(response)}. If this persists, the API has changed shape and this plugin needs an "
                "update; report it to Rapid7 support with the response below.",
                data=self._excerpt(response),
            )
        return response

    @staticmethod
    def _describe(value: Any) -> str:
        names = {dict: "a JSON object", list: "a JSON array", str: "a string", bool: "a boolean", type(None): "null"}
        return names.get(type(value), f"a value of type {type(value).__name__}")

    @staticmethod
    def _excerpt(value: Any) -> str:
        text = value if isinstance(value, str) else json.dumps(value)
        return text[:BODY_EXCERPT]

    def _scrub(self, text: str) -> str:
        """Keep the API key out of exception data and job logs."""
        if self.api_key and text:
            return text.replace(self.api_key, "[REDACTED]")
        return text

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
        operation = f"{method} {url}"
        try:
            response = self.session.request(
                method, url, params=params, json=json_body, verify=self.ssl_verify, timeout=120
            )
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause=f"Cyber GRC did not respond within 120 seconds to {operation}.",
                assistance="Retry the workflow. If a list action times out consistently, narrow it with a Filter or "
                "a Top so the API has less to return.",
                data=self._scrub(str(error)),
            )
        except requests.exceptions.SSLError as error:
            raise PluginException(
                cause="Could not verify the TLS certificate presented by the Cyber GRC API host.",
                assistance="Verify the URL is correct, or disable SSL Verify on the connection if the host presents "
                "a private certificate.",
                data=self._scrub(str(error)),
            )
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL) as error:
            raise PluginException(
                cause=f"The connection URL is not a valid URL: {self.url or 'empty'}",
                assistance=f"Enter the full API host including the scheme, for example {API_HOST_PATTERN}, with no "
                "path or trailing slash.",
                data=self._scrub(str(error)),
            )
        except requests.exceptions.InvalidHeader:
            # The message from requests quotes the offending header value, so it is not
            # safe to attach: it would put the API key in the job log.
            raise PluginException(
                cause="The API key contains characters that cannot be sent in an HTTP header.",
                assistance="Re-enter the API key on the connection, taking care not to include a line break or any "
                "surrounding quotes. A Cyber GRC key is a single line beginning with cpyl_.",
            )
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause=f"Could not reach the Cyber GRC API host to perform {operation}.",
                assistance=f"Verify the host name resolves and is reachable from the InsightConnect orchestrator, "
                f"and that the URL is the API host rather than the web interface. The API host normally looks like "
                f"{API_HOST_PATTERN}.",
                data=self._scrub(str(error)),
            )
        except requests.exceptions.RequestException as error:
            raise PluginException(
                cause=f"The request to Cyber GRC failed: {operation}",
                assistance="This is a transport level failure rather than an API error. Verify network access from "
                "the orchestrator to the Cyber GRC API host, then retry.",
                data=self._scrub(str(error)),
            )

        self._raise_for_status(response, operation)

        if as_text:
            return response.text
        if not response.content:
            return {}
        try:
            return response.json()
        except ValueError:
            raise PluginException(
                cause=f"Cyber GRC returned a response that is not JSON for {operation}.",
                assistance="The API answered successfully but the body could not be parsed as JSON. The start of "
                "the response is attached below.",
                data=self._scrub(response.text[:BODY_EXCERPT]),
            )

    def _raise_for_status(self, response: requests.Response, operation: str) -> None:
        # A 401 is included because the web interface answers API paths with its sign-in
        # page; a 403 or 5xx page is more likely to come from a gateway in front of the
        # real API, so those are left to the status handlers below.
        if (response.ok or response.status_code == 401) and self._is_html(response):
            raise PluginException(
                cause="Cyber GRC returned a web page instead of an API response.",
                assistance="This usually means the connection URL points at the Cyber GRC web interface rather than "
                f"the API host. The web interface serves its sign-in page for every path, including API paths. The "
                f"API host is a different host and normally looks like {API_HOST_PATTERN}.",
                data=self._scrub(response.text[:BODY_EXCERPT]),
            )
        if response.status_code == 401:
            self._raise_unauthorized(response, operation)
        if response.status_code == 400:
            raise PluginException(
                cause=f"Cyber GRC rejected {operation} as a bad request.",
                assistance=f"{self._api_message(response)} Check any OData query options on this step, such as "
                "Filter, Select, Expand and Order By, against the field names in the Compyl API reference. Field "
                "names are the JSON names of the record type, for example statusID rather than Status.",
                data=self._scrub(response.text[:BODY_EXCERPT]),
            )
        if response.status_code in STATUS_CODE_ERRORS:
            error = STATUS_CODE_ERRORS[response.status_code]
            assistance = f"{error['assistance']} The failing request was {operation}."
            # The API often gives the actual reason, such as a feature being disabled for
            # the tenant rather than the user lacking a permission. That belongs next to
            # the advice, not buried in the data attached below it.
            message = self._api_message(response)
            if message and len(message) <= 300:
                assistance = f"{assistance} Cyber GRC reported: {message}"
            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    assistance = f"{assistance} The API asked for a delay of {retry_after} seconds."
            raise PluginException(cause=error["cause"], assistance=assistance, data=message)
        if response.status_code >= 500:
            raise PluginException(
                cause=f"Cyber GRC returned a server error ({response.status_code}) for {operation}.",
                assistance="The API failed to handle a valid request, so there is nothing to correct in the "
                "workflow. Retry, and if it persists report the request above to Rapid7 support.",
                data=self._scrub(response.text[:BODY_EXCERPT]),
            )
        if not response.ok:
            raise PluginException(
                cause=f"Cyber GRC returned an unexpected status ({response.status_code}) for {operation}.",
                assistance=self._api_message(response),
                data=self._scrub(response.text[:BODY_EXCERPT]),
            )

    def _raise_unauthorized(self, response: requests.Response, operation: str) -> None:
        """A 401 means the key was refused, or that the path does not accept keys at all."""
        message, scheme = self._auth_failure(response)
        if scheme and scheme.lower() != "apikey":
            # Any path the API key middleware does not recognise falls through to the
            # interactive sign-in scheme, so an unknown path is reported as a 401 rather
            # than a 404. Saying "check your key" here sends users down a dead end.
            raise PluginException(
                cause=f"Cyber GRC does not expose {operation} to API keys.",
                assistance="The API key itself was not the problem: this path fell through to the interactive "
                f"'{scheme}' sign-in scheme, which happens when the path does not exist. Check that the record type "
                "is spelled exactly as it appears in the Compyl API reference, including capitalisation, and that "
                "the connection URL is the API host on its own with no /api/v2 suffix. A few endpoints genuinely "
                "accept only interactive sessions, including the v1 flat file upload; Cyber GRC support has to "
                "enable API key access to those.",
                data=self._scrub(message or response.text[:BODY_EXCERPT]),
            )
        raise PluginException(
            cause="Unauthorized.",
            assistance="Cyber GRC rejected the API key. Verify the key was copied in full, that it has not been "
            "revoked or expired, and that it belongs to the same tenant as the connection URL.",
            data=self._scrub(message or response.text[:BODY_EXCERPT]),
        )

    def _auth_failure(self, response: requests.Response) -> Tuple[Optional[str], Optional[str]]:
        """Pull error_description and scheme out of an authentication failure body."""
        body = self._json_body(response)
        if not isinstance(body, dict):
            return None, None
        return body.get("error_description"), body.get("scheme")

    def _api_message(self, response: requests.Response) -> str:
        """The one useful sentence out of an OData error body.

        An OData error carries a full .NET stack trace alongside a precise description of
        what was wrong with the request. Only the description helps the user.
        """
        body = self._json_body(response)
        if isinstance(body, dict):
            error = body.get("error")
            if isinstance(error, dict):
                message = error.get("message") or (error.get("innererror") or {}).get("message")
                if message:
                    return self._scrub(str(message))
            for key in ("error_description", "message", "title"):
                if isinstance(body.get(key), str):
                    return self._scrub(body[key])
            if isinstance(error, str):
                return self._scrub(error)
        return self._scrub(response.text[:BODY_EXCERPT])

    @staticmethod
    def _json_body(response: requests.Response) -> Any:
        try:
            return response.json()
        except ValueError:
            return None

    @staticmethod
    def _is_html(response: requests.Response) -> bool:
        content_type = response.headers.get("Content-Type", "") if response.headers else ""
        if "html" in content_type.lower():
            return True
        # The sign-in page is served without a useful content type on some deployments,
        # so fall back to sniffing the body.
        return response.text[:200].lstrip().lower().startswith(("<!doctype html", "<html"))
