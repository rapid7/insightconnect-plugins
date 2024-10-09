import insightconnect_plugin_runtime
import os
from .schema import BasenameInput, BasenameOutput, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException


class Basename(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="basename",
            description="Get the basename of a path",
            input=BasenameInput(),
            output=BasenameOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        path = params.get(Input.PATH, "")
        # END INPUT BINDING - DO NOT REMOVE

        basename = os.path.basename(path)
        if not basename:
            raise PluginException(
                cause="Unable to find basename.",
                assistance=f"Not able to retrieve basename of {path}.",
            )
        return {Output.BASENAME: basename}
