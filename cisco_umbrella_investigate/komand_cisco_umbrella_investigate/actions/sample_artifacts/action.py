import komand
from .schema import SampleArtifactsInput, SampleArtifactsOutput
# Custom imports below
from komand.exceptions import PluginException


class SampleArtifacts(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='sample_artifacts',
                description='Return artifacts which are files created or modified during a sample analysis',
                input=SampleArtifactsInput(),
                output=SampleArtifactsOutput())

    def run(self, params={}):
        hash = params.get('hash')
        limit = params.get('limit', None)
        offset = params.get('offset', None)
        
        if not limit or limit == 0:
            limit = 10
        
        if not offset:
            offset = 0

        try:
            sample_artifacts = self.connection.investigate.sample_artifacts(hash, limit=limit, offset=offset)
        except Exception as e:
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

        if "error" in sample_artifacts:
            raise PluginException(cause='Unable to return artifact data.', assistance='Only Threat Grid customers have access to artifact data.')

        return sample_artifacts

    def test(self):
        return {"artifacts": []}
