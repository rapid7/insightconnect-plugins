import insightconnect_plugin_runtime
from .schema import AddChannelToTeamInput, AddChannelToTeamOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


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
        channel_type = params.get(Input.CHANNEL_TYPE)

        teams = self.connection.client.get_teams(team_name)
        if not teams:
            raise PluginException(
                cause="Team not found.",
                assistance=f"Please verify '{team_name}' is a valid team name.",
            )
        team_id = teams[0].get("id")

        success = self.connection.client.create_channel(team_id, channel_name, channel_description, channel_type)

        return {Output.SUCCESS: success}
