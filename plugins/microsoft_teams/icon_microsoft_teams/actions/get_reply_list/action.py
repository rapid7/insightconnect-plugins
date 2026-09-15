import insightconnect_plugin_runtime
from .schema import GetReplyListInput, GetReplyListOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class GetReplyList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_reply_list",
            description=Component.DESCRIPTION,
            input=GetReplyListInput(),
            output=GetReplyListOutput(),
        )

    def run(self, params={}):
        team_name = params.get(Input.TEAM_NAME)
        channel_name = params.get(Input.CHANNEL_NAME)
        message_id = params.get(Input.MESSAGE_ID)

        teams = self.connection.client.get_teams(team_name)
        if not teams:
            raise PluginException(
                cause="Team not found.",
                assistance="Please verify the team name is correct.",
            )

        team_id = teams[0].get("id")
        channels = self.connection.client.get_channels(team_id, channel_name)
        if not channels:
            raise PluginException(
                cause="Channel not found.",
                assistance="Please verify the channel name is correct.",
            )

        channel_id = channels[0].get("id")
        messages = self.connection.client.get_message_replies(team_id, channel_id, message_id)

        return {Output.MESSAGES: messages}
