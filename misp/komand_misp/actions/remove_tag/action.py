import komand
from .schema import RemoveTagInput, RemoveTagOutput
# Custom imports below


class RemoveTag(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_tag',
                description='Remove tag',
                input=RemoveTagInput(),
                output=RemoveTagOutput())

    def run(self, params={}):
        client = self.connection.client
        in_event = client.get_event(params.get('event'))
        try:
            item = client.untag(in_event['Event']['uuid'], tag=params.get('tag'))
            if "successfully" in item['name']:
                return {'status': True}
            else:
                self.logger.info(item)
                return {'status': False}
        except:
            self.logger.error(item)
            raise

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        self.logger.info(output)
        return {"status": True}
