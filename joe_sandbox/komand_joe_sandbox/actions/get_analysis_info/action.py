import komand
from .schema import GetAnalysisInfoInput, GetAnalysisInfoOutput, Input, Output
# Custom imports below
from komand.helper import clean


class GetAnalysisInfo(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_analysis_info',
                description='Show the status and most important attributes of an analysis',
                input=GetAnalysisInfoInput(),
                output=GetAnalysisInfoOutput())

    def run(self, params={}):
        webid = params.get('webid')

        analysis = self.connection.api.info(webid)
        return {'analysis': clean(analysis)}
