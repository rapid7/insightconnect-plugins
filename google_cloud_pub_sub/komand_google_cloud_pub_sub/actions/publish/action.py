import komand
from .schema import PublishInput, PublishOutput
# Custom imports below
import time
from google.cloud import pubsub


class Publish(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='publish',
                description='Publish',
                input=PublishInput(),
                output=PublishOutput())

    def run(self, params={}):
        topic = params.get('topic')
        message = params.get('message')

        project_id = self.connection.project
        if params.get('project_id'):
            project_id = params.get('project_id')

        message_bytes = str.encode(message)
        topic_name = 'projects/{project_id}/topics/{topic}'.format(project_id=project_id, topic=topic)

        publisher = pubsub.PublisherClient(credentials=self.connection.credentials)

        results = publisher.publish(topic_name, message_bytes)
        time.sleep(5)
        success = results.done()
        if not success:
            error = results.exception(timeout=5)
            self.logger.error('Error returned by google: ' + error)
            raise Exception('There was an error when trying to publish see log for more details')

        return {'success': success}

    def test(self):
        project_id = self.connection.project
        topics = []

        publisher = pubsub.PublisherClient(credentials=self.connection.credentials)
        project_path = publisher.project_path(project_id)

        for x in publisher.list_topics(project_path):
            topics.append(x.name)

        return {'topics': topics}
