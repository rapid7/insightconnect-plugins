import insightconnect_plugin_runtime
from .schema import CreateScanEnginePoolInput, CreateScanEnginePoolOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from insightconnect_plugin_runtime.exceptions import PluginException


class CreateScanEnginePool(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_scan_engine_pool",
            description="Create a new scan engine pool",
            input=CreateScanEnginePoolInput(),
            output=CreateScanEnginePoolOutput(),
        )

    def run(self, params={}):
        #
        # Note: ID is not a required payload parameter despite the API docs saying it is
        # Providing it actually causes the request to fail
        #
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.ScanEnginePool.scan_engine_pools(self.connection.console_url)

        if ("engines" not in params) or (("engines" in params) and (len(params["engines"]) == 0)):
            error = "At least 1 scan engine must be assigned to the scan engine pool for creation."
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        self.logger.info("Creating scan engine pool...")
        response = resource_helper.resource_request(endpoint=endpoint, method="post", payload=params)

        return response
