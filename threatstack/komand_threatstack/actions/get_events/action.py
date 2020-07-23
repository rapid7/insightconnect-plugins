import komand
from .schema import GetEventsInput, GetEventsOutput, Input, Output, Component
# Custom imports below


class GetEvents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_events',
                description=Component.DESCRIPTION,
                input=GetEventsInput(),
                output=GetEventsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
