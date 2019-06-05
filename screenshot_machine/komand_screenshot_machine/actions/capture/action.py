import komand
from .schema import CaptureInput, CaptureOutput
# Custom imports below
import requests
import base64
import hashlib


class Capture(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='capture',
                description='Capture URL Screenshot',
                input=CaptureInput(),
                output=CaptureOutput())

    def size(self, size='tiny'):
        sizes = {
                'tiny': 'T',
                'small': 'S',
                'seminormal':'E',
                'normal' :'N',
                'medium':'M',
                'large':'L',
                'extra_large':'X',
                'full':'F',
                'mobile_normal':'Nmob',
                'mobile_full':'Fmob',
                }

        return sizes.get(size) or 'T'

    def run(self, params={}):
        url = params['url']
        params = {
            'url': params['url'],
            'size': self.size(params.get('size')),
            'key': self.connection.key,
            'format': params.get('format') or 'JPG',
            'cacheLimit': params.get('cache_age_days') or 0,
            'timeout': params.get('timeout'),
        }

        if self.connection.secret:
            hash_ = hashlib.md5((params['url'] + self.connection.secret).encode('ascii')).hexdigest()
            params['hash'] = hash_

        res = requests.get(self.connection.base, params=params)

        self.logger.debug('Response is %d', res.status_code)

        if res.status_code != requests.codes.ok:
            self.logger.error('Unable to capture screenshot %d %s', res.status_code, res.text)
            raise Exception('Failure to submit url')

        content = base64.b64encode(res.content)
        content = content.decode("utf-8")
        filename = "".join([c for c in url if c.isalpha() or c.isdigit() or c==' ']).rstrip() + '.' + (params.get('format') or 'JPG')

        return {'url': url,
                'screenshot': {
                    'filename': filename,
                    'content': content,
                }
        }

    def test(self):
        """TODO: Test action"""
        return {}

    def test(self):
        # TODO: Implement test function
        return {}
