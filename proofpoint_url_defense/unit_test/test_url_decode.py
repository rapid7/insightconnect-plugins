import sys
import os
sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_proofpoint_url_defense.connection.connection import Connection
from komand_proofpoint_url_defense.actions.url_decode import UrlDecode
import json
import logging


class TestUrlDecode(TestCase):
    def test_integration_url_decode(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = UrlDecode()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/url_decode.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = """
            Could not find or read sample tests from /tests directory
            
            An exception here likely means you didn't fill out your samples correctly in the /tests directory 
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
            """
            self.fail(message)


        test_conn.connect(connection_params)
        test_action.connection = test_conn

        # test V2
        results = test_action.run(action_params)
        self.assertEquals({'decoded_url': 'http://www.example.org/url'}, results)

        # test V3
        action_params["encoded_url"] = "https://urldefense.com/v3/__https://www.myclientline.net/publicS/publicServ/ClientLineEnrollment/complete.jsp__;!!MiZrGOEI0vA!NohzERuuhFAIty3SEYDFKwxCVMolJEd8Nz9rLcG4K7F8vlC_LdVlbApnP4DYHhi0l4wPQz_sD0PvfecXmeU0yUsS$"
        results = test_action.run(action_params)
        self.assertEqual({'decoded_url': 'https://www.myclientline.net/publicS/publicServ/ClientLineEnrollment/complete.jsp'}, results)

        # another V2 test
        action_params["encoded_url"] = "https://urldefense.proofpoint.com/v2/url?u=http-3A__amazon.com&d=DQIFAg&c=HUrdOLg_tCr0UMeDjWLBOM9lLDRpsndbROGxEKQRFzk&r=6rcUljFJZnpk5uomPd3v3WCzboqh0RuwO-BZyxMfi0U&m=fo458hhJrF87dIYyHwDAWZkegyOy6sGJVAGrntX1mP0&s=2r8EJkvOhZj1zr2Emwwgjav6t4vvg-O42jL_dHQUDkk&e="
        results = test_action.run(action_params)
        self.assertEqual({'decoded_url': 'http://amazon.com'}, results)

