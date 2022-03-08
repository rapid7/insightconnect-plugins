import insightconnect_plugin_runtime

from .schema import Component, Input, Output, UploadJsonConfigInput, UploadJsonConfigOutput


class UploadJsonConfig(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="upload_json_config",
            description=Component.DESCRIPTION,
            input=UploadJsonConfigInput(),
            output=UploadJsonConfigOutput(),
        )

    def run(self, params={}):
        response = self.connection.client.upload_json_config(**params.get(Input.URLLIST))
        return {Output.UPLOADED_URLLIST: response}
