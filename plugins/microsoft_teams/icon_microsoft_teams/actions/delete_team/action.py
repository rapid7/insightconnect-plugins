import insightconnect_plugin_runtime
from .schema import DeleteTeamInput, DeleteTeamOutput, Input, Output, Component


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

        group_id = self.connection.client.get_group_id_from_name(team_name)
        success = self.connection.client.delete_group(group_id)

        return {Output.SUCCESS: success}
