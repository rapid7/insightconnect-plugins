import komand
from .schema import FindEventInput, FindEventOutput
# Custom imports below


class FindEvent(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='find_event',
                description='Receive events based on criteria',
                input=FindEventInput(),
                output=FindEventOutput())

    def run(self, params={}):
        client = self.connection.client
        try:
            event = client.get_event(params.get('event_id'))

            if isinstance(event, dict):
                # Example of when event is not found
                # {
                #    "message": "Invalid event.",
                #    "url": "/events/23423432",
                #    "errors": [ "Invalid event." ],
                #    "name": "Invalid event."
                # }
                if 'Event' not in event:
                    if 'message' in event:
                        message = event.pop('message')
                        errors = event.pop('errors')
                else:
                    message = 'Event found.'
                    errors = ['No errors.']
            else:
                Exception('Something went wrong with the request')
        except:
            self.logger.error('Event %s not found or failure occurred', params.get('event_id'))
            raise

        return {'event': event['Event'], 'message': message, 'errors': errors}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        return {'event': {}, 'message': '', 'errors': ['']}
