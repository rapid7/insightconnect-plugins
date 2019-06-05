import komand
from .schema import AddTagInput, AddTagOutput
# Custom imports below


class AddTag(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_tag',
                description='Add tag',
                input=AddTagInput(),
                output=AddTagOutput())

    def run(self, params={}):
        client = self.connection.client
        in_event = client.get_event(params.get('event'))
        try:
            item = client.tag(in_event['Event']['uuid'], tag=params.get('tag'))
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
