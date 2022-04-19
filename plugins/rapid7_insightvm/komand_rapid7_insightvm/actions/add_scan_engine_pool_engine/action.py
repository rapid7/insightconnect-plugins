import insightconnect_plugin_runtime
from .schema import AddScanEnginePoolEngineInput, AddScanEnginePoolEngineOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class AddScanEnginePoolEngine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_scan_engine_pool_engine",
            description="Add a scan engine to a scan engine pool (AWS pre-authorized engine AMI engines cannot be pooled)",
            input=AddScanEnginePoolEngineInput(),
            output=AddScanEnginePoolEngineOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        engine_pool_id = params.get("pool_id")
        engine = params.get("engine_id")
        endpoint = endpoints.ScanEnginePool.scan_engine_pool_engines(
            self.connection.console_url, engine_pool_id, engine_id=engine
        )
        self.logger.info("Adding scan engine to the pool...")
        response = resource_helper.resource_request(endpoint=endpoint, method="put")

        return response
