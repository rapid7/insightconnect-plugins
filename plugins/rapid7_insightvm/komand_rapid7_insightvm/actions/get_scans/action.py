import insightconnect_plugin_runtime
from .schema import GetScansInput, GetScansOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetScans(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_scans",
            description="Get scans with optional site filter",
            input=GetScansInput(),
            output=GetScansOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        site_id = params.get("id")
        state = params.get("active")
        params = {"active": state}

        #
        # If a filter was provided, first get the site name because it's not provided
        # in the results from the site scans endpoint and this action should be
        # consistent even when the API is not.
        #
        if site_id:
            endpoint = endpoints.Site.sites(self.connection.console_url, site_id)
            response = resource_helper.resource_request(endpoint)
            site_name = response["name"]

            endpoint = endpoints.Scan.site_scans(self.connection.console_url, site_id)
        else:
            site_name = None
            endpoint = endpoints.Scan.scans(self.connection.console_url)

        response = resource_helper.paged_resource_request(endpoint=endpoint, params=params)

        # Add the name and ID if necessary
        if site_id:
            for r in response:
                r["siteId"] = site_id
                r["siteName"] = site_name

        return {"scans": response}
