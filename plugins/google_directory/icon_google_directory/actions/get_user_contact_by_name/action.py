import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
import json
from .schema import GetUserContactByNameInput, GetUserContactByNameOutput, Input, Output, Component

# Custom imports below
from icon_google_directory.util.tools import return_contact_information_name, handle_service_error


class GetUserContactByName(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_contact_by_name",
            description=Component.DESCRIPTION,
            input=GetUserContactByNameInput(),
            output=GetUserContactByNameOutput(),
        )

    # def run(self, params={}):
    #     full_name = params.get(Input.FULL_NAME)
    #     try:
    #         response = (
    #             self.connection.service.users().list(customer="my_customer", query=f"name:'{full_name}'").execute()
    #         )
    #         return {Output.CONTACT: return_contact_information_name(response)}
    #     except Exception as exception:
    #         error = handle_service_error(exception)
    #         raise PluginException(cause=error.get("cause"), assistance=error.get("assistance"),
    #                               data=error.get("data"))

    def run(self, params={}):
        full_name = params.get(Input.FULL_NAME)
        try:
            response = (
                self.connection.service.users().list(customer="my_customer", query=f"name:'{full_name}'").execute()
            )
            if response.get("name") is not None:
                return {Output.CONTACT: return_contact_information_name(response)}
            else:
                error = handle_service_error((response.get("error")))
                raise PluginException(cause=error.get("cause"), assistance=error.get("assistance"),
                                      data=error.get("data"))
        except Exception as exception:
            error = handle_service_error(exception)
            raise PluginException(cause=error.get("cause"), assistance=error.get("assistance"),
                                  data=error.get("data"))
