import json
import os
from types import TracebackType
from typing import Any, Callable, Optional, Type
from unittest import mock

import requests


class MockResponse:
    def __init__(self, filename: str, status_code: int, text: str = "") -> None:
        self.filename = filename
        self.status_code = status_code
        self.text = text
        self.content = b""  # Add content attribute for non-JSON responses

    def json(self) -> dict[str, Any]:
        with open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                f"responses/{self.filename}.json.resp",
            )
        ) as file:
            return json.load(file)

    def __enter__(self):
        return self

    def __exit__(
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        exception_traceback: Optional[TracebackType],
    ) -> bool:
        return False


def mocked_request(side_effect: Callable) -> None:
    mock_function = requests
    mock_function.request = mock.Mock(side_effect=side_effect)


def mock_conditions(method: str, url: str, status_code: int) -> MockResponse:
    if method == "GET":
        if "/issue/" in url and "/transitions" in url:
            if status_code == 200:
                return MockResponse("get_transitions", status_code)
            elif status_code == 404:
                return MockResponse("get_transitions", status_code, "Issue not found")
            elif status_code == 401:
                return MockResponse("get_transitions", status_code, "Unauthorized")
        elif "/issue/" in url and "/transitions" not in url:
            if status_code == 200:
                return MockResponse("get_issue", status_code)
            elif status_code == 404:
                return MockResponse("get_issue", status_code, "Issue not found")
            elif status_code == 401:
                return MockResponse("get_issue", status_code, "Unauthorized")
        elif "/user/search" in url:
            if status_code == 200:
                return MockResponse("get_user", status_code)
            elif status_code == 404:
                return MockResponse("get_user", status_code, "User not found")
            elif status_code == 401:
                return MockResponse("get_user", status_code, "Unauthorized")
        elif "/attachment/content/" in url:
            if status_code == 200:
                return MockResponse("get_attachment_content", status_code)
            elif status_code == 404:
                return MockResponse("get_attachment_content", status_code, "Attachment not found")
            elif status_code == 401:
                return MockResponse("get_attachment_content", status_code, "Unauthorized")
        elif "/issuetype" in url:
            if status_code == 200:
                return MockResponse("get_all_issue_types", status_code)
            elif status_code == 401:
                return MockResponse("get_all_issue_types", status_code, "Unauthorized")
        elif "/project/search" in url:
            if status_code == 200:
                return MockResponse("get_project", status_code)
            elif status_code == 404:
                return MockResponse("get_project", status_code, "Project not found")
            elif status_code == 401:
                return MockResponse("get_project", status_code, "Unauthorized")
        elif "/field" in url:
            if status_code == 200:
                return MockResponse("get_issue_fields", status_code)
            elif status_code == 401:
                return MockResponse("get_issue_fields", status_code, "Unauthorized")
        elif "/search/jql" in url:
            # GET /search/jql
            if status_code == 200:
                return MockResponse("search_issues", status_code)
            elif status_code == 400:
                return MockResponse("search_issues", status_code, "Invalid JQL")
            elif status_code == 401:
                return MockResponse("search_issues", status_code, "Unauthorized")

    # POST endpoints
    elif method == "POST":
        if "/issue/" in url and "/comment" in url:
            if status_code == 201 or status_code == 200:
                return MockResponse("add_comment_to_issue", status_code)
            elif status_code == 404:
                return MockResponse("add_comment_to_issue", status_code, "Issue not found")
            elif status_code == 400:
                return MockResponse("add_comment_to_issue", status_code, "Bad request")
            elif status_code == 401:
                return MockResponse("add_comment_to_issue", status_code, "Unauthorized")
        elif "/issue/" in url and "/attachments" in url:
            if status_code == 200 or status_code == 201:
                return MockResponse("add_attachment", status_code)
            elif status_code == 404:
                return MockResponse("add_attachment", status_code, "Issue not found")
            elif status_code == 400:
                return MockResponse("add_attachment", status_code, "Bad request")
            elif status_code == 401:
                return MockResponse("add_attachment", status_code, "Unauthorized")
        elif "/issue/" in url and "/transitions" in url:
            if status_code == 204 or status_code == 200:
                return MockResponse("transition_issue", status_code)
            elif status_code == 404:
                return MockResponse("transition_issue", status_code, "Issue or transition not found")
            elif status_code == 400:
                return MockResponse("transition_issue", status_code, "Bad request")
            elif status_code == 401:
                return MockResponse("transition_issue", status_code, "Unauthorized")
        elif url.endswith("/issue") or "/issue" in url and "/issue/" not in url:
            if status_code == 201 or status_code == 200:
                return MockResponse("create_issue", status_code)
            elif status_code == 400:
                return MockResponse("create_issue", status_code, "Bad request")
            elif status_code == 401:
                return MockResponse("create_issue", status_code, "Unauthorized")
        elif "/user" in url and "/user/" not in url:
            if status_code == 201 or status_code == 200:
                return MockResponse("add_user", status_code)
            elif status_code == 400:
                return MockResponse("add_user", status_code, "Bad request")
            elif status_code == 401:
                return MockResponse("add_user", status_code, "Unauthorized")

    # PUT endpoints
    elif method == "PUT":
        if "/issue/" in url and "/assignee" in url:
            if status_code == 204 or status_code == 200:
                return MockResponse("assign_issue", status_code)
            elif status_code == 404:
                return MockResponse("assign_issue", status_code, "Issue not found")
            elif status_code == 400:
                return MockResponse("assign_issue", status_code, "Bad request")
            elif status_code == 401:
                return MockResponse("assign_issue", status_code, "Unauthorized")
        elif "/issue/" in url:
            if status_code == 204 or status_code == 200:
                return MockResponse("edit_issue", status_code)
            elif status_code == 404:
                return MockResponse("edit_issue", status_code, "Issue not found")
            elif status_code == 400:
                return MockResponse("edit_issue", status_code, "Bad request")
            elif status_code == 401:
                return MockResponse("edit_issue", status_code, "Unauthorized")

    # DELETE endpoints
    elif method == "DELETE":
        if "/user" in url:
            if status_code == 204 or status_code == 200:
                return MockResponse("delete_user", status_code)
            elif status_code == 404:
                return MockResponse("delete_user", status_code, "User not found")
            elif status_code == 400:
                return MockResponse("delete_user", status_code, "Bad request")
            elif status_code == 401:
                return MockResponse("delete_user", status_code, "Unauthorized")

    # Generic error responses for status codes
    if status_code == 400:
        return MockResponse("error_400", status_code, "Bad request")
    elif status_code == 401:
        return MockResponse("error_401", status_code, "Unauthorized")
    elif status_code == 403:
        return MockResponse("error_403", status_code, "Forbidden")
    elif status_code == 404:
        return MockResponse("error_404", status_code, "Not found")
    elif status_code == 500:
        return MockResponse("error_500", status_code, "Internal server error")
    elif status_code == 201:
        return MockResponse("success_201", status_code, "Created")

    # In case of unhandled conditions, raise an exception
    raise Exception("Not implemented.")


def mock_request_200(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 200)


def mock_request_201_invalid_json(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 201)


def mock_request_400(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 400)


def mock_request_401(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 401)


def mock_request_404(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 404)


def mock_request_500(*args, **kwargs) -> MockResponse:
    return mock_conditions(args[0], args[1], 500)


# Rich text in descriptions and comments: Jira wiki markup and an Atlassian Document Format (ADF) document
WIKI_MARKUP = "*bold* [Rapid7|https://www.rapid7.com]"
ADF_DOCUMENT = {
    "type": "doc",
    "version": 1,
    "content": [{"type": "paragraph", "content": [{"type": "text", "text": "bold", "marks": [{"type": "strong"}]}]}],
}


def text_as_adf(text: str) -> dict[str, Any]:
    return {
        "type": "doc",
        "version": 1,
        "content": [{"type": "paragraph", "content": [{"type": "text", "text": text}]}],
    }


def get_request(mock_request: mock.Mock, method: str) -> tuple[str, Any]:
    # Returns the URL and the JSON body of the last request sent with the given method
    calls = [call for call in mock_request.call_args_list if call.args[0] == method]
    return calls[-1].args[1], calls[-1].kwargs.get("json")


def get_urls(mock_request: mock.Mock, method: str) -> list[str]:
    # Returns the URLs of all requests sent with the given method
    return [call.args[1] for call in mock_request.call_args_list if call.args[0] == method]
