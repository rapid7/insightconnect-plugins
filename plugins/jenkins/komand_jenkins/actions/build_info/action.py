import insightconnect_plugin_runtime

from .schema import BuildInfoInput, BuildInfoOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class BuildInfo(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="build_info",
            description="Returns detailed information on a build",
            input=BuildInfoInput(),
            output=BuildInfoOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        name = params.get(Input.NAME)
        build_number = params.get(Input.BUILD_NUMBER)
        # END INPUT BINDING - DO NOT REMOVE

        try:
            output = self.connection.server.get_build_info(name, build_number)
            return {
                Output.BUILD_INFO: {
                    "building": output.get("building"),
                    "full_display_name": output.get("fullDisplayName", ""),
                    "keep_log": output.get("keepLog"),
                    "number": output.get("number"),
                    "queue_id": output.get("queueId"),
                    "result": output.get("result"),
                    "timestamp": output.get("timestamp"),
                    "url": output.get("url"),
                    "built_on": output.get("builtOn", ""),
                    "items": output.get("changeSet", {}).get("items", []),
                }
            }
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
