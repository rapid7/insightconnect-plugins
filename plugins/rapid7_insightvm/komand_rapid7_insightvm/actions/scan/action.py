import insightconnect_plugin_runtime
from .schema import ScanInput, ScanOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class Scan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="scan",
            description="Start a scan on a site",
            input=ScanInput(),
            output=ScanOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)

        site_id = params.get("site_id")
        hosts = params.get("hosts")
        endpoint = endpoints.Scan.site_scans(self.connection.console_url, site_id)

        self.logger.info(f"Using {endpoint}")

        if hosts:
            payload = {"hosts": hosts}
            response = resource_helper.resource_request(endpoint=endpoint, method="post", payload=payload)
        else:
            response = resource_helper.resource_request(endpoint=endpoint, method="post")

        return response
