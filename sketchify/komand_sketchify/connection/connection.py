import komand
from .schema import ConnectionSchema
from komand.exceptions import ConnectionTestException
# Custom imports below
import requests


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        pass

    def test(self):
        try:
            r = requests.post('https://verylegit.link/sketchify', data={'long_url': 'test'})
            r.raise_for_status()
            sketchy_url = r.content
        except Exception as e:
            self.logger.error(e)
            raise ConnectionTestException(cause='Server Error',
                                          assistance="Can't create url",
                                          data=e)

        return {'url': sketchy_url.decode()}
