import komand
from .schema import DeleteRecordInput, DeleteRecordOutput
# Custom imports below
from komand.exceptions import ConnectionTestException


class DeleteRecord(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_record',
                description='Delete a record',
                input=DeleteRecordInput(),
                output=DeleteRecordOutput())

    def run(self, params={}):
        record_id = params.get('record_id')
        object_name = params.get('object_name', 'Account')

        try:
            self.connection.api.delete_record(record_id, object_name)
        except ConnectionTestException:
            return {'success': False}
        else:
            return {'success': True}
