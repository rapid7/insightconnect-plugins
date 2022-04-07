import insightconnect_plugin_runtime
from .schema import DeleteTeamInput, DeleteTeamOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.azure_ad_utils import delete_group


class DeleteTeam(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_team",
            description=Component.DESCRIPTION,
            input=DeleteTeamInput(),
            output=DeleteTeamOutput(),
        )

    def run(self, params={}):
        team_name = params.get(Input.TEAM_NAME)
        success = delete_group(self.logger, self.connection, team_name)
        return {Output.SUCCESS: success}
