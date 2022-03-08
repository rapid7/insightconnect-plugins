import json
import os

from unit_tests.util import Util

STUB_JOB_ID = "5058b0b4-701a-414e-9630-430d2cddbf4d"
STUB_JOB_ID_DETAIL_SEARCH = "86a8abc0-95f3-4353-adf5-abb631c1f824"
STUB_HOST_VALID = "url"
STUB_HOST_INVALID = "url_invalid"
STUB_ORG_KEY_VALID = "org_key"
STUB_ORG_KEY_FORBIDDEN = "org_key_forbidden"
REQUEST_GET = "GET"
REQUEST_POST = "POST"


# Define and return mock API responses based on request type and endpoint
def mock_request(*args, **_kwarg):
    return mock_request_selection(args[0], args[1])


class MockResponse:
    def __init__(self, filename: str, status_code: int) -> None:
        self.status_code = status_code
        if filename:
            self.text = Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
            )
        else:
            self.text = ""

    def json(self):
        return json.loads(self.text)


def mock_request_post(url):
    if url == f"{STUB_HOST_VALID}/api/investigate/v2/orgs/{STUB_ORG_KEY_VALID}/enriched_events/search_jobs":
        return MockResponse("get_job_id_for_enriched_event", 200)
    if url == f"{STUB_HOST_VALID}/api/investigate/v2/orgs/{STUB_ORG_KEY_VALID}/enriched_events/detail_jobs":
        return MockResponse("get_job_id_for_detail_search", 200)
    if url == f"{STUB_HOST_INVALID}/api/investigate/v2/orgs/{STUB_ORG_KEY_VALID}/enriched_events/search_jobs":
        return MockResponse("find_event_unauthorized", 401)
    if url == f"{STUB_HOST_INVALID}/api/investigate/v2/orgs/{STUB_ORG_KEY_VALID}/enriched_events/detail_jobs":
        return MockResponse("find_event_unauthorized", 401)
    if url == f"{STUB_HOST_VALID}/api/investigate/v2/orgs/{STUB_ORG_KEY_FORBIDDEN}/enriched_events/search_jobs":
        return MockResponse("find_event_forbidden", 403)
    if url == f"{STUB_HOST_VALID}/api/investigate/v2/orgs/{STUB_ORG_KEY_FORBIDDEN}/enriched_events/detail_jobs":
        return MockResponse("find_event_forbidden", 403)


def mock_request_get(url):
    if (
        url
        == f"{STUB_HOST_VALID}/api/investigate/v1/orgs/{STUB_ORG_KEY_VALID}/enriched_events/search_jobs/{STUB_JOB_ID}"
    ):
        return MockResponse("get_enriched_event_status", 200)
    if (
        url
        == f"{STUB_HOST_VALID}/api/investigate/v2/orgs/{STUB_ORG_KEY_VALID}/enriched_events/search_jobs/{STUB_JOB_ID}/results"
    ):
        return MockResponse("retrieve_results_for_enriched_event", 200)
    if (
        url
        == f"{STUB_HOST_VALID}/api/investigate/v2/orgs/{STUB_ORG_KEY_VALID}/enriched_events/detail_jobs/{STUB_JOB_ID_DETAIL_SEARCH}"
    ):
        return MockResponse("check_status_of_detail_search", 200)
    if (
        url
        == f"{STUB_HOST_VALID}/api/investigate/v2/orgs/{STUB_ORG_KEY_VALID}/enriched_events/detail_jobs/{STUB_JOB_ID_DETAIL_SEARCH}/results"
    ):
        return MockResponse("retrieve_results_for_detail_search", 200)


def mock_request_selection(method, url):
    # Check reqeust type and endpoint. Return appropriate file name to be loaded and response code
    if method == REQUEST_POST:
        return mock_request_post(url)
    elif method == REQUEST_GET:
        return mock_request_get(url)
    raise Exception("Response has been not implemented")
