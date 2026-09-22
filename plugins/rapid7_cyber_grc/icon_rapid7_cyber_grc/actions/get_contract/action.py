import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetContractInput, GetContractOutput, Input, Output, Component

# Custom imports below


class GetContract(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_contract", description=Component.DESCRIPTION, input=GetContractInput(), output=GetContractOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        record_id = params.get(Input.ID)
        select = params.get(Input.SELECT)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.CONTRACT: self.connection.client.get_record("Contracts", record_id, select=select)}
