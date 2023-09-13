import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetReplyListInput, GetReplyListOutput, Input, Output, Component

from icon_microsoft_teams.util.teams_utils import get_teams_from_microsoft, get_channels_from_microsoft, get_reply_list


class GetReplyList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_reply_list",
            description=Component.DESCRIPTION,
            input=GetReplyListInput(),
            output=GetReplyListOutput(),
        )

    def run(self, params={}):
        team = params.get(Input.TEAM_NAME)
        channel = params.get(Input.CHANNEL_NAME)
        message_id = params.get(Input.MESSAGE_ID)

        team_id, channel_id = "", ""
        teams = get_teams_from_microsoft(self.logger, self.connection, team)
        if teams and isinstance(teams, list):
            team_id = teams[0].get("id")
            channels = get_channels_from_microsoft(self.logger, self.connection, team_id, channel)
            if channels and isinstance(channels, list):
                channel_id = channels[0].get("id")

        if not team_id and not channel_id:
            raise PluginException(
                cause="No team ID with channel ID was provided.",
                assistance="Please provide the team and channel details(name or"
                " GUID) to send the message to a specific channel.",
            )

        messages = get_reply_list(self.connection, team_id, channel_id, message_id)
        return {Output.MESSAGES: messages}
