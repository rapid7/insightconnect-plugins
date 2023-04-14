import insightconnect_plugin_runtime
from .schema import CooccurrencesInput, CooccurrencesOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Cooccurrences(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="cooccurrences",
            description="Return co-occurences for the specified domain",
            input=CooccurrencesInput(),
            output=CooccurrencesOutput(),
        )

    def run(self, params={}):
        domain = params.get(Input.DOMAIN)

        try:
            cooccurrences = self.connection.investigate.cooccurrences(domain)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        founded = cooccurrences.get("found")
        if founded:
            self.logger.info("Found Co-occurences")
            return {Output.COOCCURRENCES: cooccurrences.get("pfs2")}

        self.logger.info("No Co-occurences found")
        return {Output.COOCCURRENCES: []}
