import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CreateContractInput, CreateContractOutput, Input, Output, Component

# Custom imports below


class CreateContract(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_contract",
            description=Component.DESCRIPTION,
            input=CreateContractInput(),
            output=CreateContractOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        record = params.get(Input.RECORD)
        # END INPUT BINDING - DO NOT REMOVE
        return {Output.CONTRACT: self.connection.client.create_record("Contracts", record)}
