import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate

from icon_any_run.actions.get_reputation import GetReputation
from icon_any_run.actions.get_reputation.schema import Input, Output

from util import Util


def _file_meta_mock() -> MagicMock:
    hashes = MagicMock()
    hashes.md5 = "d41d8cd98f00b204e9800998ecf8427e"
    hashes.sha1 = "da39a3ee5e6b4b0d3255bfef95601890afd80709"
    hashes.sha256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    hashes.ssdeep = "3::"

    fm = MagicMock()
    fm.file_extension = ".exe"
    fm.filename = "sample.exe"
    fm.filepath = "C:\\\\temp\\\\sample.exe"
    fm.hashes = hashes
    return fm


@patch("icon_any_run.actions.get_reputation.action.LookupConnector")
class TestGetReputation(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetReputation())

    def test_get_reputation_url(self, mock_lookup_cls: MagicMock) -> None:
        mock_cm = MagicMock()
        mock_lookup_cls.return_value.__enter__.return_value = mock_cm
        mock_lookup_cls.return_value.__exit__.return_value = None

        summary = MagicMock()
        summary.asn.return_value = "AS64496"
        fm = _file_meta_mock()
        summary.file_meta.return_value = fm
        summary.country.return_value = "US"
        summary.industries.return_value = "Tech"
        summary.tasks.return_value = "task-list"
        summary.last_modified.return_value = "2024-01-01"
        summary.port.return_value = "443"
        summary.tags.return_value = "tag-a"
        summary.verdict.return_value = "Malicious"
        summary.intelligence_url.return_value = "https://intelligence.any.run/url"

        mock_cm.get_intelligence.return_value = summary

        entity_value = "https://malware.example/payload"
        actual = self.action.run({Input.ENTITY_TYPE: "url", Input.ENTITY_VALUE: entity_value, Input.LOOKUP_DEPTH: 180})

        validate(actual, self.action.output.schema)
        mock_cm.get_intelligence.assert_called_once_with(url=entity_value, lookup_depth=180, parse_response=True)
        self.assertEqual(actual[Output.VERDICT], "Malicious")
        self.assertEqual(actual[Output.LOOKUP_URL], "https://intelligence.any.run/url")
        self.assertEqual(actual[Output.MD5], fm.hashes.md5)

    def test_get_reputation_hash(self, mock_lookup_cls: MagicMock) -> None:
        mock_cm = MagicMock()
        mock_lookup_cls.return_value.__enter__.return_value = mock_cm
        mock_lookup_cls.return_value.__exit__.return_value = None

        summary = MagicMock()
        summary.asn.return_value = ""
        summary.file_meta.return_value = None
        summary.country.return_value = ""
        summary.industries.return_value = ""
        summary.tasks.return_value = ""
        summary.last_modified.return_value = ""
        summary.port.return_value = ""
        summary.tags.return_value = ""
        summary.verdict.return_value = "No threats detected"
        summary.intelligence_url.return_value = "https://intelligence.any.run/hash"

        mock_cm.get_intelligence.return_value = summary

        sha256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        actual = self.action.run({Input.ENTITY_TYPE: "hash", Input.ENTITY_VALUE: sha256, Input.LOOKUP_DEPTH: 30})

        validate(actual, self.action.output.schema)
        mock_cm.get_intelligence.assert_called_once_with(sha256=sha256, lookup_depth=30, parse_response=True)
        self.assertEqual(actual[Output.VERDICT], "No threats detected")
