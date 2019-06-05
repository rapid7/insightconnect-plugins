import komand
from .schema import GetBlobDataInput, GetBlobDataOutput
# Custom imports below
from base64 import b64encode
from binascii import Error as B64EncodingError
from komand.exceptions import ConnectionTestException


class GetBlobData(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_blob_data',
                description='Retrieve blob data for a given record',
                input=GetBlobDataInput(),
                output=GetBlobDataOutput())

    def run(self, params={}):
        record_id = params.get('record_id')
        object_name = params.get('object_name', 'Attachment')
        field_name = params.get('field_name', 'body')

        api_data = self.connection.api.get_blob_data(
            record_id, object_name, field_name
        )

        try:
            data = b64encode(api_data).decode()
        except (B64EncodingError, UnicodeDecodeError):
            message = 'Incorrect data format received from API: {}'.format(
                api_data
            )
            self.logger.error('Get Blob Data: ' + message)
            raise ConnectionTestException(
                cause=message,
                assistance='Please make sure that you are using a correct ' +
                'object type (not all of them allow for binary data). Also, ' +
                'check if the binary data has been set for a given record'
            )

        return {'data': data}
