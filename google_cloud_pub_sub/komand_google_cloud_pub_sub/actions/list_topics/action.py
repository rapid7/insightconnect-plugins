import komand
from .schema import ListTopicsInput, ListTopicsOutput
# Custom imports below
from google.cloud import pubsub


class ListTopics(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_topics',
                description='List all topics within a project',
                input=ListTopicsInput(),
                output=ListTopicsOutput())

    def run(self, params={}):
        project_id = self.connection.project
        if params.get('project_id'):
            project_id = params.get('project_id')
        topics = []

        publisher = pubsub.PublisherClient(credentials=self.connection.credentials)
        project_path = publisher.project_path(project_id)

        for x in publisher.list_topics(project_path):
            topics.append(x.name)

        return {'topics': topics}

    def test(self):
        project_id = self.connection.project
        topics = []

        publisher = pubsub.PublisherClient(credentials=self.connection.credentials)
        project_path = publisher.project_path(project_id)

        for x in publisher.list_topics(project_path):
            topics.append(x.name)

        return {'topics': topics}
