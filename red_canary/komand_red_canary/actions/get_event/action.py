import komand
from .schema import GetEventInput, GetEventOutput
# Custom imports below


class GetEvent(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_event',
                description='Retrieves an event by unique identifier',
                input=GetEventInput(),
                output=GetEventOutput())

    def run(self, params={}):
        event_id = params.get('event_id')
        event = self.connection.api.get_event(event_id)
        return {'event': event}
