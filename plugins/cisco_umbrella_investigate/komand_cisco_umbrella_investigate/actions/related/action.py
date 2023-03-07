import insightconnect_plugin_runtime
from .schema import RelatedInput, RelatedOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Related(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="related",
            description="Returns a list of domain names that have been frequently seen",
            input=RelatedInput(),
            output=RelatedOutput(),
        )

    def run(self, params={}):
        domain = params.get(Input.DOMAIN)
        try:
            related = self.connection.investigate.related(domain)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
        founded = related.get("found")
        if founded:
            return {"related": related.get("tb1")}

        self.logger.info("No results found")
        return {Output.RELATED: []}
