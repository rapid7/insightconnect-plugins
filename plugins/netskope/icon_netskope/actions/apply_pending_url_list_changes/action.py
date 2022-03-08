import insightconnect_plugin_runtime

from .schema import ApplyPendingUrlListChangesInput, ApplyPendingUrlListChangesOutput, Component, Output


class ApplyPendingUrlListChanges(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="apply_pending_url_list_changes",
            description=Component.DESCRIPTION,
            input=ApplyPendingUrlListChangesInput(),
            output=ApplyPendingUrlListChangesOutput(),
        )

    def run(self, params={}):
        # pylint: disable=unused-argument
        return {Output.DEPLOYED_URLLISTS: self.connection.client.apply_pending_url_list_changes()}
