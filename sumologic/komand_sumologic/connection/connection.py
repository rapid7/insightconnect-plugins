import komand
from .schema import ConnectionSchema
# Custom imports below
from sumologic import SumoLogic


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
      access_id = params.get('access_id').get('secretKey')
      access_key = params.get('access_key').get('secretKey')
      self.client = SumoLogic(access_id, access_key)

