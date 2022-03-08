import insightconnect_plugin_runtime
from .schema import GetScanEnginesInput, GetScanEnginesOutput

# Custom imports below
import re
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetScanEngines(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scan_engines",
            description="List scan engines paired with the security console",
            input=GetScanEnginesInput(),
            output=GetScanEnginesOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        name = params.get("name")
        address = params.get("address")
        endpoint = endpoints.ScanEngine.scan_engines(self.connection.console_url)
        engines = resource_helper.resource_request(endpoint=endpoint)

        # Not paged for some reason...
        engines = engines["resources"]

        # Process filters
        if name == "":
            name = None
        if address == "":
            address = None

        if name:
            regex = re.compile(name, re.IGNORECASE)
            filtered_engines = []
            for e in engines:
                if regex.match(e["name"]):
                    filtered_engines.append(e)
            self.logger.info("Returning %d scan engines based on filters..." % (len(filtered_engines)))
            engines = filtered_engines

        if address:
            regex = re.compile(address, re.IGNORECASE)
            filtered_engines = []
            for e in engines:
                if regex.match(e["address"]):
                    filtered_engines.append(e)
            self.logger.info("Returning %d scan engines based on filters..." % (len(filtered_engines)))
            engines = filtered_engines

        # Remove the default engine pool if it's in the list...
        for idx, e in enumerate(engines):
            if e["name"] == "Default Engine Pool":
                del engines[idx]

        # Request engine pools separately because the API is broken atm
        for e in engines:
            endpoint = endpoints.ScanEngine.scan_engine_pools(self.connection.console_url, e["id"])
            scan_engine_pools_response = resource_helper.resource_request(endpoint=endpoint)
            pools = []
            for pool in scan_engine_pools_response["resources"]:
                pools.append(pool["id"])
            e["enginePools"] = pools

        return {"scan_engines": engines}
