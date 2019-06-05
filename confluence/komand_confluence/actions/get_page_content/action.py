import komand
from .schema import GetPageContentInput, GetPageContentOutput
# Custom imports below
from ...util import util


class GetPageContent(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_page_content',
                description='Get Page Content',
                input=GetPageContentInput(),
                output=GetPageContentOutput())

    def run(self, params={}):
        page = params['page']
        space = params['space']
        p = self.connection.client.getPage(page, space)
        if p:
            p = util.normalize_page(p)
            return { 'content': p['content'], 'found': True }

        return { 'found': False, 'content': '' }

    def test(self):
        """Return content"""
        return { 'found': True, 'content': '' }
