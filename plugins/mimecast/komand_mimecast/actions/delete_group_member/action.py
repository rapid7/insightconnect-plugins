import insightconnect_plugin_runtime
from .schema import DeleteGroupMemberInput, DeleteGroupMemberOutput, Input, Component, Output

# Custom imports below
from komand_mimecast.util.constants import ID_FIELD, DOMAIN_FIELD, EMAIL_FIELD
from insightconnect_plugin_runtime.exceptions import PluginException


class DeleteGroupMember(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_group_member",
            description=Component.DESCRIPTION,
            input=DeleteGroupMemberInput(),
            output=DeleteGroupMemberOutput(),
        )

    def run(self, params={}):
        group_id = params.get(Input.ID)
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
            data = {ID_FIELD: group_id, EMAIL_FIELD: email}
        else:
            data = {ID_FIELD: group_id, DOMAIN_FIELD: domain}

        self.connection.client.delete_group_member(data)
        return {Output.SUCCESS: True}
