import insightconnect_plugin_runtime
from .schema import GetScanEnginePoolInput, GetScanEnginePoolOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetScanEnginePool(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scan_engine_pool",
            description="Retrieve scan engine pool details by ID",
            input=GetScanEnginePoolInput(),
            output=GetScanEnginePoolOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        engine_pool_id = params.get("id")
        endpoint = endpoints.ScanEnginePool.scan_engine_pools(self.connection.console_url, engine_pool_id)
        response = resource_helper.resource_request(endpoint=endpoint)

        # Add the engines key if it is the Default Engine Pool
        if response["name"] == "Default Engine Pool":
            response["engines"] = []
        return {"scan_engine_pool": response}
