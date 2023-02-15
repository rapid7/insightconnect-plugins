import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_samanage.actions.list_incidents import ListIncidents
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized



class TestListIncidents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListIncidents())

    #@parameterized.expand(Util.load_parameters("list_incidents").get("parameters"))
    #@patch('requests.request', side_effect=Util.mocked_requests)
    @patch('requests.request', side_effect=Util.mocked_requests)
    #def test_list_incidents(self, mock_request, name, inputs, expected):
    def test_list_incidents(self, mock_request):
        print("Before actual")
        params = {
            "phone": "12345",
            "mobile_phone": "1234567",
            "name": "ExampleUser",
            "token": {"secretKey": "Examplesecretkey"},
            "email": "example@user.com",
            "role": "Example role",
            "department": "Example department",

        }
        actual = self.action.run(params)
        print("actual : {}".format(actual))
        self.assertEqual(actual, expected)
