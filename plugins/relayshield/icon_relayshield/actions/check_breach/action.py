import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CheckBreachInput, CheckBreachOutput, Input, Output, Component

# Custom imports below


class CheckBreach(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_breach", description=Component.DESCRIPTION, input=CheckBreachInput(), output=CheckBreachOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        email = params.get(Input.EMAIL)
        # END INPUT BINDING - DO NOT REMOVE

        data = self.connection.call("/v1/metered/breach", {"email": email})

        return {
            Output.EMAIL: data.get("email", email),
            Output.BREACH_COUNT: data.get("breach_count", 0),
            Output.BREACHES: data.get("breaches", []),
        }
