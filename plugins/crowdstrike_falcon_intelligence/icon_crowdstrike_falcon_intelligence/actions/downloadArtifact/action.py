import insightconnect_plugin_runtime
from .schema import DownloadArtifactInput, DownloadArtifactOutput, Input, Output, Component

# Custom imports below

from icon_crowdstrike_falcon_intelligence.util.constants import TextCase
from icon_crowdstrike_falcon_intelligence.util.helpers import convert_dict_keys_case


class DownloadArtifact(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="downloadArtifact",
            description=Component.DESCRIPTION,
            input=DownloadArtifactInput(),
            output=DownloadArtifactOutput(),
        )

    def run(self, params: dict = None):
        return {
            Output.ARTIFACTS: convert_dict_keys_case(
                self.connection.api_client.download_artifact(params.get(Input.ID)), TextCase.CAMEL_CASE
            )
        }
