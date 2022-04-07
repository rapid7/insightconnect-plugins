import insightconnect_plugin_runtime
from .schema import (
    CreateTeamsEnabledGroupInput,
    CreateTeamsEnabledGroupOutput,
    Input,
    Component,
    Output,
)

# Custom imports below
from icon_microsoft_teams.util.azure_ad_utils import create_group, enable_teams_for_group
from icon_microsoft_teams.util.komand_clean_with_nulls import remove_null_and_clean


class CreateTeamsEnabledGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_teams_enabled_group",
            description=Component.DESCRIPTION,
            input=CreateTeamsEnabledGroupInput(),
            output=CreateTeamsEnabledGroupOutput(),
        )

    def run(self, params={}):
        group_name = params.get(Input.GROUP_NAME)
        group_description = params.get(Input.GROUP_DESCRIPTION)
        mail_nickname = params.get(Input.MAIL_NICKNAME)
        mail_enabled = params.get(Input.MAIL_ENABLED)
        owners = params.get(Input.OWNERS)
        members = params.get(Input.MEMBERS)

        group_result = create_group(
            self.logger,
            self.connection,
            group_name,
            group_description,
            mail_nickname,
            mail_enabled,
            owners,
            members,
        )

        group_id = group_result.get("id")

        enable_teams_for_group(self.logger, self.connection, group_id)

        return {Output.GROUP: remove_null_and_clean(group_result)}
