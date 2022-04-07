import insightconnect_plugin_runtime
from .schema import (
    RemoveChannelFromTeamInput,
    RemoveChannelFromTeamOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from icon_microsoft_teams.util.teams_utils import (
    get_teams_from_microsoft,
    get_channels_from_microsoft,
    delete_channel,
)


class RemoveChannelFromTeam(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_channel_from_team",
            description=Component.DESCRIPTION,
            input=RemoveChannelFromTeamInput(),
            output=RemoveChannelFromTeamOutput(),
        )

    def run(self, params={}):
        team_name = params.get(Input.TEAM_NAME)
        channel_name = params.get(Input.CHANNEL_NAME)

        teams = get_teams_from_microsoft(self.logger, self.connection, team_name)
        team_id = teams[0].get("id")
        channels = get_channels_from_microsoft(self.logger, self.connection, team_id, channel_name)
        channel_id = channels[0].get("id")

        success = delete_channel(self.logger, self.connection, team_id, channel_id)

        return {Output.SUCCESS: success}
