import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import DownloadPcapInput, DownloadPcapOutput, Input, Output, Component

# Custom imports below
import base64
from anyrun import RunTimeException
from anyrun.connectors.sandbox.base_connector import BaseSandboxConnector

from icon_any_run.util.config import Config
from icon_any_run.util.tools import get_report_name


class DownloadPcap(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_pcap",
            description=Component.DESCRIPTION,
            input=DownloadPcapInput(),
            output=DownloadPcapOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        analysis_uuid = params.get(Input.ANALYSIS_UUID, "")
        # END INPUT BINDING - DO NOT REMOVE
        try:
            with BaseSandboxConnector(self.connection.sandbox_api_key, integration=Config.VERSION) as connector:
                pcap_content = connector.download_pcap(analysis_uuid)

            return {
                Output.PCAP: {
                    "filename": get_report_name(analysis_uuid, "pcap"),
                    "content": base64.b64encode(pcap_content).decode(),
                }
            }
        except RunTimeException as error:
            raise PluginException(
                cause="Failed to download analysis pcap.",
                assistance=error.description,
                data=error.json,
            )
