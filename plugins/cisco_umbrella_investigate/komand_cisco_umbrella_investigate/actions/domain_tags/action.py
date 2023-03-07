import insightconnect_plugin_runtime
from .schema import DomainTagsInput, DomainTagsOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class DomainTags(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain_tags",
            description="Returns the date range when the domain being queried was a part of the Umbrella block list",
            input=DomainTagsInput(),
            output=DomainTagsOutput(),
        )

    def run(self, params={}):
        domain = params.get(Input.DOMAIN)
        try:
            domain_tags = self.connection.investigate.domain_tags(domain)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        if not domain_tags:
            self.logger.info("DomainTags: Run: No results")
            return []

        domains = []
        for tag in domain_tags:
            url = ""
            if tag.get("url"):
                url = tag.get("url")
            domains.append(
                {
                    "begin": tag.get("period").get("begin"),
                    "end": tag.get("period").get("end"),
                    "category": tag.get("category"),
                    "url": url,
                }
            )
        return {Output.DOMAIN_TAGS: domains}
