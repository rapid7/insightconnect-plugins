import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import TagAssetsInput, TagAssetsOutput, Input, Output, Component

# Custom imports below


class TagAssets(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="tag_assets",
            description=Component.DESCRIPTION,
            input=TagAssetsInput(),
            output=TagAssetsOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        object_ids = params.get(Input.OBJECT_IDS)
        tags = params.get(Input.TAGS)
        operation = params.get(Input.OPERATION)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.api.tag_assets(
            object_ids=object_ids, tags=tags, operation=operation
        )
        return {
            Output.SUCCESS_COUNT: result["success_count"],
            Output.FAILURE_COUNT: result["failure_count"],
            Output.FAILURES: result["failures"],
        }
