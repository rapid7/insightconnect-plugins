import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import convert_dict_to_camel_case
from .schema import GetUserByIdInput, GetUserByIdOutput, Input, Output, Component

# Custom imports below
from komand_duo_admin.util.helpers import clean


class GetUserById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_by_id",
            description=Component.DESCRIPTION,
            input=GetUserByIdInput(),
            output=GetUserByIdOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.USERID)
        self.logger.info(f"Getting user by ID: {user_id}")
        return {
            Output.USER: convert_dict_to_camel_case(
                clean(self.connection.admin_api.get_user_by_id(user_id).get("response", {}))
            )
        }
