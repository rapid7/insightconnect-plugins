import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import SubmitFilesInput, SubmitFilesOutput, Input, Component
# Custom imports below
import base64


class SubmitFiles(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="submit_files",
            description=Component.DESCRIPTION,
            input=SubmitFilesInput(),
            output=SubmitFilesOutput(),
        )

    def run(self, params={}):
        files = params.get(Input.FILES)
        endpoint = "tasks/create/file"
        file_list = []
        try:
            for file in files:
                file_list.append(("file", (file.get("filename", ""), base64.b64decode(file.get("contents")))))
        except (TypeError, ValueError, UnicodeDecodeError) as exception:
            raise PluginException(preset=PluginException.Preset.BASE64_DECODE, data=exception)
        response = self.connection.api.send(endpoint, method="POST", files=file_list)
        return response
