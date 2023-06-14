import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import convert_dict_to_camel_case
from .schema import AddUserInput, AddUserOutput, Input, Output, Component

# Custom imports below
from komand_duo_admin.util.constants import Cause, Assistance, MAX_ALIASES_NUMBER
from komand_duo_admin.util.helpers import clean


class AddUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_user",
            description=Component.DESCRIPTION,
            input=AddUserInput(),
            output=AddUserOutput(),
        )

    def run(self, params={}):
        aliases = params.get(Input.ALIASES)

        if len(aliases) > MAX_ALIASES_NUMBER:
            raise PluginException(cause=Cause.INVALID_REQUEST, assistance=Assistance.ALIASES_NUMBER_EXCEEDED)

        aliases_object = {}
        if aliases:
            for index, value in enumerate(aliases, 1):
                aliases_object[f"alias{index}"] = value

        data = {
            "username": params.get(Input.USERNAME),
            "realname": params.get(Input.REALNAME),
            "status": params.get(Input.STATUS),
            "notes": params.get(Input.NOTES),
            "email": params.get(Input.EMAIL),
            "firstname": params.get(Input.FIRSTNAME),
            "lastname": params.get(Input.LASTNAME),
            **aliases_object,
        }

        return {
            Output.USER: clean(convert_dict_to_camel_case(self.connection.admin_api.add_user(data).get("response", {})))
        }
