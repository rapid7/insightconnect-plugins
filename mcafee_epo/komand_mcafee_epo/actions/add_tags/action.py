import insightconnect_plugin_runtime
from .schema import AddTagsInput, AddTagsOutput, Input, Output
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class AddTags(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='add_tags',
            description='Assigns the given tag to a supplied list of systems',
            input=AddTagsInput(),
            output=AddTagsOutput())

    def run(self, params=None):
        if params is None:
            params = {}
        try:
            for d in params.get(Input.DEVICES):
                self.connection.client(
                    'system.applyTag',
                    d,
                    params.get(Input.TAG)
                )
            self.logger.info(f"Applied to {len(params.get(Input.DEVICES))} devices")
            return {
                Output.MESSAGE: "Tags applied to devices successfully"
            }
        except Exception as e:
            raise PluginException(
                cause="Tags error",
                assistance="Tags could not be added to some or all devices. Please check tag name and device name.",
                data=e
            )
