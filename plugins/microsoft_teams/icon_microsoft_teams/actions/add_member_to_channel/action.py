import insightconnect_plugin_runtime
from .schema import AddMemberToChannelInput, AddMemberToChannelOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AddMemberToChannel(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_member_to_channel",
            description=Component.DESCRIPTION,
            input=AddMemberToChannelInput(),
            output=AddMemberToChannelOutput(),
        )

    def run(self, params={}):
        group_name = params.get(Input.GROUP_NAME)
        channel_name = params.get(Input.CHANNEL_NAME)
        member_login = params.get(Input.MEMBER_LOGIN)
        role = params.get(Input.ROLE, "Member").lower()

        group_id = self.connection.client.get_group_id_from_name(group_name)
        channels = self.connection.client.get_channels(group_id, channel_name)

        try:
            channel_id = channels[0].get("id")
        except (IndexError, TypeError) as error:
            raise PluginException(
                cause="The specified channel does not exist.",
                assistance="Please check that channel name is correct.",
                data=str(error),
            ) from error

        if not channel_id:
            raise PluginException(
                cause="The specified channel does not exist.",
                assistance="Please check that channel name is correct.",
            )

        user = self.connection.client.get_user_info(member_login)
        user_id = user.get("id")

        if not user_id:
            raise PluginException(
                cause="The specified user does not exist.",
                assistance="Please check that member login is correct.",
            )

        success = self.connection.client.add_member_to_channel(group_id, channel_id, user_id, role)

        return {Output.SUCCESS: success}
