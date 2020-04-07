import komand
from .schema import SubmitUrlInput, SubmitUrlOutput
# Custom imports below
from komand.exceptions import PluginException
import requests
import xmltodict


class SubmitUrl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='submit_url',
                description='Submit a URL for analysis',
                input=SubmitUrlInput(),
                output=SubmitUrlOutput())

    def run(self, params={}):
        """TODO: Run action"""
        endpoint =  "/publicapi/submit/link"
        client = self.connection.client
        url = 'https://{}{}'.format(self.connection.host, endpoint)

        # Formatted with None and tuples so requests sends form-data properly
        # => Send data, 299 bytes (0x12b)
        # 0000: --------------------------8557684369749613
        # 002c: Content-Disposition: form-data; name="apikey"
        # 005b:
        # 005d: 740219c8fab2606b9206b2d40626b2d1
        # 007f: --------------------------8557684369749613
        # 00ab: Content-Disposition: form-data; name="format"
        # 00d8:
        # 00da: pdf
        # 00fd: --------------------------8557684369749613--
        # ...

        req = {
            'apikey': (None, self.connection.api_key),
            'link': (None, params.get('url')),
        }

        try:
            r = requests.post(url, files=req)
            o = xmltodict.parse(r.content)
            out = dict(o)

            #self.logger.info(out)
            #{
            #   "submission": {
            #     "error": {
            #       "error-message": "'Invalid webpage type url, url should start with http or https'"
            #     }
            #   }
            #}
            if 'submission' in out:
                if 'error' in out['submission']:
                    if 'error-message' in out['submission']['error']:
                      error = out['submission']['error']['error-message']
                      raise PluginException(cause='Received an error response from Wildfire.', assistance=f'{error}.')

            # A different response occurs sometimes
            # {'error': OrderedDict([('error-message', "'Invalid webpage type url, url should start with http or https'")])}
            if 'error' in out:
                if 'error-message' in out['error']:
                  error = out['error']['error-message']
                  raise PluginException(cause='Received an error response from Wildfire.', assistance=f'{error}.')
                else:
                  self.logger.info(out)
                  raise PluginException(cause='Received an error response from Wildfire.', assistance="Check the log output for more details.")

            out = dict(o['wildfire']['submit-link-info'])
        except:
            raise

        return { 'submission': out }

    def test(self):
        """TODO: Test action"""
        client = self.connection.client
        return { 'submission': { 'url': 'Test', 'sha256': 'Test', 'md5': 'Test' } }
