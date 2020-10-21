import insightconnect_plugin_runtime
from .schema import SendAcknowledgeEventInput, SendAcknowledgeEventOutput, Input, Output, Component
# Custom imports below


class SendAcknowledgeEvent(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_acknowledge_event',
                description=Component.DESCRIPTION,
                input=SendAcknowledgeEventInput(),
                output=SendAcknowledgeEventOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
