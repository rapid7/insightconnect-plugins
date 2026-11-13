import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import DomainReputationInput, DomainReputationOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class DomainReputation(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain_reputation",
            description=Component.DESCRIPTION,
            input=DomainReputationInput(),
            output=DomainReputationOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain = params.get(Input.DOMAIN)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.client.lookup(
            "Domain Reputation", "GET", constants.PATH_DOMAIN_REPUTATION, {"domainName": validators.domain(domain)}
        )
        data = result.data_dict
        return outputs.single(
            result,
            {
                Output.VERDICT: outputs.to_str(outputs.get_path(data, "risk_category", "verdict")),
                Output.SEVERITY: outputs.to_str(outputs.get_path(data, "risk_category", "severity")),
                Output.CONFIDENCE: outputs.to_float(outputs.get_path(data, "risk_category", "confidence")),
                Output.TRUST_SCORE: outputs.to_int(outputs.get_path(data, "trust_signals", "trust_score")),
                Output.IS_DGA: outputs.to_bool(outputs.get_path(data, "dga_score", "is_dga")),
            },
        )
