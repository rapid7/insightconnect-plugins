import insightconnect_plugin_runtime
from .schema import ClearTagsInput, ClearTagsOutput, Input, Output
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class ClearTags(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name='clear_tags',
            description='Clears the given tag to a supplied list of systems',
            input=ClearTagsInput(),
            output=ClearTagsOutput())

    def run(self, params=None):
        if params is None:
            params = {}
        try:
            for d in params.get(Input.DEVICES):
                self.connection.client(
                    'system.clearTag',
                    d,
                    params.get(Input.TAG)
                )
            self.logger.info("Tag cleared from {} devices".format(len(params.get(Input.DEVICES))))
            return {
                Output.MESSAGE: "Tags cleared from devices successfully"
            }
        except Exception as e:
            raise PluginException(
                cause="Tags error",
                assistance=f"Tags could not be cleared from some or all devices. Error: {e}"
            )
