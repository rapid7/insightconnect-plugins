import json
import logging
import sys
import os
import github

sys.path.append(os.path.abspath("../"))

import insightconnect_plugin_runtime
from komand_github.connection.connection import Connection
from komand_github.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params: dict = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if not params:
            params = {Input.CREDENTIALS: {"username": "usename", "personal_token": {"secretKey": "key"}}}
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mock_github(*args, **kwargs):
        class mock_github:
            def __init__(self, auth):
                self.auth = auth

            def get_user(self, username):
                return Util.mock_github_user(username)

            def get_organization(self, org):
                return Util.mock_github_org(org)

        return mock_github(kwargs.get("auth"))

    @staticmethod
    def mock_github_user(*args, **kwargs):
        class mock_github_user:
            def __init__(self, usename="", bio="", email="", avatar_url="", html_url=""):
                self.name = usename
                self.bio = bio
                self.email = email
                self.avatar_url = avatar_url
                self.html_url = html_url

            def get_repo(self, repo):
                return Util.mock_github_repo(repo)

        if (args[0]) == "test_fetch_user":
            return mock_github_user(
                usename="test user",
                bio="this is a bio",
                email="test@test.com",
                avatar_url="https://avatars.githubusercontent.com/u/144030336?v=4",
                html_url="https://github.com/test_fetch_user",
            )

        if (args[0]) == "test_user_invalid_404":
            raise github.GithubException(status=404)

        else:
            return mock_github_user(args[0])

    @staticmethod
    def mock_github_auth_token(*args, **kwargs):
        return args[0]

    @staticmethod
    def mock_github_org(*args, **kwargs):
        class mock_github_org:
            def __init__(self):
                pass

            def get_repo(self, repo):
                return Util.mock_github_repo(repo)

            def remove_from_members(self, user):
                if user.name == "test_user_403":
                    raise github.GithubException(status=403)

                elif user.name == "test_user_404":
                    raise github.GithubException(status=404)

                elif user.name == "test_user_error":
                    raise github.GithubException(status=500)

                return user.name

        return mock_github_org()

    @staticmethod
    def mock_github_repo(*args, **kwargs):
        class mock_github_repo:
            def __init__(self, full_name):
                self.full_name = full_name

            def get_issue(self, issue):
                return Util.mock_github_issue(issue)

            def create_issue(self, **kwargs):
                return Util.mock_github_issue(kwargs)

            def get_milestone(self, milestone):
                return milestone

            def remove_from_collaborators(self, user):
                if user.name == "test_user_403":
                    raise github.GithubException(status=403)

                elif user.name == "test_user_404":
                    raise github.GithubException(status=404)

                elif user.name == "test_user_error":
                    raise github.GithubException(status=500)

                return user.name

        if args[0] == "test_repository_403":
            raise github.GithubException(status=403)

        elif args[0] == "test_repository_404":
            raise github.GithubException(status=404)

        elif args[0] == "test_repository_error":
            raise github.GithubException(status=500)

        return mock_github_repo(args[0])

    @staticmethod
    def mock_github_issue(*args, **kwargs):
        class mock_github_issue:
            def __init__(self):
                self.html_url = "https://github.com/test_organization/test_repository/issues/1#issuecomment-1910003101"

            def edit(self, **kwargs):
                pass

            def create_comment(self, **kwargs):
                if kwargs.get("body") == "error in body":
                    raise github.GithubException(status=500)

                return mock_github_issue()

            def add_to_labels(self, label):
                pass

        if (args[0]) in [403, 404, 500]:
            raise github.GithubException(status=args[0])

        try:
            if args[0].get("title") == "error":
                raise github.GithubException(status=500)
        except Exception:
            pass

        return mock_github_issue()

    @staticmethod
    def mock_get_request(*args, **kwargs):
        class MockGetResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = str(status_code)
                self.content = b""
                self.filename = filename
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")
                    self.content = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                if self.filename:
                    return json.loads(self.text)
                else:
                    return json.loads("this is bad json")

        url = kwargs.get("url", "")
        Authorization = kwargs.get("headers", {}).get("Authorization")
        query = kwargs.get("params", {}).get("q")

        if Authorization == "Bearer error_403":
            return MockGetResponse(status_code=403)

        if Authorization == "Bearer error_404":
            return MockGetResponse(status_code=404)

        elif Authorization == "Bearer error_500":
            return MockGetResponse(status_code=500)

        elif Authorization == "Bearer error_bad_json":
            return MockGetResponse(status_code=200)

        elif url == "https://api.github.com/issues":
            return MockGetResponse(status_code=200, filename="get_my_issues_valid.json.resp")

        elif url in [
            "https://api.github.com/repos/test_owner/test_repo_valid",
            "https://api.github.com/repos/%21%40%C2%A3%24%25%5E%26%2A%2A%28%29/test_repo_valid",
        ]:
            return MockGetResponse(status_code=200, filename="get_repo_valid.json.resp")

        elif url in [
            "https://api.github.com/repos/test_owner/test_repo_valid/issues",
            "https://api.github.com/repos/%21%40%C2%A3%24%25%5E%26%2A%2A%28%29/test_repo_valid/issues",
        ]:
            return MockGetResponse(status_code=200, filename="get_issues_by_repo_valid.json.resp")

        elif url == "https://api.github.com/search/issues":
            if query == "repo:integrationalliance/Test_new_repo test":
                return MockGetResponse(status_code=200, filename="search_valid.json.resp")

        raise NotImplementedError("Not implemented", kwargs)

    @staticmethod
    def mock_put_request(*args, **kwargs):
        class MockPutResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = str(status_code)
                self.content = b""
                self.filename = filename
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")
                    self.content = Util.read_file_to_string(f"responses/{filename}")
                if status_code == 1234:
                    raise ValueError("this is an error")

            def json(self):
                if self.filename:
                    return json.loads(self.text)
                else:
                    return json.loads("this is bad json")

        url = kwargs.get("url", "")
        Authorization = kwargs.get("headers", {}).get("Authorization")

        if Authorization == "Bearer error_204":
            return MockPutResponse(status_code=204)

        elif Authorization == "Bearer error_403":
            return MockPutResponse(status_code=403)

        elif Authorization == "Bearer error_404":
            return MockPutResponse(status_code=404)

        elif Authorization == "Bearer error_422":
            return MockPutResponse(status_code=422)

        elif Authorization == "Bearer error_500":
            return MockPutResponse(status_code=500)

        elif Authorization == "Bearer error":
            return MockPutResponse(status_code=1234)

        if url in [
            "https://api.github.com/user/blocks/test_name",
            "https://api.github.com/user/blocks/%21%40%C2%A3%24%25%5E%26%2A%2A%28%29",
        ]:
            return MockPutResponse(status_code=204)

        if url in ["https://api.github.com/orgs/test_org/memberships/test_username"]:
            return MockPutResponse(status_code=200, filename="add_membership_valid.json.resp")

        if url == "https://api.github.com/repos/test_org/test_repo/collaborators/test_username":
            return MockPutResponse(status_code=201, filename="add_collaborator_valid.json.resp")

        raise NotImplementedError("Not implemented", kwargs)

    @staticmethod
    def mock_delete_request(*args, **kwargs):
        class MockDeleteResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = str(status_code)
                self.content = b""
                self.filename = filename
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")
                    self.content = Util.read_file_to_string(f"responses/{filename}")
                if status_code == 1234:
                    raise ValueError("this is an error")

            def json(self):
                if self.filename:
                    return json.loads(self.text)
                else:
                    return json.loads("this is bad json")

        url = kwargs.get("url", "")
        Authorization = kwargs.get("headers", {}).get("Authorization")

        if Authorization == "Bearer error_404":
            return MockDeleteResponse(status_code=404)

        if Authorization == "Bearer error_500":
            return MockDeleteResponse(status_code=500)

        elif Authorization == "Bearer error":
            return MockDeleteResponse(status_code=1234)

        if url in [
            "https://api.github.com/user/blocks/test_name",
            "https://api.github.com/user/blocks/%21%40%C2%A3%24%25%5E%26%2A%2A%28%29",
        ]:
            return MockDeleteResponse(status_code=204)

        raise NotImplementedError("Not implemented", kwargs)
