import insightconnect_plugin_runtime
from .schema import GetPageInput, GetPageOutput
from insightconnect_plugin_runtime import helper
# Custom imports below
from ...util.util import extract_page_data


class GetPage(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_page", description="Get Page", input=GetPageInput(), output=GetPageOutput()
        )

    def run(self, params={}):
        """Return a page."""
        page = params["page"]
        space = params["space"]
        id = self.connection.client.get_page_id(title=page, space=space)
        data = self.connection.client.get_page_by_id(page_id=id)
        if data:
            page = extract_page_data(page=data)
            page = helper.clean_dict(page)
            return {"page": page, "found": True}

        return {"page": {}, "found": False}

    def test(self):
        """Test action"""
        return {
            "found": True,
            "page": {
                "title": "HelloWorld",
                "space": "DEMO",
                "modifier": "TestUser",
                "created": "20161024T20:19:23Z",
                "content": "<p>hello</p>",
                "url": "https://komand.atlassian.net/wiki/display/DEMO/HelloWorld", # base and webui
                "permissions": "0", #
                "creator": "TestUser",
                "parentId": "0", #
                "version": "1",
                "homePage": "false", #
                "id": "19726355",
                "current": "true", #
                "contentStatus": "current", #
                "modified": "20161024T20:19:23Z", #
            },
        }
