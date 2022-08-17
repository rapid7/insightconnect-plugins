import insightconnect_plugin_runtime
from .schema import DownloadMaliciousFileInput, DownloadMaliciousFileOutput, Input, Output, Component

# Custom imports below


class DownloadMaliciousFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="download_malicious_file",
            description=Component.DESCRIPTION,
            input=DownloadMaliciousFileInput(),
            output=DownloadMaliciousFileOutput(),
        )

    def run(self, params={}):
        return {
            Output.CONTENT: self.connection.api.download_malicious_file(params.get(Input.ALERT_ID)),
            Output.SUCCESS: True,
        }
