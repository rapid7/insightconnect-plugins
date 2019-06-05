import komand
from .schema import MitigateThreatInput, MitigateThreatOutput, Input, Output
# Custom imports below


class MitigateThreat(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='mitigate_threat',
                description='Apply a mitigation action to a threat',
                input=MitigateThreatInput(),
                output=MitigateThreatOutput())

    def run(self, params={}):
        threat_id = params.get(Input.THREAT_ID)
        action = params.get(Input.ACTION)

        affected = self.connection.mitigate_threat(threat_id, action)
        return {Output.AFFECTED: affected}
