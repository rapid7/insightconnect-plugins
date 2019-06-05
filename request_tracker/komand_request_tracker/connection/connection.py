import komand
from .schema import ConnectionSchema
# Custom imports below
import urllib
import urllib.parse
import rt

BASE_URL = '/REST/1.0/'

class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        user = params.get('credentials').get('username')
        password = params.get('credentials').get('password')
        url = params.get('url')
        url = urllib.parse.urljoin(url, BASE_URL)
        tracker = rt.Rt(url, user, password)
        try:
            if not tracker.login():
                self.logger.error('RequestTracker: Connect: error %s', params)
                raise Exception('RequestTracker: Connect: user could not be authenticated please try again.')
        except rt.ConnectionError as e:
            self.logger.error('RequestTracker: Connect: error %s', str(e))
            raise Exception('RequestTracker: Connect: Failed to connect to server {}'.format(url))

        self.tracker = tracker
