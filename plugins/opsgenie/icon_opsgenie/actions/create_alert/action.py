import insightconnect_plugin_runtime
from .schema import CreateAlertInput, CreateAlertOutput, Input, Output, Component
# Custom imports below


class CreateAlert(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_alert',
                description=Component.DESCRIPTION,
                input=CreateAlertInput(),
                output=CreateAlertOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
