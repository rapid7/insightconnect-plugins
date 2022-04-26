import insightconnect_plugin_runtime

from .schema import Component, Input, PatchUrlListByIdInput, PatchUrlListByIdOutput


class PatchUrlListById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="patch_url_list_by_id",
            description=Component.DESCRIPTION,
            input=PatchUrlListByIdInput(),
            output=PatchUrlListByIdOutput(),
        )

    def run(self, params={}):
        data = {}
        if params.get(Input.NAME):
            data[Input.NAME] = params.get(Input.NAME)
        if all((params.get(Input.URLS), params.get(Input.TYPE))):
            data["data"] = {Input.URLS: params.get(Input.URLS), Input.TYPE: params.get(Input.TYPE)}
        return self.connection.client.patch_url_list_by_id(params.get(Input.ID), params.get(Input.ACTION), data)
