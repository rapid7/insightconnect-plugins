import insightconnect_plugin_runtime
from .schema import GetUsersInput, GetUsersOutput

# Custom imports below
import re
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetUsers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_users",
            description="List user accounts",
            input=GetUsersInput(),
            output=GetUsersOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.User.users(self.connection.console_url)
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.paged_resource_request(endpoint)

        # Filter response
        name = params.get("name")
        login = params.get("login")
        if name and (name != ""):
            name_regex = re.compile(name, re.IGNORECASE)
            response = [r for r in response if name_regex.match(r["name"])]
        if login and (login != ""):
            name_regex = re.compile(login, re.IGNORECASE)
            response = [r for r in response if name_regex.match(r["login"])]

        self.logger.info(f"Returning {len(response)} results based on filter...")

        return {"users": response}
