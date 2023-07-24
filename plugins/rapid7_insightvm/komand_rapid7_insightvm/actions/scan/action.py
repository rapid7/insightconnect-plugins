import insightconnect_plugin_runtime
from .schema import ScanInput, ScanOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class Scan(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="scan",
            description=Component.DESCRIPTION,
            input=ScanInput(),
            output=ScanOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)

        hosts = params.get(Input.HOSTS)
        endpoint = endpoints.Scan.site_scans(self.connection.console_url, params.get(Input.SITE_ID))

        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(
            endpoint=endpoint,
            method="post",
            payload={"hosts": hosts} if hosts else {},
            params={"overrideBlackout": params.get(Input.OVERRIDE_BLACKOUT)},
        )

        return {Output.ID: response.get("id"), Output.LINKS: response.get("links", [])}
