from typing import Any, List

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import extract_json, make_request

from komand_redhat_advisory.util.constants import LIST_ADVISORIES_MAX_PAGES, PAGE_SIZE, REQUEST_TIMEOUT
from komand_redhat_advisory.util.endpoints import API_HOST, CSAF_DOC_ENDPOINT, CSAF_LIST_ENDPOINT


class RedHatSecurityDataAPI:
    """Thin client for the public Red Hat Security Data API (CSAF 2.0)."""

    def test_connection(self) -> None:
        self._call_api("GET", CSAF_LIST_ENDPOINT, params={"per_page": 1})

    def list_advisories(self, after: str) -> List[dict]:
        """Return advisories released on or after the given UTC date (paginated)."""
        advisories: List[dict] = []
        for page in range(1, LIST_ADVISORIES_MAX_PAGES + 1):
            batch = self._call_api(
                "GET",
                CSAF_LIST_ENDPOINT,
                params={"after": after, "per_page": PAGE_SIZE, "page": page},
            )
            if not isinstance(batch, list):
                raise PluginException(
                    cause="Red Hat Security Data API returned unexpected response shape.",
                    assistance="This indicates an API contract change. Report this to Rapid7 support.",
                    data=f"Expected JSON list, got {type(batch).__name__}: {str(batch)[:200]}",
                )
            advisories.extend(batch)
            if len(batch) < PAGE_SIZE:
                return advisories
        raise PluginException(
            cause=f"Red Hat Security Data API returned more than {LIST_ADVISORIES_MAX_PAGES} pages "
            f"({LIST_ADVISORIES_MAX_PAGES * PAGE_SIZE} advisories) for after={after}.",
            assistance="This is unexpected for a normal poll window. Report this to Rapid7 support.",
        )

    def get_advisory_document(self, rhsa_id: str) -> dict:
        """Return the full CSAF 2.0 document for the given advisory ID."""
        return self._call_api("GET", f"{CSAF_DOC_ENDPOINT}/{rhsa_id}.json")

    def _call_api(self, method: str, endpoint: str, params: dict = None) -> Any:
        url = f"{API_HOST}{endpoint}"
        request = requests.Request(
            method=method,
            url=url,
            params=params,
            headers={"Accept": "application/json"},
        )
        response = make_request(request, timeout=REQUEST_TIMEOUT)
        return extract_json(response)
