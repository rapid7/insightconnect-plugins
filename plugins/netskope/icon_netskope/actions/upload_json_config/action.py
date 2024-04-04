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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        url_list = params.get(Input.URLLIST, [])
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.UPLOADED_URLLIST: self.connection.client.upload_json_config(**url_list)}
