import komand
from .schema import GetThreatSummaryInput, GetThreatSummaryOutput
# Custom imports below


class GetThreatSummary(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_threat_summary',
            description='Gets summary of all threats',
            input=GetThreatSummaryInput(),
            output=GetThreatSummaryOutput())

    def run(self, params={}):
        self.logger.info("Starting step")
        threats = self.connection.get_threat_summary()
        return komand.helper.clean(threats)
