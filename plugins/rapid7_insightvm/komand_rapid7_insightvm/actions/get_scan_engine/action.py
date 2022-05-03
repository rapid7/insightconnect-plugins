import insightconnect_plugin_runtime
from .schema import GetScanEngineInput, GetScanEngineOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetScanEngine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scan_engine",
            description="Get a scan engine by ID",
            input=GetScanEngineInput(),
            output=GetScanEngineOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        engine_id = params.get("id")
        endpoint = endpoints.ScanEngine.scan_engines(self.connection.console_url, engine_id)
        scan_engine_response = resource_helper.resource_request(endpoint=endpoint)

        # Request engine pools separately because the API is broken atm
        endpoint = endpoints.ScanEngine.scan_engine_pools(self.connection.console_url, engine_id)
        scan_engine_pools_response = resource_helper.resource_request(endpoint=endpoint)
        pools = []
        for pool in scan_engine_pools_response["resources"]:
            pools.append(pool["id"])
        scan_engine_response["enginePools"] = pools

        return {"scan_engine": scan_engine_response}
