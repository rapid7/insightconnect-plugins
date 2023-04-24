import insightconnect_plugin_runtime
from .schema import GetRemediationActionInput, GetRemediationActionOutput, Input, Output, Component
# Custom imports below


class GetRemediationAction(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_remediation_action',
                description=Component.DESCRIPTION,
                input=GetRemediationActionInput(),
                output=GetRemediationActionOutput())

    def run(self, params={}):
        remediation_details = self.connection.api.get_remediation_action(params.get(Input.INCIDENT_ID))
        return {Output.REMEDIATION_DETAILS: remediation_details}
        