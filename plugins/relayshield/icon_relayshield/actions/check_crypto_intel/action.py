import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import CheckCryptoIntelInput, CheckCryptoIntelOutput, Input, Output, Component

# Custom imports below


class CheckCryptoIntel(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_crypto_intel",
            description=Component.DESCRIPTION,
            input=CheckCryptoIntelInput(),
            output=CheckCryptoIntelOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        address = params.get(Input.ADDRESS)
        chain_id = params.get(Input.CHAIN_ID)
        token_address = params.get(Input.TOKEN_ADDRESS)
        # END INPUT BINDING - DO NOT REMOVE

        payload = {"address": address, "chain_id": chain_id or "1"}
        if token_address:
            payload["token_address"] = token_address

        data = self.connection.call("/v1/metered/crypto-intel", payload)

        return {
            Output.ADDRESS: data.get("address", address),
            Output.CHAIN_ID: data.get("chain_id", chain_id or "1"),
            Output.COMPOSITE_RISK: data.get("composite_risk", "LOW"),
            Output.ADDRESS_FLAGS: data.get("address_flags", []),
            Output.TOKEN_RISK: data.get("token_risk") or {},
            Output.CORRELATION_ADVISORIES: data.get("correlation_advisories", []),
        }
