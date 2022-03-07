import insightconnect_plugin_runtime
from .schema import GetChannelsForTeamInput, GetChannelsForTeamOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.teams_utils import (
    get_teams_from_microsoft,
    get_channels_from_microsoft,
)
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

        team_array = get_teams_from_microsoft(self.logger, self.connection, team_name)
        team = team_array[0]

        team_id = team.get("id")

        channels = get_channels_from_microsoft(self.logger, self.connection, team_id, channel_name)
        clean_channels = []
        for channel in channels:
            clean_channels.append(remove_null_and_clean(channel))

        return {Output.CHANNELS: clean_channels}
