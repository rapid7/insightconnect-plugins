import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetUserContactByNameInput, GetUserContactByNameOutput, Input, Output, Component

# Custom imports below
from icon_google_directory.util.tools import return_contact_information_name, Message


class GetUserContactByName(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_contact_by_name",
            description=Component.DESCRIPTION,
            input=GetUserContactByNameInput(),
            output=GetUserContactByNameOutput(),
        )

    def run(self, params={}):
        full_name = params.get(Input.FULL_NAME)
        try:
            # Generate response with full_name input
            response = (
                self.connection.service.users().list(customer="my_customer", query=f"name:'{full_name}'").execute()
            )
            if "users" in response.keys():
                return {Output.CONTACT: return_contact_information_name(response)}
            else:
                raise PluginException("User not found")

        # Handles all errors
        except Exception as error:
            raise PluginException(
                cause=Message.USER_CONTACT_CAUSE, assistance=Message.USER_CONTACT_ASSISTANCE, data=error
            )
