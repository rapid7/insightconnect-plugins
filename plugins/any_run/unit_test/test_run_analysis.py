import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_any_run.actions.run_analysis import RunAnalysis
from icon_any_run.actions.run_analysis.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mocked_requests)
class TestRunAnalysis(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(RunAnalysis())

    @parameterized.expand(Util.load_parameters("run_analysis").get("parameters"))
    def test_run_analysis(
        self,
        mock_request: MagicMock,
        name: str,
        file: Dict[str, Any],
        obj_type: str,
        obj_url: str,
        obj_ext_cmd: str,
        obj_ext_browser: str,
        obj_ext_useragent: str,
        obj_ext_elevateprompt: bool,
        obj_ext_extension: str,
        obj_ext_startfolder: str,
        env_os: str,
        env_bitness: str,
        env_version: str,
        env_type: str,
        opt_privacy_hidesource: bool,
        opt_network_connect: bool,
        opt_network_fakenet: bool,
        opt_network_tor: bool,
        opt_network_mitm: bool,
        opt_network_geo: str,
        opt_kernel_heavyevasion: bool,
        opt_privacy_type: str,
        opt_timeout: int,
        expected: Dict[str, Any],
    ) -> None:
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
        validate(actual, self.action.output.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("run_analysis_bad").get("parameters"))
    def test_run_analysis_bad(
        self,
        mock_request: MagicMock,
        name: str,
        file: Dict[str, Any],
        obj_type: str,
        obj_url: str,
        obj_ext_cmd: str,
        obj_ext_browser: str,
        obj_ext_useragent: str,
        obj_ext_elevateprompt: bool,
        obj_ext_extension: str,
        obj_ext_startfolder: str,
        env_os: str,
        env_bitness: str,
        env_version: str,
        env_type: str,
        opt_privacy_hidesource: bool,
        opt_network_connect: bool,
        opt_network_fakenet: bool,
        opt_network_tor: bool,
        opt_network_mitm: bool,
        opt_network_geo: str,
        opt_kernel_heavyevasion: bool,
        opt_privacy_type: str,
        opt_timeout: int,
        cause: str,
        assistance: str,
    ) -> None:
        with self.assertRaises(PluginException) as error:
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
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
