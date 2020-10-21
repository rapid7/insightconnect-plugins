import insightconnect_plugin_runtime
from .schema import SendResolveEventInput, SendResolveEventOutput, Input, Output, Component
# Custom imports below


class SendResolveEvent(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_resolve_event',
                description=Component.DESCRIPTION,
                input=SendResolveEventInput(),
                output=SendResolveEventOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
