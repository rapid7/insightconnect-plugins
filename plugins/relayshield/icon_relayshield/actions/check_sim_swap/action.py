import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CheckSimSwapInput, CheckSimSwapOutput, Input, Output, Component

# Custom imports below


class CheckSimSwap(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_sim_swap",
            description=Component.DESCRIPTION,
            input=CheckSimSwapInput(),
            output=CheckSimSwapOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        phone = params.get(Input.PHONE)
        # END INPUT BINDING - DO NOT REMOVE

        data = self.connection.call("/v1/metered/sim-swap", {"phone": phone})

        return {
            Output.PHONE: data.get("phone", phone),
            Output.SWAPPED: data.get("swapped", False),
            Output.SWAP_TIMESTAMP: data.get("swap_timestamp", ""),
            Output.CARRIER: data.get("carrier", ""),
        }
