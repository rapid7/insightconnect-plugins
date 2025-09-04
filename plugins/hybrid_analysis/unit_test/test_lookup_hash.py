import os
import sys
from unittest import TestCase
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from icon_hybrid_analysis.actions.lookup_hash import LookupHash
from icon_hybrid_analysis.actions.lookup_hash.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util


class TestLookUpHash(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(LookupHash())
        cls.maxDiff = None

    @patch("requests.request", side_effect=Util.mocked_request)
    def test_look_up_hash(self, mocked_request):
        actual = self.action.run({Input.HASH: "4c740b7f0bdc728daf9fca05241e85d921a54a6e17ae47ed1577a2b30792cf5c"})
        expected = {
            "found": True,
            "reports": [
                {
                    "id": "6231490aa298763373515933",
                    "environment_id": 100,
                    "environment_description": "Windows 7 32 bit",
                    "state": "SUCCESS",
                    "verdict": "malicious",
                }
            ],
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
            "The API only supports MD5, SHA256, SHA1 hashes. Please check the provided hash and try again.",
            context.exception.assistance,
        )
