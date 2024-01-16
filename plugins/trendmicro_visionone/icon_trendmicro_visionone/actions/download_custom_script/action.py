import insightconnect_plugin_runtime
from .schema import DownloadCustomScriptInput, DownloadCustomScriptOutput, Input, Output, Component
# Custom imports below


class DownloadCustomScript(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='download_custom_script',
                description=Component.DESCRIPTION,
                input=DownloadCustomScriptInput(),
                output=DownloadCustomScriptOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
