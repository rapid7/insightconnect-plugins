import insightconnect_plugin_runtime
from .schema import StorePageContentInput, StorePageContentOutput

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
        return {"page": page}

    def test(self):
        """Test action"""
        return {
            "content": {
                "title": "HelloWorld",
                "space": "DEMO",
                "modifier": "TestUser",
                "created": "20161024T20:19:23Z",
                "content": "<p>hello</p>",
                "url": "https://komand.atlassian.net/wiki/display/DEMO/HelloWorld",
                "permissions": "0",
                "creator": "TestUser",
                "parentId": "0",
                "version": "1",
                "homePage": "false",
                "id": "19726355",
                "current": "true",
                "contentStatus": "current",
                "modified": "20161024T20:19:23Z",
            }
        }
