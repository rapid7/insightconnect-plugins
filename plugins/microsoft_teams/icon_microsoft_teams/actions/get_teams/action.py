import insightconnect_plugin_runtime
from .schema import GetTeamsInput, GetTeamsOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean
from icon_microsoft_teams.util.teams_utils import get_teams_from_microsoft


class GetTeams(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_teams",
            description=Component.DESCRIPTION,
            input=GetTeamsInput(),
            output=GetTeamsOutput(),
        )

    def run(self, params={}):
        team_name = params.get(Input.TEAM_NAME, "")

        # The end of this filters for only MS Team enabled Teams
        teams = get_teams_from_microsoft(self.logger, self.connection, team_name, False)

        clean_teams = []
        for team in teams:
            clean_teams.append(remove_null_and_clean(team))

        return {Output.TEAMS: clean_teams}
