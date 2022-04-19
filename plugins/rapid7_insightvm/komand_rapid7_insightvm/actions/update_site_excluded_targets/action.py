import insightconnect_plugin_runtime
from .schema import UpdateSiteExcludedTargetsInput, UpdateSiteExcludedTargetsOutput, Input

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class UpdateSiteExcludedTargets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_site_excluded_targets",
            description="Update an existing site scope of excluded ip address and hostname targets",
            input=UpdateSiteExcludedTargetsInput(),
            output=UpdateSiteExcludedTargetsOutput(),
        )

    def run(self, params={}):
        scope = params.get(Input.EXCLUDED_TARGETS)
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.Site.site_excluded_targets(self.connection.console_url, params.get(Input.ID))

        # Pull current site scope in order to append to list instead of overwriting
        if not params.get(Input.OVERWRITE):
            current_scope = resource_helper.resource_request(endpoint=endpoint, method="get")
            self.logger.info("Appending to current list of excluded targets")
            scope.extend(current_scope["addresses"])

        self.logger.info(f"Using {endpoint} ...")
        payload = {"rawbody": scope}
        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=payload)

        return {"id": params.get(Input.ID), "links": response["links"]}
