import insightconnect_plugin_runtime
from .schema import AddGroupOwnerInput, AddGroupOwnerOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AddGroupOwner(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_group_owner",
            description=Component.DESCRIPTION,
            input=AddGroupOwnerInput(),
            output=AddGroupOwnerOutput(),
        )

    def run(self, params={}):
        user = self.connection.client.get_user_info(params.get(Input.MEMBER_LOGIN))
        user_id = user.get("id")

        if not user_id:
            raise PluginException(
                cause="The specified user does not exist.",
                assistance="Please check that member login is correct.",
            )

        group_id = self.connection.client.get_group_id_from_name(params.get(Input.GROUP_NAME))
        success = self.connection.client.add_group_owner(group_id, user_id)

        return {Output.SUCCESS: success}
