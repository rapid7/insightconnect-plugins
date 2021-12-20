import insightconnect_plugin_runtime
from .schema import CloseAlertInput, CloseAlertOutput, Input, Output, Component
# Custom imports below


class CloseAlert(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='close_alert',
                description=Component.DESCRIPTION,
                input=CloseAlertInput(),
                output=CloseAlertOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
