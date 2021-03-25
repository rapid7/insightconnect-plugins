import insightconnect_plugin_runtime
from .schema import ManageTagsInput, ManageTagsOutput, Input, Output, Component

# Custom imports below


class ManageTags(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="manage_tags", description=Component.DESCRIPTION, input=ManageTagsInput(), output=ManageTagsOutput()
        )

    def run(self, params={}):
        self.logger.info("Running...")
        if params.get(Input.TYPE):
            action_type = "Add"
        else:
            action_type = "Remove"
        return {
            Output.MANAGE_TAGS_RESPONSE: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.manage_tags(
                    self.connection.client.find_machine_id(params.get(Input.MACHINE)),
                    params.get(Input.TAG),
                    action_type,
                )
            )
        }
