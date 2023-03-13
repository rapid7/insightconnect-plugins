import insightconnect_plugin_runtime
from .schema import RrHistoryIpInput, RrHistoryIpOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from IPy import IP as IP_Validate


class RrHistoryIp(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="rr_history_ip",
            description="Return the history that Umbrella has seen for a given IP address",
            input=RrHistoryIpInput(),
            output=RrHistoryIpOutput(),
        )

    def run(self, params={}):
        ip_address = params.get(Input.IP)
        try:
            IP_Validate(ip_address)
        except Exception as error:
            raise PluginException(
                cause="Invalid IP provided by user.",
                assistance="Please try again by submitting a valid IP address.",
                data=error,
            )

        try:
            type_ = params.get(Input.TYPE)
            if not type_:
                rr_history = self.connection.investigate.rr_history(ip_address)
            else:
                rr_history = self.connection.investigate.rr_history(ip_address, type_)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        return {Output.FEATURES: [rr_history.get("features")], Output.RRS: rr_history.get("rrs")}
