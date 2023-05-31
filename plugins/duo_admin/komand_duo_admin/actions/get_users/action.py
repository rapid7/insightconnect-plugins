import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import convert_dict_to_camel_case
from .schema import GetUsersInput, GetUsersOutput, Output, Component

# Custom imports below
from komand_duo_admin.util.helpers import clean


class GetUsers(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_users",
            description=Component.DESCRIPTION,
            input=GetUsersInput(),
            output=GetUsersOutput(),
        )

    def run(self, params={}):
        self.logger.info("Getting users...")
        return {
            Output.USERS: convert_dict_to_camel_case(clean(self.connection.admin_api.get_users().get("response", [])))
        }
