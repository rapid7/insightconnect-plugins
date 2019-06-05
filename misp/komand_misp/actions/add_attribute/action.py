import komand
from .schema import AddAttributeInput, AddAttributeOutput
# Custom imports below


class AddAttribute(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_attribute',
                description='Add an attribute to an event',
                input=AddAttributeInput(),
                output=AddAttributeOutput())

    def run(self, params={}):
        event = params.get('event')
        type_value = params.get('type_value')
        category = params.get('category')
        value = params.get('value')
        comment = params.get('comment')

        client = self.connection.client
        in_event = client.get_event(event)
        item = client.add_named_attribute(in_event, type_value, value, category, comment=comment)
        try:
            attribute = item[0]
        except IndexError:
            self.logger.error('Add attribute return invalid, ' + item)
            raise
        try:
            attribute = attribute['Attribute']
        except KeyError:
            self.logger.error('Improperly formatted attribute, ' + attribute)
            raise
        return {'attribute': attribute}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        self.logger.info(output)
        return {"status": True}
