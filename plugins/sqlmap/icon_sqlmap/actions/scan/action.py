import subprocess

import insightconnect_plugin_runtime
from .schema import ScanInput, ScanOutput, Input, Component, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_sqlmap.util.constants import SQL_MAP_LOGS_FILENAME, DEFAULT_ENCODING
from uuid import uuid4
from io import StringIO


class Scan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="scan",
            description=Component.DESCRIPTION,
            input=ScanInput(),
            output=ScanOutput(),
        )

    def run(self, params=None):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        url = params.get(Input.URL, "")
        headers = params.get(Input.HEADERS, {})
        # END INPUT BINDING - DO NOT REMOVE

        try:
            scan_data = self.connection.sqlmap_client.run_scan(url, headers, params)
            return {Output.RESULT: {"log": scan_data}}
        except Exception as error:
            self.logger.error(f"SQLMap scan failed: {error}")
            self.connection.sqlmap_client.get_logs(cleanup=True)
            raise PluginException(
                cause="SQLMap scan failed.",
                assistance="Please check the URL and SQLMap API connectivity.",
                data=error,
            )
