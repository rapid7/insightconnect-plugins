import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import ViewFileInput, ViewFileOutput, Input, Component, Output


class ViewFile(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="view_file",
            description=Component.DESCRIPTION,
            input=ViewFileInput(),
            output=ViewFileOutput(),
        )

    def run(self, params={}):
        md5 = params.get(Input.MD5, "")
        sha256 = params.get(Input.SHA256, "")
        task_id = params.get(Input.ID, "")
        if md5:
            endpoint = f"files/view/md5/{md5}"
        elif sha256:
            endpoint = f"files/view/sha256/{sha256}"
        elif id:
            endpoint = f"files/view/id/{task_id}"
        else:
            raise PluginException(
                cause="Invalid input provided.", assistance="Please provide one of ID, MD5, or SHA256"
            )
        response = self.connection.api.send(endpoint)
        return {Output.DATA: response.get("sample", {})}
