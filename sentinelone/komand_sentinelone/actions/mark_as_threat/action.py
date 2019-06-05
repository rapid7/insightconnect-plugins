import komand
from .schema import MarkAsThreatInput, MarkAsThreatOutput, Input, Output
# Custom imports below


class MarkAsThreat(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='mark_as_threat',
                description='Mark suspicious threat as threat',
                input=MarkAsThreatInput(),
                output=MarkAsThreatOutput())

    def run(self, params={}):
        threat_id = params.get(Input.THREAT_ID)
        whitening_option = params.get(Input.WHITENING_OPTION)
        target_scope = params.get(Input.TARGET_SCOPE)

        whitening_option = whitening_option or None

        affected = self.connection.mark_as_threat(
            threat_id, whitening_option, target_scope
        )
        return {Output.AFFECTED: affected}
