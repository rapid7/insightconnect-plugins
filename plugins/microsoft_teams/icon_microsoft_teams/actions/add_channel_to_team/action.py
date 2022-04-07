import insightconnect_plugin_runtime
from .schema import AddChannelToTeamInput, AddChannelToTeamOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.teams_utils import get_teams_from_microsoft, create_channel


class AddChannelToTeam(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_channel_to_team",
            description=Component.DESCRIPTION,
            input=AddChannelToTeamInput(),
            output=AddChannelToTeamOutput(),
        )

    def run(self, params={}):
        team_name = params.get(Input.TEAM_NAME)
        channel_name = params.get(Input.CHANNEL_NAME)
        channel_description = params.get(Input.CHANNEL_DESCRIPTION)

        teams = get_teams_from_microsoft(self.logger, self.connection, team_name)
        team_id = teams[0].get("id")

        success = create_channel(self.logger, self.connection, team_id, channel_name, channel_description)

        return {Output.SUCCESS: success}
