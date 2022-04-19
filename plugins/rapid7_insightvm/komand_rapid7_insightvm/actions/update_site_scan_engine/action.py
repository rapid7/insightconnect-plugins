import insightconnect_plugin_runtime
from .schema import UpdateSiteScanEngineInput, UpdateSiteScanEngineOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class UpdateSiteScanEngine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_site_scan_engine",
            description="Update the scan engine/scan engine pool associated with a site",
            input=UpdateSiteScanEngineInput(),
            output=UpdateSiteScanEngineOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        site_id = params.get("site_id")
        engine_id = params.get("engine_id")
        endpoint = endpoints.Site.site_engine(self.connection.console_url, site_id)

        self.logger.info("Updating site scan engine...")
        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=engine_id)

        return response
