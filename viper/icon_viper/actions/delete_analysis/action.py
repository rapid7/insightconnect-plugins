import komand
from .schema import DeleteAnalysisInput, DeleteAnalysisOutput, Input, Output, Component
from ...util import malware


class DeleteAnalysis(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_analysis',
                description=Component.DESCRIPTION,
                input=DeleteAnalysisInput(),
                output=DeleteAnalysisOutput())

    def run(self, params={}):
        malware.Malware(self.connection.config, params.get(Input.PROJECT_NAME), **{"sha256": params.get(Input.MALWARE_SHA256)})\
            .get_analysis(params.get(Input.ID)).delete()
        return {}
