import komand
from .schema import SendTriggerEventInput, SendTriggerEventOutput
# Custom import below
import pypd


class SendTriggerEvent(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_trigger_event',
                description='Trigger an incident',
                input=SendTriggerEventInput(),
                output=SendTriggerEventOutput())

    def run(self, params={}):
        """Trigger event"""
        ev = pypd.Event.create(data={
            'service_key': params['service_key'],
            'event_type': 'trigger',
            'description': params['description'],
            'contexts': params.get('contexts'),
            'details': params.get('details'),
            'client': params.get('client'),
            'client_url': params.get('client_url'),
        })

        return ev

    def test(self):
        """Test event"""
        return {
            'incident_key': 'aebdf1be9793454e86c0f0079820f32f',
            'status': 'success',
            'message': 'Event processed'
        }
