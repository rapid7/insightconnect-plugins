import komand
from .schema import PublishInput, PublishOutput
# Custom imports below


class Publish(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='publish',
                description='Publish an event',
                input=PublishInput(),
                output=PublishOutput())

    def run(self, params={}):
        event = params.get('event')

        client = self.connection.client
        in_event = client.get_event(event)
        published = client.publish(in_event, True)
        try:
            test = published['id']
        except KeyError:
            self.logger.error('Something went wrong see returned request, ' + published)
            raise
        return {'published': published}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        self.logger.info(output)
        return {"status": True}
