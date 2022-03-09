import insightconnect_plugin_runtime
from .schema import UpdateUserSiteAccessInput, UpdateUserSiteAccessOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class UpdateUserSiteAccess(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_user_site_access",
            description="Update the sites to which a user has access in bulk. It can be used to remove sites as well",
            input=UpdateUserSiteAccessInput(),
            output=UpdateUserSiteAccessOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.User.user_sites(self.connection.console_url, params.get("user_id"))
        payload = params.get("site_ids")
        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=payload)

        return response
