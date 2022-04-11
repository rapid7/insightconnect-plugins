import insightconnect_plugin_runtime
from .schema import AddMemberToChannelInput, AddMemberToChannelOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.teams_utils import get_channels_from_microsoft
from icon_microsoft_teams.util.azure_ad_utils import (
    get_user_info,
    get_group_id_from_name,
    add_user_to_channel,
)
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
        group_id = get_group_id_from_name(self.logger, self.connection, params.get(Input.GROUP_NAME))
        channels = get_channels_from_microsoft(self.logger, self.connection, group_id, params.get(Input.CHANNEL_NAME))
        user_id = get_user_info(self.logger, self.connection, params.get(Input.MEMBER_LOGIN))
        try:
            channel_id = channels[0].get("id")
            user_id = user_id.get("id")
            if not channel_id:
                raise PluginException(
                    cause="The specified channel does not exist.",
                    assistance="Please check that channel name is correct.",
                )
            if not user_id:
                raise PluginException(
                    cause="The specified user does not exist.",
                    assistance="Please check that member login is correct.",
                )
        except IndexError as e:
            raise PluginException(
                cause="The specified channel does not exist.",
                assistance="If the issue persists please contact support.",
                data=e,
            )
        return {Output.SUCCESS: add_user_to_channel(self.logger, self.connection, group_id, channel_id, user_id)}
