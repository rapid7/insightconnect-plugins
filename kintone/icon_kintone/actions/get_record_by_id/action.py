import komand
from .schema import GetRecordByIdInput, GetRecordByIdOutput, Input, Output, Component
# Custom imports below
from icon_kintone.util.kintone import get_record


class GetRecordById(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_record_by_id',
                description=Component.DESCRIPTION,
                input=GetRecordByIdInput(),
                output=GetRecordByIdOutput())

    def run(self, params={}):
        app_id = params.get(Input.APP_ID)
        record_id = params.get(Input.RECORD_ID)
        verify_ssl = self.connection.verify_ssl

        output = get_record(self.logger, self.connection.api_key, app_id, record_id, verify_ssl)

        return {Output.RECORD: output}
