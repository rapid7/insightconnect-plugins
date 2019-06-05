import komand
from .schema import ReceiveEventInput, ReceiveEventOutput
# Custom imports below
from dxlclient.callbacks import EventCallback
from dxlclient.client import DxlClient
from threading import Condition


class ReceiveEvent(komand.Trigger):

    message_list = []

    def __init__(self):
        super(self.__class__, self).__init__(
                name='receive_event',
                description='Trigger on receiving a new event from a specified topic',
                input=ReceiveEventInput(),
                output=ReceiveEventOutput())

    def run(self, params={}):
        topic = params.get('topic')
        number_of_messages = params.get('number_of_messages')
        if number_of_messages < 1:
            raise Exception('Number of messages must be 1 or more')

        def _send(message_string):
            try:
                self.message_list.append(message_string)
                if len(self.message_list) >= number_of_messages:
                    self.send({'messages': self.message_list})
                    self.message_list = []
            except Exception as e:
                self.logger.error('Message string: {}'.format(message_string))
                self.logger.error('Message list: {}'.format(self.message_list))
                raise Exception(
                    'An unknown error occurred. Dumping buffer to log. Error: {}'.format(e))

        event_count_condition = Condition()
        # Create the DXL client
        with DxlClient(self.connection.config) as dxl_client:
            # Connect to the fabric
            dxl_client.connect()

            class _TriggerEventCallback(EventCallback):

                def on_event(self, event):
                    with event_count_condition:
                        _send(event.payload.decode())
                        event_count_condition.notify_all()

            dxl_client.add_event_callback(topic, _TriggerEventCallback())
            with event_count_condition:
                while True:
                    event_count_condition.wait()

    def test(self):
        t = self.connection.test()
        if t:
            return {'success': True}
