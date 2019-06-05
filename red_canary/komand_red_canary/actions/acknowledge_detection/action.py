import komand
from .schema import AcknowledgeDetectionInput, AcknowledgeDetectionOutput
# Custom imports below


class AcknowledgeDetection(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='acknowledge_detection',
                description='Marks detection as acknowledged',
                input=AcknowledgeDetectionInput(),
                output=AcknowledgeDetectionOutput())

    def run(self, params={}):
        detection = self.connection.api.acknowledge_detection(
            params['detection_id']
        )
        return {'detection': detection}
