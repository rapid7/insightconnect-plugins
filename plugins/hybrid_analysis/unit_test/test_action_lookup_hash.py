import os
import sys
from unittest import TestCase
from unittest.mock import patch

from icon_hybrid_analysis.actions.lookup_hash import LookupHash
from icon_hybrid_analysis.actions.lookup_hash.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util

sys.path.append(os.path.abspath("../"))


class TestLookUpHash(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LookupHash())

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_look_up_hash(self, mocked_request):
        actual = self.action.run({Input.HASH: "40451f20371329b992fb1b85c754d062"})
        expected = {
            "found": True,
            "reports": [
                {
                    "analysis_start_time": "2021-11-09T19:12:21+00:00",
                    "av_detect": 0,
                    "certificates": [],
                    "classification_tags": [],
                    "compromised_hosts": [],
                    "domains": [],
                    "environment_description": "Static Analysis",
                    "extracted_files": [],
                    "hosts": [],
                    "interesting": False,
                    "machine_learning_models": [],
                    "md5": "40451f20371329b992fb1b85c754d062",
                    "mitre_attcks": [],
                    "network_mode": "default",
                    "processes": [],
                    "sha1": "89504d91c5539a366e153894c1bc17277116342b",
                    "sha256": "3919059a1e0d38d6116f24945b0bb2aa5e98b85ac688b3aba270d7997bb64a0d",
                    "sha512": "acfaca234c48f055c0f532e16bd5879f1637ecd639938c3d301b528b08af79988fcd6f0b61e4fd51901b250e72c90a48aca60d20d1b54036373aa6996baae326",
                    "size": 27298,
                    "state": "SUCCESS",
                    "submissions": [
                        {
                            "created_at": "2021-11-10T20:09:28+00:00",
                            "filename": "file",
                            "submission_id": "618c26f8099c0e23c541f405",
                        },
                        {
                            "created_at": "2021-11-09T19:12:21+00:00",
                            "filename": "file",
                            "submission_id": "618ac815742aee567341009c",
                        },
                    ],
                    "submit_name": "file",
                    "tags": [],
                    "threat_level": 0,
                    "total_network_connections": 0,
                    "total_processes": 0,
                    "total_signatures": 0,
                    "type": "PE32 executable (DLL) (GUI) Intel 80386, for MS Windows",
                    "type_short": ["pedll", "executable"],
                    "url_analysis": False,
                    "verdict": "no specific threat",
                }
            ],
            "threatscore": 0,
        }
        self.assertEqual(actual, expected)

        actual = self.action.run({Input.HASH: "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"})

        expected = Util.load_json(f"payloads/action_lookup_hash_sha256_sha1.json.exp")
        self.assertEqual(actual, expected)

        actual = self.action.run({Input.HASH: "44d88612fea8a8f36de82e1278abb02f"})

        expected = Util.load_json(f"payloads/action_lookup_hash_sha256_sha1.json.exp")
        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_bad_look_up_hash(self, mocked_request):
        with self.assertRaises(PluginException) as context:
            self.action.run({Input.HASH: "1"})

        self.assertEqual("Provided hash is not supported.", context.exception.cause)
        self.assertEqual(
            "The API only supports MD5, SHA256, sha1 hashes. Please check the provided hash and try again.",
            context.exception.assistance,
        )
