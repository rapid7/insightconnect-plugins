import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from mockconnection import MockConnection

from komand_vmray.actions.get_analysis import GetAnalysis


class GetAnalysis(TestCase):

  def test_get_unit(self):
    test_conn = MockConnection()
    test_action = GetAnalysis()

    test_action.connection = test_conn
    action_params = {"route": "https://www.google.com", "headers": {}}
    results = test_action.run(action_params)

    # only new things to test is that it correctly routes output of results
    self.assertEqual(results["status"], 200)
    # more tests?
    self.assertEqual(results["body_object"], {"SampleSuccessBody": "SampleVal"})
    self.assertEqual(results["body_string"], "SAMPLETEXT for method GET")
    self.assertEqual(results["headers"], {"SampleHeader": "SampleVal"})
