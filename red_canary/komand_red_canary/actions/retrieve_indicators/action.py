import komand
from .schema import RetrieveIndicatorsInput, RetrieveIndicatorsOutput
# Custom imports below


class RetrieveIndicators(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_indicators',
                description='Fetches a list of all indicators of compromise '
                'associated with all confirmed detections',
                input=RetrieveIndicatorsInput(),
                output=RetrieveIndicatorsOutput())

    def run(self, params={}):
        detection_id = params.get('detection_id')
        max_results = params.get('max_results', 100)

        indicators = self.connection.api.retrieve_indicators(
            detection_id, max_results
        )
        return {'indicators': indicators}
