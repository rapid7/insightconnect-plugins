import insightconnect_plugin_runtime
from .schema import StorePageContentInput, StorePageContentOutput, Output

# Custom imports below
from insightconnect_plugin_runtime.helper import clean_dict
from ...util.util import extract_page_data


class StorePageContent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="store_page_content",
            description="Store Page Content",
            input=StorePageContentInput(),
            output=StorePageContentOutput(),
        )

    def run(self, params={}):
        """Store a page"""
        content = params.get("content")
        title = params.get("page")
        space = params.get("space")
        data = self.connection.client.store_page_content(title=title, space=space, content=content)
        page = extract_page_data(page=data)
        page = clean_dict(page)
        return {Output.PAGE: page}
