import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import SearchMachinesInput, SearchMachinesOutput, Input, Output, Component

# Custom imports below


class SearchMachines(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_machines",
            description=Component.DESCRIPTION,
            input=SearchMachinesInput(),
            output=SearchMachinesOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        odata_filter = params.get(Input.FILTER)
        limit = params.get(Input.LIMIT, 100)
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info("Running...")

        response = self.connection.client.search_machines(odata_filter, limit)

        return {
            Output.MACHINES: insightconnect_plugin_runtime.helper.clean(response.get("value", [])),
        }
