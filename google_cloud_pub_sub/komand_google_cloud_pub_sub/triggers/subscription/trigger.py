import komand
from .schema import SubscriptionInput, SubscriptionOutput
# Custom imports below
from google.cloud import pubsub


class Subscription(komand.Trigger):

    message_list = []

    def __init__(self):
        super(self.__class__, self).__init__(
                name='subscription',
                description='Subscription',
                input=SubscriptionInput(),
                output=SubscriptionOutput())

    def run(self, params={}):
        number_of_messages = params.get('number_of_messages')
        if number_of_messages < 1:
            raise Exception('Number of messages must be 1 or more')

        def _callback(message):
            message_string = bytes.decode(message.data)
            _send(message_string)
            message.ack()

        def _send(message_string):
            try:
                self.message_list.append(message_string)
                if len(self.message_list) >= number_of_messages:
                    self.send({'messages': self.message_list})
                    self.message_list = []
            except Exception as e:
                self.logger.error('Message string: {}'.format(message_string))
                self.logger.error('Message list: {}'.format(self.message_list))
                raise Exception('An unknown error occurred. Dumping buffer to log. Error: {}'.format(e))

        subscription = params.get('subscription')
        project_id = self.connection.project
        if params.get('project_id'):
            project_id = params.get('project_id')

        sub_name = 'projects/{project}/subscriptions/{subscription}'.format(project=project_id,
                                                                            subscription=subscription)

        subscriber = pubsub.SubscriberClient(credentials=self.connection.credentials)
        future = subscriber.subscribe(sub_name, _callback)
        try:
            future.result()
        except Exception as ex:
            self.logger.error('An error occurred, {}'.format(ex))
            subscription.close()
            raise

    def test(self):
        project_id = self.connection.project

        subscriptions = []
        subscriber = pubsub.SubscriberClient(credentials=self.connection.credentials)
        project_path = subscriber.project_path(project_id)

        for x in subscriber.list_subscriptions(project_path):
            subscriptions.append(x.name)
        return {'project_path': project_path}
