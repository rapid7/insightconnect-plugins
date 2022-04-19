import insightconnect_plugin_runtime
from .schema import RemoveScanEnginePoolEngineInput, RemoveScanEnginePoolEngineOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class RemoveScanEnginePoolEngine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_scan_engine_pool_engine",
            description="Remove a scan engine from a scan engine pool",
            input=RemoveScanEnginePoolEngineInput(),
            output=RemoveScanEnginePoolEngineOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        engine_pool_id = params.get("pool_id")
        engine_id = params.get("engine_id")
        endpoint = endpoints.ScanEnginePool.scan_engine_pool_engines(self.connection.console_url, engine_pool_id)

        response = resource_helper.resource_request(endpoint=endpoint)
        current_engines = response["resources"]

        if engine_id in current_engines:
            self.logger.info("Removing scan engine from the pool...")
            endpoint = endpoints.ScanEnginePool.scan_engine_pool_engines(
                self.connection.console_url, engine_pool_id, engine_id
            )
            response = resource_helper.resource_request(endpoint=endpoint, method="delete")
            return response
        else:
            self.logger.info("Engine was not found in list of associated engines for the pool...")
            return {"links": response["links"]}
