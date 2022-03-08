import insightconnect_plugin_runtime
from .schema import GetRoleInput, GetRoleOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetRole(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_role",
            description="Get role details by ID",
            input=GetRoleInput(),
            output=GetRoleOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.Role.roles(self.connection.console_url, params.get("id"))
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint)

        # Patch record if no privileges key
        if "privileges" not in response:
            response["privileges"] = []

        return {"role": response}
