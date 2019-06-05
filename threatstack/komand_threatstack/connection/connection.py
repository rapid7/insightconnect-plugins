import komand
from .schema import ConnectionSchema
# Custom imports below
from threatstack import ThreatStack


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        k = params['api_key']
        params['api_key'] = k['secretKey']
        if params.get('org_id') == '':
            params['org_id'] = None

        self.client = ThreatStack(**params)
