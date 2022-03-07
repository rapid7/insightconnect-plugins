import insightconnect_plugin_runtime
from .schema import AddMemberToTeamInput, AddMemberToTeamOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.azure_ad_utils import get_user_info, add_user_to_group
from icon_microsoft_teams.util.teams_utils import get_teams_from_microsoft


class AddMemberToTeam(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_member_to_team",
            description=Component.DESCRIPTION,
            input=AddMemberToTeamInput(),
            output=AddMemberToTeamOutput(),
        )

    def run(self, params={}):
        user_login = params.get(Input.MEMBER_LOGIN)
        team_name = params.get(Input.TEAM_NAME)

        # Get User ID
        user_result = get_user_info(self.logger, self.connection, user_login)
        user_id = user_result.get("id")

        # Get Group ID
        teams_result = get_teams_from_microsoft(self.logger, self.connection, team_name)
        group_id = teams_result[0].get("id")

        # Add user to Group
        success = add_user_to_group(self.logger, self.connection, group_id, user_id)

        return {Output.SUCCESS: success}
