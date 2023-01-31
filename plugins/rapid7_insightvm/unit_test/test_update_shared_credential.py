import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from komand_rapid7_insightvm.actions.tag_assets import TagAssets
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.sessions.Session.put", side_effect=Util.mocked_requests)
class TestUpdateSharedCredential(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(TagAssets())

        # make connector in util
        # rename to USC
        # add parameterized test for each service