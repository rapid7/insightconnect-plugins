import komand
from .schema import ExpandInput, ExpandOutput
# Custom imports below
from komand_url_expander.util import util


class Expand(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='expand',
                description='Expand a shortened URL',
                input=ExpandInput(),
                output=ExpandOutput())

    def run(self, params={}):
        url = params['url']
        follow = params.get('follow')

        if follow:
            resp = komand.helper.open_url(url)
            return {'url': resp.url}

        resp = util.unshorten_url(url)
        return {'url': resp}

    def test(self):
        # TODO: Implement test function
        return {}
