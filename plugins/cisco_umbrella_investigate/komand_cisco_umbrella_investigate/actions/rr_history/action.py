import insightconnect_plugin_runtime
from .schema import RrHistoryInput, RrHistoryOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class RrHistory(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="rr_history",
            description="Return the history that Umbrella has seen for a given domain",
            input=RrHistoryInput(),
            output=RrHistoryOutput(),
        )

    def run(self, params={}):
        domain = params.get(Input.DOMAIN)
        type_ = params.get(Input.TYPE)

        try:
            if not type_:
                rr_history = self.connection.investigate.rr_history(domain)
            else:
                rr_history = self.connection.investigate.rr_history(domain, type_)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        return {Output.FEATURES: [rr_history.get("features")], Output.RRS_TF: rr_history.get("rrs_tf")}
