import komand
from .schema import UnshortenInput, UnshortenOutput
# Custom imports below
import requests


class Unshorten(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='unshorten',
                description='Unshorten a shortened URL',
                input=UnshortenInput(),
                output=UnshortenOutput())

    def run(self, params={}):
        short_url = params.get('url')
        try:
            r = requests.get('https://unshorten.me/json/' + short_url)
            r.raise_for_status()
            out = r.json()
        except Exception as e:
            self.logger.error(e)
            raise

        try:
            if out['error']:
                self.logger.error(out.get('error'))
        except KeyError:
            # All good, no error key is present
            self.logger.info('No errors')

        return out

    def test(self):
        url = 'https://bit.ly/komand_rocks'
        try:
            r = requests.get('https://unshorten.me/json/' + url)
            r.raise_for_status()
            out = r.json()
        except Exception as e:
            self.logger.error(e)
            raise

        # All good
        try:
            if out['error']:
                self.logger.error(out.get('error'))
        except KeyError:
            # All good, no error key is present
            self.logger.info('No errors')

        return out
