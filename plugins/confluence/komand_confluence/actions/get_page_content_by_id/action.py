import insightconnect_plugin_runtime
from .schema import GetPageContentByIdInput, GetPageContentByIdOutput, Output, Input


class GetPageContentById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_page_content_by_id",
            description="Get Page Content by Page ID",
            input=GetPageContentByIdInput(),
            output=GetPageContentByIdOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        page_id = params.get(Input.PAGE_ID, "")
        # END INPUT BINDING - DO NOT REMOVE

        data = self.connection.client.get_page_content(page_id=page_id)
        if data:
            return {Output.CONTENT: data, Output.FOUND: True}
        return {Output.FOUND: False, Output.CONTENT: ""}
