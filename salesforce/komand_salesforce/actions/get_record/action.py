import komand
from .schema import GetRecordInput, GetRecordOutput
# Custom imports below


class GetRecord(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_record',
                description='Retrieve a record',
                input=GetRecordInput(),
                output=GetRecordOutput())

    def run(self, params={}):
        record_id = params.get('record_id')
        external_id_field_name = params.get('external_id_field_name')
        object_name = params.get('object_name', 'Account')

        record = self.connection.api.get_record(
            record_id, external_id_field_name, object_name
        )

        return {'record': record}
