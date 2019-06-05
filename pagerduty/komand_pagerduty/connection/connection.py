import komand
from .schema import ConnectionSchema
# Custom imports below
import pypd


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        """
        Connect to PagerDuty
        """

        key = params.get('api_key').get('secretKey')
        pypd.api_key = key
        self.logger.debug("Connecting: %s", key)
        pypd.Incident.find(maximum=1)
