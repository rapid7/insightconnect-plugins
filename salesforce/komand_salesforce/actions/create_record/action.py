import komand
from .schema import CreateRecordInput, CreateRecordOutput
# Custom imports below


class CreateRecord(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_record',
                description='Create a new SObject record',
                input=CreateRecordInput(),
                output=CreateRecordOutput())

    def run(self, params={}):
        object_name = params.get('object_name', 'Account')
        object_data = params.get('object_data')

        record = self.connection.api.create_record(object_name, object_data)

        try:
            id_ = record['id']
        except KeyError:
            self.logger.error('Error: id key is missing from record.')
            id_ = 'Not available'

        if record.get('success'):
            return {'id': id_}
        else:
            return {}
