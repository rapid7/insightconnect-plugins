import insightconnect_plugin_runtime
from .schema import GetScanEnginePoolsInput, GetScanEnginePoolsOutput

# Custom imports below
import re
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetScanEnginePools(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scan_engine_pools",
            description="Retrieve a list of configured scan engine pools",
            input=GetScanEnginePoolsInput(),
            output=GetScanEnginePoolsOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        name = params.get("name")
        endpoint = endpoints.ScanEnginePool.scan_engine_pools(self.connection.console_url)
        engine_pools = resource_helper.resource_request(endpoint=endpoint)

        # Not paged for some reason...
        engine_pools = engine_pools["resources"]

        # Process filters
        if name == "":
            name = None

        if name:
            regex = re.compile(name, re.IGNORECASE)
            filtered_engine_pools = []
            for e in engine_pools:
                if regex.match(e["name"]):
                    filtered_engine_pools.append(e)
            self.logger.info(f"Returning {len(filtered_engine_pools)} scan engine pools based on filters...")
            engine_pools = filtered_engine_pools

        # Add an engines key to the default engine pool if it's in the list...
        for e in engine_pools:
            if e["name"] == "Default Engine Pool":
                e["engines"] = []

        return {"scan_engine_pools": engine_pools}
