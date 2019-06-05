import komand
from .schema import UpdateRecordInput, UpdateRecordOutput
# Custom imports below
from komand.exceptions import ConnectionTestException


class UpdateRecord(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_record',
                description='Update a record',
                input=UpdateRecordInput(),
                output=UpdateRecordOutput())

    def run(self, params={}):
        record_id = params.get('record_id')
        object_name = params.get('object_name', 'Account')
        object_data = params.get('object_data')

        try:
            self.connection.api.update_record(
                record_id, object_name, object_data
            )
        except ConnectionTestException:
            return {'success': False}
        else:
            return {'success': True}
