import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import LinuxUrlAnalysisInput, LinuxUrlAnalysisOutput, Input, Output, Component

# Custom imports below
from anyrun import RunTimeException
from anyrun.connectors import SandboxConnector
from insightconnect_plugin_runtime.helper import clean

from icon_any_run.util.config import Config


class LinuxUrlAnalysis(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="linux_url_analysis",
            description=Component.DESCRIPTION,
            input=LinuxUrlAnalysisInput(),
            output=LinuxUrlAnalysisOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        payload = {
            "obj_url": params.pop(Input.OBJ_URL, ""),
            "env_os": params.get(Input.ENV_OS, "ubuntu"),
            "env_locale": params.get(Input.ENV_LOCALE, ""),
            "obj_ext_extension": params.get(Input.OBJ_EXT_EXTENSION, ""),
            "obj_ext_browser": params.get(Input.OBJ_EXT_BROWSER, ""),
            "opt_auto_delete_after": params.get(Input.OPT_AUTO_DELETE_AFTER, ""),
            "opt_network_connect": params.get(Input.OPT_NETWORK_CONNECT, ""),
            "opt_network_fakenet": params.get(Input.OPT_NETWORK_FAKENET, ""),
            "opt_network_geo": params.get(Input.OPT_NETWORK_GEO, ""),
            "opt_network_mitm": params.get(Input.OPT_NETWORK_MITM, ""),
            "opt_network_residential_proxy": params.get(Input.OPT_NETWORK_RESIDENTIAL_PROXY, ""),
            "opt_network_residential_proxy_geo": params.get(Input.OPT_NETWORK_RESIDENTIAL_PROXY_GEO, ""),
            "opt_network_tor": params.get(Input.OPT_NETWORK_TOR, ""),
            "opt_privacy_type": params.get(Input.OPT_PRIVACY_TYPE, ""),
            "opt_timeout": params.get(Input.OPT_TIMEOUT, ""),
            "user_tags": params.get(Input.USER_TAGS, ""),
        }
        # END INPUT BINDING - DO NOT REMOVE

        try:
            with SandboxConnector.linux(self.connection.sandbox_api_key, integration=Config.VERSION) as connector:
                analysis_uuid = connector.run_url_analysis(**clean(payload))

            return {
                Output.ANALYSIS_UUID: analysis_uuid,
                Output.ANALYSIS_URL: f"https://app.any.run/tasks/{analysis_uuid}",
            }
        except RunTimeException as error:
            raise PluginException(
                cause="Failed to start analysis.",
                assistance=error.description,
                data=error.json,
            )
