import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetUserContactByNameInput, GetUserContactByNameOutput, Input, Output, Component
# Custom imports below
from icon_google_directory.util.tools import Message, return_contact_informations


class GetUserContactByName(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_user_contact_by_name',
            description=Component.DESCRIPTION,
            input=GetUserContactByNameInput(),
            output=GetUserContactByNameOutput()
        )

    def run(self, params={}):
        full_name = params.get(Input.NAME)
        try:
            response = self.connection.service.users().get(userKey=full_name).execute()
            if response:
                return {Output.CONTACT: return_contact_informations(response)}
        except Exception:
            raise PluginException(cause=Message.USER_CONTACT_CAUSE, assistance=Message.USER_CONTACT_ASSISTANCE)
