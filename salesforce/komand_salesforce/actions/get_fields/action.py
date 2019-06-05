import komand
from .schema import GetFieldsInput, GetFieldsOutput
# Custom imports below


class GetFields(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_fields',
                description='Retrieve field values from a record',
                input=GetFieldsInput(),
                output=GetFieldsOutput())

    def run(self, params={}):
        record_id = params.get('record_id')
        object_name = params.get('object_name', 'Account')
        fields = params.get('fields', [])

        fields = self.connection.api.get_fields(record_id, object_name, fields)

        try:
            del fields['attributes']
        except KeyError:
            self.logger.error('Error: attributes key does not exist in fields object')

        return {'fields': fields}
