import sys
import os
from unittest.mock import patch
from unittest import TestCase
from komand_paloalto_wildfire.actions.submit_file import SubmitFile
from komand_paloalto_wildfire.actions.submit_file.schema import Input
from unit_test.test_util import Util
from pyldfire import WildFireException

sys.path.append(os.path.abspath("../"))


class TestSubmitFile(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SubmitFile())

    @patch(
        "pyldfire.WildFire.submit_file",
        side_effect=WildFireException("Unsupport File type with sample sha256:invalidFile"),
    )
    def test_submit_file_unsupported_type(self, mock_request):
        actual = self.action.run(
            {
                Input.FILE: "WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgrSCo=",
                Input.FILENAME: "EICAR.txt",
            }
        )
        expected = {"submission": {"supported_file_type": False, "filename": "Unknown", "url": "Unknown"}}

        self.assertEqual(actual, expected)
