import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import convert_dict_to_camel_case
from .schema import ModifyUserInput, ModifyUserOutput, Input, Output, Component

# Custom imports below
from komand_duo_admin.util.helpers import clean


class ModifyUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="modify_user",
            description=Component.DESCRIPTION,
            input=ModifyUserInput(),
            output=ModifyUserOutput(),
        )

    def run(self, params={}):
        user_id = params.get(Input.USERID)
        user_status = params.get(Input.STATUS)
        self.logger.info(f"Updating user with ID: {user_id}")

        input_params = {
            "username": params.get(Input.USERNAME),
            "alias1": params.get(Input.ALIAS1),
            "alias2": params.get(Input.ALIAS2),
            "alias3": params.get(Input.ALIAS3),
            "alias4": params.get(Input.ALIAS4),
            "realname": params.get(Input.REALNAME),
            "email": params.get(Input.EMAIL),
            "status": None if user_status == "None" else user_status,
            "notes": params.get(Input.NOTES),
            "firstname": params.get(Input.FIRSTNAME),
            "lastname": params.get(Input.LASTNAME),
        }

        return {
            Output.USER: convert_dict_to_camel_case(
                clean(self.connection.admin_api.modify_user(user_id, clean(input_params)).get("response", {}))
            )
        }
