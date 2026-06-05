import insightconnect_plugin_runtime
from .schema import CreateGroupInput, CreateGroupOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class CreateGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_group", description=Component.DESCRIPTION, input=CreateGroupInput(), output=CreateGroupOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        name = params.get(Input.NAME, "").strip()
        refresh_interval = params.get(Input.REFRESH_INTERVAL, 1440)
        parent_server_group_id = params.get(Input.PARENT_SERVER_GROUP_ID, 0)
        color = params.get(Input.COLOR, "")
        notes = params.get(Input.NOTES, "")
        policies = params.get(Input.POLICIES, [])
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        if refresh_interval <= 0:
            raise PluginException(cause="Invalid input", assistance="Refresh Interval must be a positive integer")

        default_server_group_id = self.default_server_group(org_id)
        payload = {
            "name": name,
            "refresh_interval": refresh_interval,
            "parent_server_group_id": parent_server_group_id or default_server_group_id,
            "ui_color": color,
            "notes": notes,
            "policies": policies,
        }
        group = self.connection.automox_api.create_group(org_id, payload)
        self.logger.info("Group Successfully Created")
        return {Output.SUCCESS: True, Output.GROUP: self.connection.automox_api.remove_null_values(group)}

    def default_server_group(self, org_id):
        # Get Default Server Group id for org
        default_server_group_id = 0
        for group in self.connection.automox_api.get_groups(org_id):
            if not group.get("name"):
                default_server_group_id = group.get("id")
                break
        return default_server_group_id
