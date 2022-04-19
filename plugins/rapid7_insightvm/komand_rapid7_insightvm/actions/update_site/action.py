import insightconnect_plugin_runtime
from .schema import UpdateSiteInput, UpdateSiteOutput, Input

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class UpdateSite(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_site",
            description="Update an existing site",
            input=UpdateSiteInput(),
            output=UpdateSiteOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.Site.sites(self.connection.console_url, params.get(Input.ID))

        update_site = {
            "description": params.get(Input.DESCRIPTION),
            "engineId": params.get(Input.ENGINE_ID),
            "importance": params.get(Input.IMPORTANCE),
            "name": params.get(Input.NAME),
            "scanTemplateId": params.get(Input.SCAN_TEMPLATE_ID),
        }

        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=update_site)

        return {"id": params.get(Input.ID), "links": response["links"]}
