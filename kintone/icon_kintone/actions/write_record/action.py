import komand
from .schema import WriteRecordInput, WriteRecordOutput, Input, Output, Component
# Custom imports below
from icon_kintone.util.kintone import write_record


class WriteRecord(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='write_record',
                description=Component.DESCRIPTION,
                input=WriteRecordInput(),
                output=WriteRecordOutput())

    def run(self, params={}):
        app_id = params.get(Input.APP_ID)
        record_body = params.get(Input.RECORD_BODY)
        verify_ssl = self.connection.verify_ssl

        output = write_record(self.logger, self.connection.api_key, app_id, record_body, verify_ssl)

        return {Output.ADD_RECORD_RESPONSE: output}
