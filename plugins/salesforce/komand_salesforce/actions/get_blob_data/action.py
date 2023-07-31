import insightconnect_plugin_runtime
from .schema import GetBlobDataInput, GetBlobDataOutput, Input, Output, Component

# Custom imports below
from base64 import b64encode
from binascii import Error as B64EncodingError
from insightconnect_plugin_runtime.exceptions import PluginException


class GetBlobData(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_blob_data",
            description=Component.DESCRIPTION,
            input=GetBlobDataInput(),
            output=GetBlobDataOutput(),
        )

    def run(self, params={}):
        api_data = self.connection.api.get_blob_data(
            params.get(Input.RECORDID), params.get(Input.OBJECTNAME), params.get(Input.FIELDNAME)
        )
        try:
            data = b64encode(api_data).decode()
        except (B64EncodingError, UnicodeDecodeError):
            message = f"Incorrect data format received from API: {api_data}"
            self.logger.error(f"Get Blob Data: {message}")
            raise PluginException(
                cause=message,
                assistance="Please make sure that you are using a correct object type (not all of them allow for binary"
                " data). Also, check if the binary data has been set for a given record",
            )

        return {Output.DATA: data}
