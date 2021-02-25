import komand
from .schema import CooccurrencesInput, CooccurrencesOutput

# Custom imports below
from komand.exceptions import PluginException


class Cooccurrences(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="cooccurrences",
            description="Return co-occurences for the specified domain",
            input=CooccurrencesInput(),
            output=CooccurrencesOutput(),
        )

    def run(self, params={}):
        domain = params.get("domain")

        try:
            cooccurrences = self.connection.investigate.cooccurrences(domain)
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=e)

        founded = cooccurrences.get("found")
        if founded:
            self.logger.info("Found Co-occurences")
            return {"cooccurrences": cooccurrences.get("pfs2")}

        self.logger.info("No Co-occurences found")
        return {"cooccurrences": []}

    def test(self):
        return {"cooccurrences": []}
