import insightconnect_plugin_runtime
from .schema import SampleArtifactsInput, SampleArtifactsOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class SampleArtifacts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="sample_artifacts",
            description="Return artifacts which are files created or modified during a sample analysis",
            input=SampleArtifactsInput(),
            output=SampleArtifactsOutput(),
        )

    def run(self, params={}):
        hash_ = params.get(Input.HASH)
        limit = params.get(Input.LIMIT)
        offset = params.get(Input.OFFSET)

        if not limit or limit == 0:
            limit = 10

        if not offset:
            offset = 0

        try:
            sample_artifacts = self.connection.investigate.sample_artifacts(hash_, limit=limit, offset=offset)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        if "error" in sample_artifacts:
            raise PluginException(
                cause="Unable to return artifact data.",
                assistance="Only Threat Grid customers have access to artifact data.",
            )

        return sample_artifacts
