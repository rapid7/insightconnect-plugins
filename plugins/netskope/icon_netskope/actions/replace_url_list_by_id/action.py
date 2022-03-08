import insightconnect_plugin_runtime

from .schema import Component, Input, ReplaceUrlListByIdInput, ReplaceUrlListByIdOutput


class ReplaceUrlListById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="replace_url_list_by_id",
            description=Component.DESCRIPTION,
            input=ReplaceUrlListByIdInput(),
            output=ReplaceUrlListByIdOutput(),
        )

    def run(self, params={}):
        data = {
            Input.NAME: params.get(Input.NAME),
            "data": {Input.URLS: params.get(Input.URLS), Input.TYPE: params.get(Input.TYPE)},
        }
        return self.connection.client.replace_url_list_by_id(params.get(Input.ID), data)
