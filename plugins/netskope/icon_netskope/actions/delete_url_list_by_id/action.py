import insightconnect_plugin_runtime

from .schema import Component, DeleteUrlListByIdInput, DeleteUrlListByIdOutput, Input


class DeleteUrlListById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_url_list_by_id",
            description=Component.DESCRIPTION,
            input=DeleteUrlListByIdInput(),
            output=DeleteUrlListByIdOutput(),
        )

    def run(self, params={}):
        return self.connection.client.delete_url_list_by_id(params.get(Input.ID))
