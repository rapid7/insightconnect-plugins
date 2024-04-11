import insightconnect_plugin_runtime
from .schema import StorePageContentInput, StorePageContentOutput, Output, Input

# Custom imports below
from insightconnect_plugin_runtime.helper import clean_dict
from komand_confluence.util.util import extract_page_data


class StorePageContent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="store_page_content",
            description="Store Page Content",
            input=StorePageContentInput(),
            output=StorePageContentOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        content = params.get(Input.CONTENT, "")
        page_name = params.get(Input.PAGE, "")
        space = params.get(Input.SPACE, "")
        # END INPUT BINDING - DO NOT REMOVE

        data = self.connection.client.store_page_content(title=page_name, space=space, content=content)
        return {Output.PAGE: clean_dict(extract_page_data(page=data))}
