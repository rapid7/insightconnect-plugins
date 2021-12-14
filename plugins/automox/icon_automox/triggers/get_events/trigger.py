import insightconnect_plugin_runtime
import time
from .schema import GetEventsInput, GetEventsOutput, Input, Output, Component
# Custom imports below


class GetEvents(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_events',
                description=Component.DESCRIPTION,
                input=GetEventsInput(),
                output=GetEventsOutput())

    def run(self, params={}):
        """Run the trigger"""
        while True:
            # TODO: Implement trigger functionality
            self.send({})
            time.sleep(params.get("interval", 5))
