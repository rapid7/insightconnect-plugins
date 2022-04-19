import insightconnect_plugin_runtime
from .schema import GetSitesInput, GetSitesOutput

# Custom imports below
import re
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetSites(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_sites",
            description="Get a list of sites",
            input=GetSitesInput(),
            output=GetSitesOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        name = params.get("name")

        endpoint = endpoints.Site.sites(self.connection.console_url)
        self.logger.info(f"Using {endpoint}")

        sites = resource_helper.paged_resource_request(endpoint=endpoint)

        if name == "":
            name = None

        if name:
            regex = re.compile(name, re.IGNORECASE)
            filtered_sites = []
            for s in sites:
                if regex.match(s["name"]):
                    filtered_sites.append(s)
            self.logger.info(f"Returning {len(filtered_sites)} sites based on filters...")
            sites = filtered_sites

        return {"sites": sites}
