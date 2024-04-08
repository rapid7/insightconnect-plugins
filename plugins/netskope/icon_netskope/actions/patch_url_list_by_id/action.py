import insightconnect_plugin_runtime

from .schema import Component, Input, PatchUrlListByIdInput, PatchUrlListByIdOutput, Output


class PatchUrlListById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="patch_url_list_by_id",
            description=Component.DESCRIPTION,
            input=PatchUrlListByIdInput(),
            output=PatchUrlListByIdOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        identifier = params.get(Input.ID)
        name = params.get(Input.NAME)
        type_ = params.get(Input.TYPE)
        urls = params.get(Input.URLS)
        action = params.get(Input.ACTION)
        # END INPUT BINDING - DO NOT REMOVE

        data = {"name": name} if name else {}
        if all((urls, type_)):
            data["data"] = {"urls": urls, "type": type_}
        response = self.connection.client.patch_url_list_by_id(identifier, action, data)
        return {
            Output.ID: response.get("id", 0),
            Output.NAME: response.get("name", ""),
            Output.DATA: response.get("data", {"urls": [], "type": ""}),
            Output.PENDING: response.get("pending", 0),
            Output.MODIFY_BY: response.get("modify_by", ""),
            Output.MODIFY_TIME: response.get("modify_time", ""),
            Output.MODIFY_TYPE: response.get("modify_type", ""),
        }
