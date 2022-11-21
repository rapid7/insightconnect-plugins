import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

import logging
from typing import Callable
from unittest import TestCase

from icon_threatcrowd.actions.hash import Hash
from icon_threatcrowd.actions.hash.schema import Input
from icon_threatcrowd.connection.connection import Connection
from parameterized import parameterized

from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_201_invalid_json,
    mock_request_401,
    mock_request_404,
    mock_request_500,
    mock_request_503,
    mocked_request,
)


class TestHash(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

        self.action = Hash()
        self.action.connection = self.connection
        self.action.logger = logging.getLogger("action logger")

        self.payload = {Input.HASH: "9de5069c5afe602b2ea0a04b66beb2c0"}

    def test_hash_ok(self) -> None:
        mocked_request(mock_request_200)
        response = self.action.run(self.payload)
        expected_response = {
            "domains": ["hpservice.homepc.it", "facebook.controlliamo.com"],
            "found": True,
            "hashes": {"md5": "31d0e421894004393c48de1769744687", "sha1": "4f0eb746d81a616fb9bdff058997ef47a4209a76"},
            "ips": ["8.8.8.8"],
            "permalink": "https://www.threatcrowd.org/malware.php?md5=31d0e421894004393c48de1769744687",
            "references": [],
            "scans": [
                "Error Scanning File",
                "Malware-gen*Win32*Malware-gen",
                "Gen*Variant.Symmi.50061",
                "W32/Trojan.VSQD-1927",
                "BDS/Plugx.266990",
                "Gen*Variant.Symmi.50061",
                "Gen*Variant.Symmi.50061",
                "Win32/Korplug.CF",
                "W32/FakeAV.CX",
                "Generic11_c.CDQL",
                "Trojan.SuspectCRC*Backdoor.Win32.Gulpix",
                "Riskware ( 0040eff71 )",
                "Trojan.Win32.Generic*Backdoor.Win32.Gulpix.yk",
                "Backdoor*Win32/Plugx",
                "Gen*Variant.Symmi.50061[ZP]",
            ],
        }
        self.assertEqual(expected_response, response)

    @parameterized.expand(
        [
            (mock_request_201_invalid_json, PluginException.causes[PluginException.Preset.INVALID_JSON]),
            (mock_request_401, PluginException.causes[PluginException.Preset.UNKNOWN]),
            (mock_request_404, PluginException.causes[PluginException.Preset.NOT_FOUND]),
            (mock_request_500, PluginException.causes[PluginException.Preset.SERVER_ERROR]),
            (mock_request_503, PluginException.causes[PluginException.Preset.SERVICE_UNAVAILABLE]),
        ],
    )
    def test_hash_exception(self, mock_request: Callable, exception: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.payload)
        self.assertEqual(
            context.exception.cause,
            exception,
        )
