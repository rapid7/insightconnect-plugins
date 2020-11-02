import insightconnect_plugin_runtime
from .schema import SendResolveEventInput, SendResolveEventOutput
# Custom imports below
import pypd


class SendResolveEvent(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_resolve_event',
                description='Resolve an incident',
                input=SendResolveEventInput(),
                output=SendResolveEventOutput())

    def run(self, params={}):
        """Resolve event"""
        
        ev = pypd.Event.create(data={
            'service_key': params['service_key'],
            'event_type': 'resolve',
            'incident_key': params['incident_key'],
            'description': params.get('description'),
            'details': params.get('details'),
        })

        return ev

    def test(self):
        """Test action"""
        return {}
