import komand
from .schema import CheckInput, CheckOutput
# Custom imports below
import requests


class Check(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check',
                description='Submit URL to Phishtank',
                input=CheckInput(),
                output=CheckOutput())

    def run(self, params={}):
        url = params.get('url')
        if not url:
            raise ValueError('url is required')

        url = url.strip()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        try:
            result = self.connection.check(url)
            self.logger.debug("result: %s", result)
        except Exception as e:
            self.logger.exception(e)
            return {
                'url': url,
                'in_database': False,
                'verified': False,
                }

        if 'verified_at' in result:
            if result['verified_at'] is None:
                result['verified_at'] = str(result['verified_at'])

        return result

    def test(self):
        url = "http://cielobbfidelidade.xyz/home/"

        try:
            result = self.connection.check(url)
        except Exception as e:
            self.logger.exception(e)
            return {
                'url': url,
                'in_database': False,
                'verified': False,
                }

        return result