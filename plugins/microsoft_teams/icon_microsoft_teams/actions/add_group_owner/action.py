import insightconnect_plugin_runtime
from .schema import AddGroupOwnerInput, AddGroupOwnerOutput, Input, Output, Component

# Custom imports below
from icon_microsoft_teams.util.azure_ad_utils import (
    get_user_info,
    get_group_id_from_name,
    add_user_to_owners,
)
from insightconnect_plugin_runtime.exceptions import PluginException


class AddGroupOwner(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_group_owner",
            description=Component.DESCRIPTION,
            input=AddGroupOwnerInput(),
            output=AddGroupOwnerOutput(),
        )

    def run(self, params={}):
        user_id = get_user_info(self.logger, self.connection, params.get(Input.MEMBER_LOGIN))
        if not user_id or not user_id.get("id"):
            raise PluginException(
                cause="The specified user does not exist.",
                assistance="Please check that member login is correct.",
            )
        return {
            Output.SUCCESS: add_user_to_owners(
                self.logger,
                self.connection,
                get_group_id_from_name(self.logger, self.connection, params.get(Input.GROUP_NAME)),
                user_id.get("id"),
            )
        }
