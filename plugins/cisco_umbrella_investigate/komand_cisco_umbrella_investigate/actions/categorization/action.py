import insightconnect_plugin_runtime
from .schema import CategorizationInput, CategorizationOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Categorization(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="categorization",
            description="Return if domain has been flagged as malicious by the Cisco Security Labs team",
            input=CategorizationInput(),
            output=CategorizationOutput(),
        )

    def run(self, params={}):

        domains = params.get(Input.DOMAINS)
        if len(domains) == 1:
            domains = str(domains[0])

        try:
            remoteCategories = self.connection.investigate.categorization(domains, labels=True)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        categories = []
        for key, value in remoteCategories.items():
            categories.append(
                {
                    "name": key,
                    "status": value.get("status"),
                    "security_categories": value.get("security_categories"),
                    "content_categories": value.get("content_categories"),
                }
            )

        return {Output.CATEGORIES: categories}
