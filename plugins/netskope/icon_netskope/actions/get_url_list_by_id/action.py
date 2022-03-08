import insightconnect_plugin_runtime

from .schema import Component, GetUrlListByIdInput, GetUrlListByIdOutput, Input


class GetUrlListById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_url_list_by_id",
            description=Component.DESCRIPTION,
            input=GetUrlListByIdInput(),
            output=GetUrlListByIdOutput(),
        )

    def run(self, params={}):
        return self.connection.client.get_url_list_by_id(params.get(Input.ID))
