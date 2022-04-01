import os

from unit_test.util import Util
from komand_google_search.actions.search.schema import Input as SearchInput

STUB_JOB_ID = "5058b0b4-701a-414e-9630-430d2cddbf4d"
STUB_JOB_ID_DETAIL_SEARCH = "86a8abc0-95f3-4353-adf5-abb631c1f824"
STUB_HOST_VALID = "url"
STUB_HOST_INVALID = "url_invalid"
STUB_ORG_KEY_VALID = "org_key"
STUB_ORG_KEY_FORBIDDEN = "org_key_forbidden"
REQUEST_GET = "GET"
REQUEST_POST = "POST"


# Define and return mock API responses based on request type and endpoint
def mock_search_func(*args, **kwargs):
    return mock_response_selection(kwargs.get(SearchInput.QUERY))

def mock_get_page_func(*args, **kwargs):
    return mock_response_selection(args[0])

def mock_response_retrieval(filename: str) -> str:
    text = ""
    if filename:
        text = Util.read_file_to_string(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{filename}.resp")
        )
    return text

def mock_response_selection(query_param):
    if query_param == "Example Organization":
        return mock_response_retrieval("search").split(",")
    if query_param == "http://www.example.com":
        return mock_response_retrieval("get_page").encode('utf8')
