import komand
from .schema import DeleteAnalysisInput, DeleteAnalysisOutput, Input, Output
# Custom imports below


class DeleteAnalysis(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_analysis',
                description='Delete an analysis',
                input=DeleteAnalysisInput(),
                output=DeleteAnalysisOutput())

    def run(self, params={}):
        webid = params.get('webid')

        deleted = self.connection.api.delete(webid)
        return deleted
