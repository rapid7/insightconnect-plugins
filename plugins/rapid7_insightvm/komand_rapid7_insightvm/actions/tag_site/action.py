import insightconnect_plugin_runtime
from .schema import TagSiteInput, TagSiteOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class TagSite(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="tag_site",
            description="Add a tag to a site",
            input=TagSiteInput(),
            output=TagSiteOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        site_id = params.get("site_id")
        tag_id = params.get("tag_id")
        endpoint = endpoints.Site.site_tags(self.connection.console_url, site_id, tag_id)
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint=endpoint, method="put")

        return response
