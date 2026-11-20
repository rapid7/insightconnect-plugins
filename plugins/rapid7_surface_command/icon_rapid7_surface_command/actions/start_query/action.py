import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import StartQueryInput, StartQueryOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean


class StartQuery(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="start_query", description=Component.DESCRIPTION, input=StartQueryInput(), output=StartQueryOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        cypher = params.get(Input.CYPHER)
        query_id = params.get(Input.QUERY_ID)
        # END INPUT BINDING - DO NOT REMOVE

        query_id = (query_id or "").strip()
        cypher = (cypher or "").strip()
        if bool(query_id) == bool(cypher):
            raise PluginException(
                cause="Exactly one of Query ID or Cypher Query is required.",
                assistance="Provide the ID of a saved query, or a Cypher query, but not both.",
            )

        result = self.connection.api.start_query(query_id=query_id or None, cypher=cypher or None)
        return {
            Output.STATUS: result["status"],
            Output.JOB_ID: result["job_id"],
            Output.ITEMS: clean(result["items"]),
        }
