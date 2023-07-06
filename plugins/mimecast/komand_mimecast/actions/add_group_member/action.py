import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

# Custom imports below
from .schema import AddGroupMemberInput, AddGroupMemberOutput, Input, Output, Component
from komand_mimecast.util.constants import DATA_FIELD, ID_FIELD, DOMAIN_FIELD, EMAIL_FIELD


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
            data = {ID_FIELD: params.get(Input.ID), EMAIL_FIELD: email}
        else:
            data = {ID_FIELD: params.get(Input.ID), DOMAIN_FIELD: domain}

        response = self.connection.client.add_group_member(data).get(DATA_FIELD)[0]
        return clean(
            {
                Output.ID: response.get(ID_FIELD),
                Output.FOLDER_ID: response.get("folderId"),
                Output.EMAIL_ADDRESS: response.get(EMAIL_FIELD, ""),
                Output.INTERNAL: response.get("internal"),
            }
        )
