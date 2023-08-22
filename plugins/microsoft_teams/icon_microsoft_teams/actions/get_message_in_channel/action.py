import insightconnect_plugin_runtime

from icon_microsoft_teams.util.teams_utils import get_message_from_channel
from .schema import GetMessageInChannelInput, GetMessageInChannelOutput, Input, Output, Component


class GetMessageInChannel(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_message_in_channel",
            description=Component.DESCRIPTION,
            input=GetMessageInChannelInput(),
            output=GetMessageInChannelOutput(),
        )

    def run(self, params={}):
        team_id = params.get(Input.TEAM_ID, "")
        channel_id = params.get(Input.CHANNEL_ID, "")
        message_id = params.get(Input.MESSAGE_ID, "")
        reply_id = params.get(Input.REPLY_ID, "")

        message = get_message_from_channel(self.connection, team_id, channel_id, message_id, reply_id)
        return {Output.MESSAGE: message}
