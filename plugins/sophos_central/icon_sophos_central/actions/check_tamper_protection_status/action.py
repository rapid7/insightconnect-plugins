import insightconnect_plugin_runtime
from .schema import (
    CheckTamperProtectionStatusInput,
    CheckTamperProtectionStatusOutput,
    Input,
    Output,
    Component,
)

# Custom imports below


class CheckTamperProtectionStatus(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_tamper_protection_status",
            description=Component.DESCRIPTION,
            input=CheckTamperProtectionStatusInput(),
            output=CheckTamperProtectionStatusOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        agent = params.get(Input.AGENT)
        # END INPUT BINDING - DO NOT REMOVE

        return {
            Output.TAMPER_STATUS: {
                "enabled": self.connection.client.tamper_status(self.connection.client.get_endpoint_id(agent)).get(
                    "enabled"
                )
            }
        }
