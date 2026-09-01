import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CheckDomainInput, CheckDomainOutput, Input, Output, Component

# Custom imports below


class CheckDomain(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_domain", description=Component.DESCRIPTION, input=CheckDomainInput(), output=CheckDomainOutput()
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain = params.get(Input.DOMAIN)
        # END INPUT BINDING - DO NOT REMOVE

        data = self.connection.call("/v1/metered/domain", {"domain": domain})

        return {
            Output.DOMAIN: data.get("domain", domain),
            Output.LOOKALIKES_FOUND: data.get("lookalikes_found", 0),
            Output.LOOKALIKES: data.get("lookalikes", []),
        }
