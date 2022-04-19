import insightconnect_plugin_runtime
from .schema import DeleteScanEngineInput, DeleteScanEngineOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class DeleteScanEngine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_scan_engine",
            description="Delete an existing scan engine from the security console",
            input=DeleteScanEngineInput(),
            output=DeleteScanEngineOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        engine_id = params.get("id")
        endpoint = endpoints.ScanEngine.scan_engines(self.connection.console_url, engine_id)
        response = resource_helper.resource_request(endpoint=endpoint, method="delete")

        return response
