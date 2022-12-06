import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetUserContactInput, GetUserContactOutput, Input, Output, Component

# Custom imports below
from icon_google_directory.util.tools import Message, return_contact_information


class GetUserContact(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_contact",
            description=Component.DESCRIPTION,
            input=GetUserContactInput(),
            output=GetUserContactOutput(),
        )

    def run(self, params={}):
        email = params.get(Input.EMAIL)
        try:
            response = self.connection.service.users().get(userKey=email).execute()
            if response:
                return {Output.CONTACT: return_contact_information(response)}
        except Exception:
            raise PluginException(cause=Message.USER_CONTACT_CAUSE, assistance=Message.USER_CONTACT_ASSISTANCE)
