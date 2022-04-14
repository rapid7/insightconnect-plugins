import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from .schema import AddGroupMemberInput, AddGroupMemberOutput, Input, Output, Component
from komand_mimecast.util.constants import DATA_FIELD


class AddGroupMember(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_group_member",
            description=Component.DESCRIPTION,
            input=AddGroupMemberInput(),
            output=AddGroupMemberOutput(),
        )

    def run(self, params={}):
        email = params.get(Input.EMAIL_ADDRESS)
        domain = params.get(Input.DOMAIN)
        if not email and not domain:
            raise PluginException(
                cause="Invalid input.",
                assistance="Email Address and Domain inputs cannot both be blank.",
            )
        if email and domain:
            raise PluginException(
                cause="Invalid input.",
                assistance="Both Email Address and Domain fields cannot be used. Choose either Email Address or Domain.",
            )

        if email:
            data = {"id": params.get(Input.ID), "emailAddress": email}
        else:
            data = {"id": params.get(Input.ID), "domain": domain}

        response = self.connection.client.add_group_member(data).get(DATA_FIELD)[0]
        return {
            Output.ID: response.get("id"),
            Output.FOLDER_ID: response.get("folderId"),
            Output.EMAIL_ADDRESS: response.get("emailAddress"),
            Output.INTERNAL: response.get("internal"),
        }
