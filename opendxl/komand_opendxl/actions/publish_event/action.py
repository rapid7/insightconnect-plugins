import komand
from .schema import PublishEventInput, PublishEventOutput
# Custom imports below
from dxlclient.message import Event
from dxlclient.client import DxlClient


class PublishEvent(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='publish_event',
                description='Publish a new event to a specified topic',
                input=PublishEventInput(),
                output=PublishEventOutput())

    def run(self, params={}):
        topic = params.get('topic')
        event_message = params.get('event_message')

        event = Event(topic)
        event.payload = event_message.encode()

        with DxlClient(self.connection.config) as dxl_client:
            # Connect to the fabric
            dxl_client.connect()
            dxl_client.send_event(event)
        return {'success': True}

    def test(self):
        t = self.connection.test()
        if t:
            return {'success': True}
