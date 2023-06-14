import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import convert_dict_to_camel_case
from .schema import GetPhonesByUserIdInput, GetPhonesByUserIdOutput, Input, Output, Component

# Custom imports below
from komand_duo_admin.util.helpers import clean


class GetPhonesByUserId(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_phones_by_user_id",
            description=Component.DESCRIPTION,
            input=GetPhonesByUserIdInput(),
            output=GetPhonesByUserIdOutput(),
        )

    def run(self, params={}):
        return {
            Output.PHONELIST: clean(
                convert_dict_to_camel_case(
                    self.connection.admin_api.get_phones_by_user_id(params.get(Input.USERID)).get("response", [])
                )
            )
        }
