import insightconnect_plugin_runtime
from .schema import GetPageByIdInput, GetPageByIdOutput, Output, Input
from insightconnect_plugin_runtime.helper import clean_dict

# Custom imports below
from komand_confluence.util.util import extract_page_data


class GetPageById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_page_by_id",
            description="Get Page By ID",
            input=GetPageByIdInput(),
            output=GetPageByIdOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        page_id = params.get(Input.PAGE_ID, "")
        # END INPUT BINDING - DO NOT REMOVE

        data = self.connection.client.get_page_by_id(page_id=page_id)
        if data:
            return {Output.PAGE: clean_dict(extract_page_data(page=data)), Output.FOUND: True}
        return {Output.PAGE: {}, Output.FOUND: False}
