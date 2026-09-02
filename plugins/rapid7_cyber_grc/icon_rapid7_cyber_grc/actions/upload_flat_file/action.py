import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import UploadFlatFileInput, UploadFlatFileOutput, Input, Output, Component

# Custom imports below


class UploadFlatFile(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="upload_flat_file",
            description=Component.DESCRIPTION,
            input=UploadFlatFileInput(),
            output=UploadFlatFileOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        description = params.get(Input.DESCRIPTION)
        file = params.get(Input.FILE)
        file_name = params.get(Input.FILE_NAME)
        id = params.get(Input.ID)
        operation_type = params.get(Input.OPERATION_TYPE)
        # END INPUT BINDING - DO NOT REMOVE
        return {
            Output.RESULT: self.connection.client.upload_flat_file(
                file_name=file_name,
                contents=file,
                operation_type=operation_type,
                description=description,
                record_id=id,
            )
        }
