import insightconnect_plugin_runtime
from .schema import GetPageContentInput, GetPageContentOutput, Output, Input

# Custom imports below


class GetPageContent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_page_content",
            description="Get Page Content",
            input=GetPageContentInput(),
            output=GetPageContentOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        page_name = params.get(Input.PAGE, "")
        space = params.get(Input.SPACE, "")
        # END INPUT BINDING - DO NOT REMOVE

        page_id = self.connection.client.get_page_id(title=page_name, space=space)
        if page_id:
            data = self.connection.client.get_page_content(page_id=page_id)
            if data:
                return {Output.CONTENT: data, Output.FOUND: True}
        return {Output.FOUND: False, Output.CONTENT: ""}
