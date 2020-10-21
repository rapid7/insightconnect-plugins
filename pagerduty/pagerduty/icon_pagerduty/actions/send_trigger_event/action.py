import insightconnect_plugin_runtime
from .schema import SendTriggerEventInput, SendTriggerEventOutput, Input, Output, Component
# Custom imports below


class SendTriggerEvent(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_trigger_event',
                description=Component.DESCRIPTION,
                input=SendTriggerEventInput(),
                output=SendTriggerEventOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
