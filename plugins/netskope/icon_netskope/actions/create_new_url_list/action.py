import insightconnect_plugin_runtime

from .schema import Component, CreateNewUrlListInput, CreateNewUrlListOutput, Input, Output


class CreateNewUrlList(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_new_url_list",
            description=Component.DESCRIPTION,
            input=CreateNewUrlListInput(),
            output=CreateNewUrlListOutput(),
        )

    def run(self, params={}):
        data = {
            Input.NAME: params.get(Input.NAME),
            "data": {Input.URLS: params.get(Input.URLS), Input.TYPE: params.get(Input.TYPE)},
        }
        return self.connection.client.create_a_new_url_list(data)
