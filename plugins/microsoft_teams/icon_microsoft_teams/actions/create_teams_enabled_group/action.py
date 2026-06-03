import insightconnect_plugin_runtime
from .schema import (
    CreateTeamsEnabledGroupInput,
    CreateTeamsEnabledGroupOutput,
    Input,
    Component,
    Output,
)

# Custom imports below
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

        group_result = self.connection.client.create_group(
            group_name=group_name,
            group_description=group_description,
            group_nickname=mail_nickname,
            mail_enabled=mail_enabled,
            owners=owners,
            members=members,
        )

        group_id = group_result.get("id")
        self.connection.client.enable_teams_for_group(group_id)

        return {Output.GROUP: remove_null_and_clean(group_result)}
