import insightconnect_plugin_runtime
from .schema import DeleteGroupInput, DeleteGroupOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below


class DeleteGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_group", description=Component.DESCRIPTION, input=DeleteGroupInput(), output=DeleteGroupOutput()
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        org_id = params.get(Input.ORG_ID, 0)
        group_id = params.get(Input.GROUP_ID, 0)
        # END INPUT BINDING - DO NOT REMOVE

        # Validation
        if org_id and org_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Organization ID must be a positive integer")

        if group_id <= 0:
            raise PluginException(cause="Invalid input", assistance="Group ID must be a positive integer")

        self.connection.automox_api.delete_group(org_id, group_id)
        return {Output.SUCCESS: True}
