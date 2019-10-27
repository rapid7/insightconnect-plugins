import komand
from .schema import ExpandAllInput, ExpandAllOutput
# Custom imports below
import re
from komand_url_expander.util import util


class ExpandAll(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='expand_all',
                description='Expand all shortened URLs in some text',
                input=ExpandAllInput(),
                output=ExpandAllOutput())


    def run(self, params={}):
        """Run action"""
        text = params['text']
        follow = params.get('follow')

        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        for url in urls:
            if follow:
                try:
                    resp = komand.helper.open_url(url)
                except Exception as e:
                    self.logger.debug("No response found: %s", e)
                    resp = None
                if resp and resp.url and resp.url != url:
                    text = text.replace(url, resp.url, -1)
            else:
                try:
                    resp = util.unshorten_url(url)
                except Exception as e:
                    self.logger.debug("No response found: %s", e)
                    resp = None
                if resp is not None and resp != url:
                    text = text.replace(url, resp, -1)

        return {'text': text}

    def test(self):
        """Test action"""
        return {'text': ''}
