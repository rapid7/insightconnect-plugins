import insightconnect_plugin_runtime
from .schema import GetUsersInput, GetUsersOutput, Input, Output, Component

# Custom imports below
from icon_zscaler.util.helpers import clean_dict


class GetUsers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_users", description=Component.DESCRIPTION, input=GetUsersInput(), output=GetUsersOutput()
        )

    def run(self, params={}):
        self.logger.info(f"Getting list of users with filter: {params}.\n")

        parameters = {
            "name": params.get(Input.NAME),
            "dept": params.get(Input.DEPARTMENT),
            "group": params.get(Input.GROUP),
            "page": params.get(Input.PAGE),
            "pageSize": params.get(Input.PAGESIZE),
        }

        return {Output.USERS: self.connection.client.get_users(clean_dict(parameters))}
