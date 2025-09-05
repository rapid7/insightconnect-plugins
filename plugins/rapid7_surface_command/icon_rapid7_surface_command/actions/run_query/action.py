import insightconnect_plugin_runtime
from .schema import RunQueryInput, RunQueryOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean


class RunQuery(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_query",
            description=Component.DESCRIPTION,
            input=RunQueryInput(),
            output=RunQueryOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        query_id = params.get(Input.QUERY_ID)
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.ITEMS: clean(self.connection.api.run_query(query_id=query_id))}
