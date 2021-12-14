import insightconnect_plugin_runtime
from .schema import UpdateGroupInput, UpdateGroupOutput, Input, Output, Component
# Custom imports below


class UpdateGroup(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_group',
                description=Component.DESCRIPTION,
                input=UpdateGroupInput(),
                output=UpdateGroupOutput())

    def run(self, params={}):
        # Retrieve current group settings to be used as fallback if not provided as input
        current_group_settings = self.current_group_settings(params.get(Input.ORG_ID), params.get(Input.GROUP_ID))

        payload = {
            "name": params.get(Input.NAME, current_group_settings["name"]),
            "refresh_interval": params.get(Input.REFRESH_INTERVAL, current_group_settings["refresh_interval"]),
            "parent_server_group_id": params.get(Input.PARENT_SERVER_GROUP_ID,
                                                 current_group_settings["parent_server_group_id"]),
            "ui_color": params.get(Input.COLOR, current_group_settings["ui_color"]),
            "notes": params.get(Input.NOTES, current_group_settings["notes"]),
            "enable_os_auto_update": None,
            "enable_wsus": None,
            "policies": params.get(Input.POLICIES, current_group_settings["policies"])
        }
        self.connection.automox_api.update_group(params.get(Input.ORG_ID), params.get(Input.GROUP_ID), payload)

        return {Output.SUCCESS: True}

    def current_group_settings(self, org_id, group_id):
        # Get Current Group Settings for defaults
        for group in self.connection.automox_api.get_groups(org_id, False):
            if group_id == group.get("id"):
                return group
