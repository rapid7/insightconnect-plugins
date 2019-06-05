import komand
from .schema import CreateTopicInput, CreateTopicOutput
# Custom imports below
from google.cloud import pubsub


class CreateTopic(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_topic',
                description='Create a new topic',
                input=CreateTopicInput(),
                output=CreateTopicOutput())

    def run(self, params={}):
        topic = params.get('topic')
        project_id = self.connection.project

        if params.get('project_id'):
            project_id = params.get('project_id')

        topic_name = 'projects/{project_id}/topics/{topic}'.format(project_id=project_id, topic=topic)

        publisher = pubsub.PublisherClient(credentials=self.connection.credentials)
        new_topic = publisher.create_topic(topic_name)

        return {'topic': new_topic.name}

    def test(self):
        project_id = self.connection.project
        topics = []

        publisher = pubsub.PublisherClient(credentials=self.connection.credentials)
        project_path = publisher.project_path(project_id)

        for x in publisher.list_topics(project_path):
            topics.append(x.name)

        return {'topics': topics}
