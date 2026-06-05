import insightconnect_plugin_runtime
from .schema import UpdateGroupInput, UpdateGroupOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class UpdateGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_group", description=Component.DESCRIPTION, input=UpdateGroupInput(), output=UpdateGroupOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        group_id = params.get(Input.GROUP_ID, 0)
        name = params.get(Input.NAME, "")
        refresh_interval = params.get(Input.REFRESH_INTERVAL, 0)
        parent_server_group_id = params.get(Input.PARENT_SERVER_GROUP_ID, 0)
        color = params.get(Input.COLOR, "")
        notes = params.get(Input.NOTES, "")
        policies = params.get(Input.POLICIES, [])
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        current_group_settings = self.connection.automox_api.get_group(org_id, group_id)

        payload = {
            "name": name or current_group_settings["name"],
            "refresh_interval": refresh_interval or current_group_settings["refresh_interval"],
            "parent_server_group_id": parent_server_group_id or current_group_settings["parent_server_group_id"],
            "ui_color": color or current_group_settings["ui_color"],
            "notes": notes or current_group_settings["notes"],
            "enable_os_auto_update": None,
            "enable_wsus": None,
            "policies": policies or current_group_settings["policies"],
        }
        self.connection.automox_api.update_group(org_id, group_id, payload)
        return {Output.SUCCESS: True}
