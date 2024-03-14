import insightconnect_plugin_runtime
from .schema import ViewFileInput, ViewFileOutput, Input, Component


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
        endpoint = f"files/view/md5/{md5}"
        if sha256:
            endpoint = f"files/view/sha256/{sha256}"
        elif id:
            endpoint = f"files/view/id/{task_id}"
        response = self.connection.api.send(endpoint)
        return response
