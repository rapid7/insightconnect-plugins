import insightconnect_plugin_runtime
from .schema import GetRolesInput, GetRolesOutput

# Custom imports below
import re
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetRoles(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_roles",
            description="List role details",
            input=GetRolesInput(),
            output=GetRolesOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.Role.roles(self.connection.console_url)
        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(endpoint)["resources"]

        # Filter response
        name = params.get("name")
        if name and (name != ""):
            name_regex = re.compile(name, re.IGNORECASE)
            response = [r for r in response if name_regex.match(r["name"])]
            self.logger.info(f"Returning {len(response)} results based on filter...")

        # Patch records with no privileges key
        for r in response:
            if "privileges" not in r:
                r["privileges"] = []

        return {"roles": response}
