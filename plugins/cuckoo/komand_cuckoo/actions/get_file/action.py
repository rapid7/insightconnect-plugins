import insightconnect_plugin_runtime
from .schema import GetFileInput, GetFileOutput, Input, Output, Component

# Custom imports below
from ...util.util import Util


class GetFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_file",
            description=Component.DESCRIPTION,
            input=GetFileInput(),
            output=GetFileOutput(),
        )

    def run(self, params={}):
        sha256 = params.get(Input.SHA256, "")
        endpoint = f"files/get/{sha256}"
        response = self.connection.api.send(endpoint, _json=False)
        content = response.content
        return {Output.CONTENTS: Util.prepare_decoded_value(content)}
