import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_any_run.actions.run_analysis import RunAnalysis
from icon_any_run.actions.run_analysis.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests)
class TestRunAnalysis(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(RunAnalysis())

    @parameterized.expand(Util.load_parameters("run_analysis").get("parameters"))
    def test_run_analysis(
        self,
        mock_request,
        name,
        file,
        obj_type,
        obj_url,
        obj_ext_cmd,
        obj_ext_browser,
        obj_ext_useragent,
        obj_ext_elevateprompt,
        obj_ext_extension,
        obj_ext_startfolder,
        env_os,
        env_bitness,
        env_version,
        env_type,
        opt_privacy_hidesource,
        opt_network_connect,
        opt_network_fakenet,
        opt_network_tor,
        opt_network_mitm,
        opt_network_geo,
        opt_kernel_heavyevasion,
        opt_privacy_type,
        opt_timeout,
        expected,
    ):
        actual = self.action.run(
            {
                Input.FILE: file,
                Input.OBJ_TYPE: obj_type,
                Input.OBJ_URL: obj_url,
                Input.OBJ_EXT_CMD: obj_ext_cmd,
                Input.OBJ_EXT_BROWSER: obj_ext_browser,
                Input.OBJ_EXT_USERAGENT: obj_ext_useragent,
                Input.OBJ_EXT_ELEVATEPROMPT: obj_ext_elevateprompt,
                Input.OBJ_EXT_EXTENSION: obj_ext_extension,
                Input.OBJ_EXT_STARTFOLDER: obj_ext_startfolder,
                Input.ENV_OS: env_os,
                Input.ENV_BITNESS: env_bitness,
                Input.ENV_VERSION: env_version,
                Input.ENV_TYPE: env_type,
                Input.OPT_PRIVACY_HIDESOURCE: opt_privacy_hidesource,
                Input.OPT_NETWORK_CONNECT: opt_network_connect,
                Input.OPT_NETWORK_FAKENET: opt_network_fakenet,
                Input.OPT_NETWORK_TOR: opt_network_tor,
                Input.OPT_NETWORK_MITM: opt_network_mitm,
                Input.OPT_NETWORK_GEO: opt_network_geo,
                Input.OPT_KERNEL_HEAVYEVASION: opt_kernel_heavyevasion,
                Input.OPT_PRIVACY_TYPE: opt_privacy_type,
                Input.OPT_TIMEOUT: opt_timeout,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("run_analysis_bad").get("parameters"))
    def test_run_analysis_bad(
        self,
        mock_request,
        name,
        file,
        obj_type,
        obj_url,
        obj_ext_cmd,
        obj_ext_browser,
        obj_ext_useragent,
        obj_ext_elevateprompt,
        obj_ext_extension,
        obj_ext_startfolder,
        env_os,
        env_bitness,
        env_version,
        env_type,
        opt_privacy_hidesource,
        opt_network_connect,
        opt_network_fakenet,
        opt_network_tor,
        opt_network_mitm,
        opt_network_geo,
        opt_kernel_heavyevasion,
        opt_privacy_type,
        opt_timeout,
        cause,
        assistance,
    ):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.FILE: file,
                    Input.OBJ_TYPE: obj_type,
                    Input.OBJ_URL: obj_url,
                    Input.OBJ_EXT_CMD: obj_ext_cmd,
                    Input.OBJ_EXT_BROWSER: obj_ext_browser,
                    Input.OBJ_EXT_USERAGENT: obj_ext_useragent,
                    Input.OBJ_EXT_ELEVATEPROMPT: obj_ext_elevateprompt,
                    Input.OBJ_EXT_EXTENSION: obj_ext_extension,
                    Input.OBJ_EXT_STARTFOLDER: obj_ext_startfolder,
                    Input.ENV_OS: env_os,
                    Input.ENV_BITNESS: env_bitness,
                    Input.ENV_VERSION: env_version,
                    Input.ENV_TYPE: env_type,
                    Input.OPT_PRIVACY_HIDESOURCE: opt_privacy_hidesource,
                    Input.OPT_NETWORK_CONNECT: opt_network_connect,
                    Input.OPT_NETWORK_FAKENET: opt_network_fakenet,
                    Input.OPT_NETWORK_TOR: opt_network_tor,
                    Input.OPT_NETWORK_MITM: opt_network_mitm,
                    Input.OPT_NETWORK_GEO: opt_network_geo,
                    Input.OPT_KERNEL_HEAVYEVASION: opt_kernel_heavyevasion,
                    Input.OPT_PRIVACY_TYPE: opt_privacy_type,
                    Input.OPT_TIMEOUT: opt_timeout,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
