import insightconnect_plugin_runtime
from .schema import GetCompleteAlertByIdInput, GetCompleteAlertByIdOutput, Input, Output, Component
# Custom imports below


class GetCompleteAlertById(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_complete_alert_by_id',
                description=Component.DESCRIPTION,
                input=GetCompleteAlertByIdInput(),
                output=GetCompleteAlertByIdOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
