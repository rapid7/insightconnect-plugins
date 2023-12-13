import insightconnect_plugin_runtime
from .schema import GetPageInput, GetPageOutput, Output
from insightconnect_plugin_runtime import helper

# Custom imports below
from ...util.util import extract_page_data


class GetPage(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_page",
            description="Get Page",
            input=GetPageInput(),
            output=GetPageOutput(),
        )

    def run(self, params={}):
        """Return a page."""
        title = params.get("page")
        space = params.get("space")
        page_id = self.connection.client.get_page_id(title=title, space=space)
        if page_id:
            self.logger.info(f"Found page with ID: {page_id}")
            data = self.connection.client.get_page_by_id(page_id=page_id)
            if data:
                page = extract_page_data(page=data)
                page = helper.clean_dict(page)
                return {Output.PAGE: page, Output.FOUND: True}
        return {Output.PAGE: {}, Output.FOUND: False}
