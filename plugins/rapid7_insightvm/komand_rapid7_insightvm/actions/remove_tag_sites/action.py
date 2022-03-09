import insightconnect_plugin_runtime
from .schema import RemoveTagSitesInput, RemoveTagSitesOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class RemoveTagSites(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_tag_sites",
            description="Removes all site associations from a tag",
            input=RemoveTagSitesInput(),
            output=RemoveTagSitesOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        site_id = params.get("id")
        endpoint = endpoints.Tag.tag_sites(self.connection.console_url, site_id)
        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(endpoint=endpoint, method="delete")

        return response
