import komand
from .schema import GetPageInput, GetPageOutput
# Custom imports below
from ...util import util


class GetPage(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_page',
                description='Get Page',
                input=GetPageInput(),
                output=GetPageOutput())

    def run(self, params={}):
        """Return a page."""
        page = params['page']
        space = params['space']
        p = self.connection.client.getPage(page, space)
        if p: 
            p = util.normalize_page(p)
            return { 'page': p, 'found': True }

        return { 'page': {}, 'found': False }

    def test(self):
        """Test action"""
        return {'found': True, 
                'page': {'title': 'HelloWorld', 'space': 'DEMO', 'modifier': 'TestUser', 'created': '20161024T20:19:23Z', 'content': '<p>hello</p>', 'url': 'https://komand.atlassian.net/wiki/display/DEMO/HelloWorld', 'permissions': '0', 'creator': 'TestUser', 'parentId': '0', 'version': '1', 'homePage': 'false', 'id': '19726355', 'current': 'true', 'contentStatus': 'current', 'modified': '20161024T20:19:23Z'}}
