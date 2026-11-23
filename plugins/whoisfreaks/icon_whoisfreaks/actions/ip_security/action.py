import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import IpSecurityInput, IpSecurityOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class IpSecurity(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="ip_security",
            description=Component.DESCRIPTION,
            input=IpSecurityInput(),
            output=IpSecurityOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        ip_address = params.get(Input.IP_ADDRESS)
        # END INPUT BINDING - DO NOT REMOVE

        ip_value, reason = validators.ip(ip_address)
        if reason:
            return outputs.not_looked_up(reason)
        result = self.connection.client.lookup("IP Security", "GET", constants.PATH_IP_SECURITY, {"ip": ip_value})
        security = outputs.get_path(result.data_dict, "security")
        flags = {
            Output.IS_TOR: "is_tor",
            Output.IS_PROXY: "is_proxy",
            Output.IS_VPN: "is_vpn",
            Output.IS_KNOWN_ATTACKER: "is_known_attacker",
            Output.IS_BOT: "is_bot",
            Output.IS_SPAM: "is_spam",
            Output.IS_CLOUD_PROVIDER: "is_cloud_provider",
        }
        extra = {name: outputs.to_bool(outputs.get_path(security, key)) for name, key in flags.items()}
        extra[Output.THREAT_SCORE] = outputs.to_int(outputs.get_path(security, "threat_score"))
        return outputs.single(result, extra)
