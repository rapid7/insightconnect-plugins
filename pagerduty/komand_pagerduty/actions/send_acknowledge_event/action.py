import komand
from .schema import SendAcknowledgeEventInput, SendAcknowledgeEventOutput
# Custom imports below
import pypd


class SendAcknowledgeEvent(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='send_acknowledge_event',
                description='Acknowledge an incident',
                input=SendAcknowledgeEventInput(),
                output=SendAcknowledgeEventOutput())

    def run(self, params={}):
        """Send acknowledge"""

        self.logger.info('Acknowledging: %s', params)
        ev = pypd.Event.create(data={
            'event_type': 'acknowledge',
            'service_key': params['service_key'],
            'incident_key': params['incident_key'],
            'description': params.get('description') or '',
            'details': params.get('details') or {},
        })

        return ev

    def test(self):
        """Test action"""
        return {
            'incident_key': 'aebdf1be9793454e86c0f0079820f32f',
            'status': 'success',
            'message': 'Event processed'
        }
