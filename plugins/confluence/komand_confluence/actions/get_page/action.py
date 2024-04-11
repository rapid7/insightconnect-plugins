import insightconnect_plugin_runtime
from .schema import GetPageInput, GetPageOutput, Output, Input
from insightconnect_plugin_runtime.helper import clean_dict

# Custom imports below
from komand_confluence.util.util import extract_page_data


class GetPage(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_page",
            description="Get Page",
            input=GetPageInput(),
            output=GetPageOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        page_name = params.get(Input.PAGE, "")
        space = params.get(Input.SPACE, "")
        # END INPUT BINDING - DO NOT REMOVE

        page_id = self.connection.client.get_page_id(title=page_name, space=space)
        if page_id:
            self.logger.info(f"Found page with ID: {page_id}")
            data = self.connection.client.get_page_by_id(page_id=page_id)
            if data:
                return {Output.PAGE: clean_dict(extract_page_data(page=data)), Output.FOUND: True}
        return {Output.PAGE: {}, Output.FOUND: False}
