import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_trendmicro_apex.actions.download_openioc_file import DownloadOpeniocFile
from icon_trendmicro_apex.actions.download_openioc_file.schema import Input, Output
from unit_test.mock import Util, mock_request_200, mocked_request
from jsonschema import validate


@patch("icon_trendmicro_apex.connection.connection.create_jwt_token", side_effect="abcgdgd")
class TestDownloadOpeniocFile(TestCase):
    @patch("requests.request", side_effect=mock_request_200)
    def setUp(self, mock_client) -> None:
        self.action = Util.default_connector(DownloadOpeniocFile())
        self.params = {Input.FILE_HASH_ID: "769fcc7550bf98d96bccb7e22a5557301c403455"}

    @patch("requests.request", side_effect=mock_request_200)
    def test_download_openioc_file(self, mock_get, mock_token):
        mocked_request(mock_get)
        response = self.action.run(self.params)

        expected = {
            Output.DATA: {
                "FileContentBase64": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXMtYXNjaWkiPz4KPGlvYyB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIiB4bWxuczp4c2Q9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hIiBpZD0iYTEzZTI4MmQtNjVlMS00MjYzLTliMzEtNWY5MTI1MTUyODhjIiBsYXN0LW1vZGlmaWVkPSIyMDEzLTEwLTMwVDE5OjA3OjQ2IiB4bWxucz0iaHR0cDovL3NjaGVtYXMubWFuZGlhbnQuY29tLzIwMTAvaW9jIj4KICA8c2hvcnRfZGVzY3JpcHRpb24+Q3J5cHRvbG9ja2VyIERldGVjdGlvbiAoRVhQRVJJTUVOVEFMKTwvc2hvcnRfZGVzY3JpcHRpb24+CiAgPGRlc2NyaXB0aW9uPlRoaXMgSU9DIGRldGVjdHMgcmVnaXN0cnkgZW50cmllcyBjcmVhdGVkIHdoZW4gdGhlIENyeXB0b2xvY2tlciBjcmltZXdhcmUgcnVucy4gUHJlc2VuY2Ugb2Ygb25lIG9mIHRoZXNlIHJlZ2lzdHJ5IGtleSBzaG93cyB0aGF0IGEgYm94IGhhcyBsaWtlbHkgYmVlbiBpbmZlY3RlZCB3aXRoIHRoZSBDcnlwdG9sb2NrZXIgc29mdHdhcmUuPC9kZXNjcmlwdGlvbj4KICA8YXV0aG9yZWRfYnk+TWFuZGlhbnQ8L2F1dGhvcmVkX2J5PgogIDxhdXRob3JlZF9kYXRlPjIwMTMtMTAtMjhUMTQ6Mjc6MTI8L2F1dGhvcmVkX2RhdGU+CiAgPGxpbmtzPgogICAgPGxpbmsgcmVsPSJncmFkZSI+dW50ZXN0ZWQ8L2xpbms+CiAgPC9saW5rcz4KICA8ZGVmaW5pdGlvbj4KICAgIDxJbmRpY2F0b3Igb3BlcmF0b3I9Ik9SIiBpZD0iN2VhNjA1YjctOGFiMS00ZTFjLTkxMjgtOTk5MjY1Y2Q5ZjIxIj4KICAgICAgPEluZGljYXRvckl0ZW0gaWQ9ImE3MWViMGQ3LWFmZTUtNDcwOC04ZGJiLTM3OWJkNDNjYzlkNyIgY29uZGl0aW9uPSJjb250YWlucyI+CiAgICAgICAgPENvbnRleHQgZG9jdW1lbnQ9IlJlZ2lzdHJ5SXRlbSIgc2VhcmNoPSJSZWdpc3RyeUl0ZW0vUGF0aCIgdHlwZT0ibWlyIiAvPgogICAgICAgIDxDb250ZW50IHR5cGU9InN0cmluZyI+U29mdHdhcmVcQ3J5cHRvTG9ja2VyXEZpbGVzPC9Db250ZW50PgogICAgICA8L0luZGljYXRvckl0ZW0+CiAgICAgIDxJbmRpY2F0b3Igb3BlcmF0b3I9IkFORCIgaWQ9ImJmYmVmOGEyLTdmMTktNDAwZC04Yjg5LTg3ZjdjNzYwNzhhZSI+CiAgICAgICAgPEluZGljYXRvckl0ZW0gaWQ9IjQyZTk2OTk4LTcxNjEtNGYyMi1iYjc3LTczNjYwZTI2OWE2YiIgY29uZGl0aW9uPSJjb250YWlucyI+CiAgICAgICAgICA8Q29udGV4dCBkb2N1bWVudD0iUmVnaXN0cnlJdGVtIiBzZWFyY2g9IlJlZ2lzdHJ5SXRlbS9QYXRoIiB0eXBlPSJtaXIiIC8+CiAgICAgICAgICA8Q29udGVudCB0eXBlPSJzdHJpbmciPkN1cnJlbnRWZXJzaW9uXFJ1bjwvQ29udGVudD4KICAgICAgICA8L0luZGljYXRvckl0ZW0+CiAgICAgICAgPEluZGljYXRvckl0ZW0gaWQ9IjVkNWI4Mjk2LTAxYzktNDE0Ni05YTc0LWFiYTUzMWM1NzQ3OSIgY29uZGl0aW9uPSJjb250YWlucyI+CiAgICAgICAgICA8Q29udGV4dCBkb2N1bWVudD0iUmVnaXN0cnlJdGVtIiBzZWFyY2g9IlJlZ2lzdHJ5SXRlbS9QYXRoIiB0eXBlPSJtaXIiIC8+CiAgICAgICAgICA8Q29udGVudCB0eXBlPSJzdHJpbmciPkNyeXB0b2xvY2tlcjwvQ29udGVudD4KICAgICAgICA8L0luZGljYXRvckl0ZW0+CiAgICAgIDwvSW5kaWNhdG9yPgogICAgPC9JbmRpY2F0b3I+CiAgPC9kZWZpbml0aW9uPgo8L2lvYz4=",
                "FileName": "file.txt",
            },
            Output.FEATURECTRL: {"mode": "0"},
            Output.META: {"ErrorCode": 0, "Result": 1},
            Output.PERMISSIONCTRL: {"permission": "255"},
            Output.SYSTEMCTRL: {"TmcmSoDist_Role": "none"},
        }
        validate(response, self.action.output.schema)
        self.assertEqual(response, expected)
