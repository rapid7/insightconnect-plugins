import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch, MagicMock
from icon_gitlab.actions.list_ssh import ListSsh
from icon_gitlab.actions.list_ssh.schema import Output, Input
from jsonschema import validate
from mock import Util, mock_request_200, mocked_request


class TestListSsh(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(ListSsh())
        self.params = {Input.ID: "123"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_list_ssh(self, mock_get: MagicMock) -> None:
        mocked_request(mock_get)
        response = self.action.run(self.params)

        expected = {
            Output.SSH_KEYS: [
                {
                    "created_at": "12.02.23",
                    "id": 17,
                    "key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9wa++Oi7Qkr8prgHc4soW6NUlfDzpvZK2H5E7eQaSeP3SAwGmQKUFHCddNaP0L+hM7zhFNzjFvpaMgJw0=",
                    "title": "MyPubKey",
                },
                {
                    "created_at": "12.02.23",
                    "id": 18,
                    "key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9wa++Oi7Qkr8prgHc4soW6NUlfDzpvZK2H5E7eQaSeP3SAwGmQKUFHCddNaP0L+hM7zhFNzjFvpaMgJw0=",
                    "title": "MyPubKey2",
                },
            ]
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
