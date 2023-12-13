import insightconnect_plugin_runtime
from .schema import GetPageByIdInput, GetPageByIdOutput, Output
from insightconnect_plugin_runtime import helper

# Custom imports below
from ...util.util import extract_page_data


class GetPageById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_page_by_id",
            description="Get Page By ID",
            input=GetPageByIdInput(),
            output=GetPageByIdOutput(),
        )

    def run(self, params={}):
        """Return a page."""
        page_id = params["page_id"]
        data = self.connection.client.get_page_by_id(page_id=page_id)
        if data:
            page = extract_page_data(page=data)
            page = helper.clean_dict(page)
            return {Output.PAGE: page, Output.FOUND: True}
        return {Output.PAGE: {}, Output.FOUND: False}
