import komand
from .schema import StorePageContentInput, StorePageContentOutput
# Custom imports below
from ...util import util


class StorePageContent(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='store_page_content',
                description='Store Page Content',
                input=StorePageContentInput(),
                output=StorePageContentOutput())

    def run(self, params={}):
        """Store a page"""
        content = params['content']
        page = params['page']
        space = params['space']
        p = self.connection.client.storePageContent(page, space, content)
        p = util.normalize_page(p)
        return { 'page': p }

    def test(self):
        """Test action"""
        return {'content': {'title': 'HelloWorld', 'space': 'DEMO', 'modifier': 'TestUser', 'created': '20161024T20:19:23Z', 'content': '<p>hello</p>', 'url': 'https://komand.atlassian.net/wiki/display/DEMO/HelloWorld', 'permissions': '0', 'creator': 'TestUser', 'parentId': '0', 'version': '1', 'homePage': 'false', 'id': '19726355', 'current': 'true', 'contentStatus': 'current', 'modified': '20161024T20:19:23Z'}}
