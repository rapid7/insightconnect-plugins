import insightconnect_plugin_runtime
from .schema import GetPageContentInput, GetPageContentOutput

# Custom imports below
from ...util import util


class GetPageContent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_page_content",
            description="Get Page Content",
            input=GetPageContentInput(),
            output=GetPageContentOutput(),
        )

    def run(self, params={}):
        title = params["page"]
        space = params["space"]
        page_id = self.connection.client.get_page_id(title=title, space=space)
        if page_id:
            data = self.connection.client.get_page_content(page_id=page_id)
            if data:
                return {"content": data, "found": True}
        return {"found": False, "content": ""}

    def test(self):
        """Return content"""
        return {"found": True, "content": ""}
