import komand
from .schema import DownloadAnalysisInput, DownloadAnalysisOutput, Input, Output
# Custom imports below
from base64 import b64encode


class DownloadAnalysis(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='download_analysis',
                description='Download a resource for an analysis. This can be a full report, binaries, screenshots, etc',
                input=DownloadAnalysisInput(),
                output=DownloadAnalysisOutput())

    def run(self, params={}):
        webid = params.get('webid')
        run = params.get('run')
        type_ = params.get('type', 'html')

        resource_name, resource_content = self.connection.api.download(
            webid, type_, run
        )
        return {
            'resource_name': resource_name,
            'resource_content': b64encode(resource_content).decode()
        }
