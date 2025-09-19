import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import RunAdhocQueryInput, RunAdhocQueryOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean


class RunAdhocQuery(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_adhoc_query",
            description=Component.DESCRIPTION,
            input=RunAdhocQueryInput(),
            output=RunAdhocQueryOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        cypher = params.get(Input.CYPHER)
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.ITEMS: clean(self.connection.api.run_adhoc_query(cypher=cypher))}
