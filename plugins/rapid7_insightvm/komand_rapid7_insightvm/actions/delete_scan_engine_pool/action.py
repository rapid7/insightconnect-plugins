import insightconnect_plugin_runtime
from .schema import DeleteScanEnginePoolInput, DeleteScanEnginePoolOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class DeleteScanEnginePool(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_scan_engine_pool",
            description="Delete an existing scan engine pool from the security console",
            input=DeleteScanEnginePoolInput(),
            output=DeleteScanEnginePoolOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.ScanEnginePool.scan_engine_pools(self.connection.console_url, params["id"])

        response = resource_helper.resource_request(endpoint=endpoint, method="delete")

        return response
