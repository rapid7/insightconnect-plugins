import insightconnect_plugin_runtime
from .schema import AvInput, AvOutput, Input, Output, Component

# Custom imports below


class Av(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="av", description=Component.DESCRIPTION, input=AvInput(), output=AvOutput()
        )

    def run(self, params={}):
        data = self.connection.client.antivirus_lookup(params.get(Input.ANTIVIRUS))
        if not data or int(data["response_code"]) == 0:
            self.logger.info("ThreatCrowd API did not return any matches.")
            return {Output.FOUND: False}

        return {
            Output.HASHES: insightconnect_plugin_runtime.helper.clean_list(data["hashes"]),
            Output.PERMALINK: data["permalink"],
            Output.REFERENCES: insightconnect_plugin_runtime.helper.clean_list(data["references"]),
            Output.FOUND: True,
        }
