import insightconnect_plugin_runtime
from .schema import DeleteSiteInput, DeleteSiteOutput, Input

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class DeleteSite(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_site",
            description="Delete an existing site",
            input=DeleteSiteInput(),
            output=DeleteSiteOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        self.logger.info(f"Deleting site ID {params.get(Input.ID)}")
        endpoint = endpoints.Site.sites(self.connection.console_url, params.get(Input.ID))

        response = resource_helper.resource_request(endpoint=endpoint, method="delete")

        return response
