import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetIntelligenceInput, GetIntelligenceOutput, Input, Output, Component

# Custom imports below
import base64
import json

from anyrun import RunTimeException
from anyrun.connectors import LookupConnector

from icon_any_run.util.config import Config
from icon_any_run.util.tools import get_report_name


class GetIntelligence(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_intelligence",
            description=Component.DESCRIPTION,
            input=GetIntelligenceInput(),
            output=GetIntelligenceOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        lookup_depth = params.get(Input.LOOKUP_DEPTH)
        query = params.get(Input.QUERY)
        # END INPUT BINDING - DO NOT REMOVE
        try:
            with LookupConnector(self.connection.lookup_api_key, integration=Config.VERSION) as connector:
                report = connector.get_intelligence(query=query, lookup_depth=lookup_depth)

            lookup_url = (
                "https://intelligence.any.run/analysis/lookup#{%22query%22:%22"
                + query.replace('"', "%5C%22").replace(" ", "%20")
                + "%22,%22dateRange%22:180}"
            )

            return {
                Output.LOOKUP_URL: lookup_url,
                Output.REPORT: {
                    "filename": get_report_name("TI_LOOKUP", "json"),
                    "content": base64.b64encode(json.dumps(report).encode()).decode(),
                },
            }

        except RunTimeException as error:
            raise PluginException(
                cause="Failed to get intelligence.",
                assistance=error.description,
                data=error.json,
            )
