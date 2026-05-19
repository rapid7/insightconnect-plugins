import insightconnect_plugin_runtime
from .schema import RemoveMemberFromTeamInput, RemoveMemberFromTeamOutput, Input, Output, Component


class RemoveMemberFromTeam(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_member_from_team",
            description=Component.DESCRIPTION,
            input=RemoveMemberFromTeamInput(),
            output=RemoveMemberFromTeamOutput(),
        )

    def run(self, params={}):
        user_login = params.get(Input.MEMBER_LOGIN)
        team_name = params.get(Input.TEAM_NAME)

        user = self.connection.client.get_user_info(user_login)
        user_id = user.get("id")

        teams = self.connection.client.get_teams(team_name)
        group_id = teams[0].get("id")

        success = self.connection.client.remove_member_from_group(group_id, user_id)

        return {Output.SUCCESS: success}
