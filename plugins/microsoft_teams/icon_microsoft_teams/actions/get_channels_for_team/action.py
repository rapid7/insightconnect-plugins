import insightconnect_plugin_runtime
from .schema import GetChannelsForTeamInput, GetChannelsForTeamOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean


class GetChannelsForTeam(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_channels_for_team",
            description=Component.DESCRIPTION,
            input=GetChannelsForTeamInput(),
            output=GetChannelsForTeamOutput(),
        )

    def run(self, params={}):
        team_name = params.get(Input.TEAM_NAME)
        channel_name = params.get(Input.CHANNEL_NAME)

        teams = self.connection.client.get_teams(team_name)
        team_id = teams[0].get("id")

        channels = self.connection.client.get_channels(team_id, channel_name)

        clean_channels = []
        for channel in channels:
            clean_channels.append(remove_null_and_clean(channel))

        return {Output.CHANNELS: clean_channels}
