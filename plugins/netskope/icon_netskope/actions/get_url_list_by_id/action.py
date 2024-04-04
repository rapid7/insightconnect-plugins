import insightconnect_plugin_runtime

from .schema import Component, GetUrlListByIdInput, GetUrlListByIdOutput, Input, Output


class GetUrlListById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_url_list_by_id",
            description=Component.DESCRIPTION,
            input=GetUrlListByIdInput(),
            output=GetUrlListByIdOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        identifier = params.get(Input.ID)
        # END INPUT BINDING - DO NOT REMOVE

        response = self.connection.client.get_url_list_by_id(identifier)
        return {
            Output.ID: response.get("id", 0),
            Output.NAME: response.get("name", ""),
            Output.DATA: response.get("data", {"urls": [], "type": ""}),
            Output.PENDING: response.get("pending", 0),
            Output.MODIFY_BY: response.get("modify_by", ""),
            Output.MODIFY_TIME: response.get("modify_time", ""),
            Output.MODIFY_TYPE: response.get("modify_type", ""),
        }
