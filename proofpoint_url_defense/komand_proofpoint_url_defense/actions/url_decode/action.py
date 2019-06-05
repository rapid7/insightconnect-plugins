import komand
from .schema import UrlDecodeInput, UrlDecodeOutput
# Custom imports below
import ppdecode


class UrlDecode(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='url_decode',
                description='Decodes an encoded URL',
                input=UrlDecodeInput(),
                output=UrlDecodeOutput())

    def run(self, params={}):
        url = 'https://urldefense.proofpoint.com/v2/url?u='
        if params.get("encoded_url").startswith(url):
            encoded_url = params.get("encoded_url")
        else:
            encoded_url = url + params.get("encoded_url")

        try:
            decoded_url = ppdecode.ppdecode(encoded_url)
            self.logger.info('URL has been decoded')
            return {'decoded_url': decoded_url['decoded_url']}
        except Exception:
            self.logger.error("Unexpected issue occurred decoding URL")
            raise

    def test(self):
        url = 'https://urldefense.proofpoint.com/v2/url?u=http-3A__www.example.org_url&d=BwdwBAg&c=TIwfCwdwWnrHy3gMA_uzZorHPsT2wfwvKrwfU'

        try:
            decoded_url = ppdecode.ppdecode(url)
            self.logger.info('URL has been decoded')
        except:
            self.logger.error("Unexpected issue occurred decoding URL")
            raise

        return {'decoded_url': decoded_url['decoded_url']}
