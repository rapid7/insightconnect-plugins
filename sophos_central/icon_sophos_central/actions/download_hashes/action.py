import insightconnect_plugin_runtime
from .schema import DownloadHashesInput, DownloadHashesOutput, Input, Output, Component
# Custom imports below


class DownloadHashes(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='download_hashes',
                description=Component.DESCRIPTION,
                input=DownloadHashesInput(),
                output=DownloadHashesOutput())

    def run(self, params={}):
        return {
            Output.HASHES: self.connection.client.download_hashes()
        }
