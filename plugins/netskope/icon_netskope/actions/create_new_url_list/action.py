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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        name = params.get(Input.NAME)
        type_ = params.get(Input.TYPE)
        urls = params.get(Input.URLS, [])
        # END INPUT BINDING - DO NOT REMOVE

        response = self.connection.client.create_a_new_url_list(
            {
                "name": name,
                "data": {"urls": urls, "type": type_},
            }
        )
        return {
            Output.ID: response.get("id", 0),
            Output.NAME: response.get("name", ""),
            Output.DATA: response.get("data", {"urls": [], "type": ""}),
            Output.PENDING: response.get("pending", 0),
            Output.MODIFY_BY: response.get("modify_by", ""),
            Output.MODIFY_TIME: response.get("modify_time", ""),
            Output.MODIFY_TYPE: response.get("modify_type", ""),
        }
