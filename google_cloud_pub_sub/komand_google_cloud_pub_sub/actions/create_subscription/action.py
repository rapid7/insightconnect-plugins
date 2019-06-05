import komand
from .schema import CreateSubscriptionInput, CreateSubscriptionOutput
# Custom imports below
from google.cloud import pubsub


class CreateSubscription(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_subscription',
                description='Create a new subscription to a topic',
                input=CreateSubscriptionInput(),
                output=CreateSubscriptionOutput())

    def run(self, params={}):
        topic = params.get('topic')
        subscription_name = params.get('subscription_name')

        project_id = self.connection.project
        if params.get('project_id'):
            project_id = params.get('project_id')

        topic_name = 'projects/{project_id}/topics/{topic}'.format(project_id=project_id, topic=topic)
        sub_name = 'projects/{project}/subscriptions/{subscription}'.format(project=project_id,
                                                                            subscription=subscription_name)

        subscriber = pubsub.SubscriberClient(credentials=self.connection.credentials)
        result = subscriber.create_subscription(sub_name, topic_name)
        return {'subscription': result.name}

    def test(self):
        project_id = self.connection.project

        subscriptions = []
        subscriber = pubsub.SubscriberClient(credentials=self.connection.credentials)
        project_path = subscriber.project_path(project_id)

        for x in subscriber.list_subscriptions(project_path):
            subscriptions.append(x.name)
        return {'project_path': project_path}
