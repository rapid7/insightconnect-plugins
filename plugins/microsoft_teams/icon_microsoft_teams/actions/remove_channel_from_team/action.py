import insightconnect_plugin_runtime
from .schema import (
    RemoveChannelFromTeamInput,
    RemoveChannelFromTeamOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


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

        teams = self.connection.client.get_teams(team_name)
        if not teams:
            raise PluginException(
                cause="Team not found.",
                assistance=f"Please verify '{team_name}' is a valid team name.",
            )
        team_id = teams[0].get("id")

        channels = self.connection.client.get_channels(team_id, channel_name)
        if not channels:
            raise PluginException(
                cause="Channel not found.",
                assistance=f"Please verify '{channel_name}' is a valid channel name.",
            )
        channel_id = channels[0].get("id")

        success = self.connection.client.delete_channel(team_id, channel_id)

        return {Output.SUCCESS: success}
