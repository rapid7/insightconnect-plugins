import komand
from .schema import UpdateRemediationStateInput, UpdateRemediationStateOutput
# Custom imports below


class UpdateRemediationState(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_remediation_state',
                description='Updates detection remediation state',
                input=UpdateRemediationStateInput(),
                output=UpdateRemediationStateOutput())

    def run(self, params={}):
        detection_id = params.get('detection_id')
        remediation_state = params.get('remediation_state', 'remediated')
        comment = params.get('comment')

        detection = self.connection.api.update_remediation_state(
            detection_id, remediation_state, comment
        )
        return {'detection': detection}
