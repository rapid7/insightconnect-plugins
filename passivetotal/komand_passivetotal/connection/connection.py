import komand
from .schema import ConnectionSchema
# Custom imports below
import passivetotal.libs.enrichment
import passivetotal.libs.whois


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        username = params.get('username')
        api_key = params.get('api_key').get('secretKey')
        self.logger.info("Connecting...")
        self.enrichment = passivetotal.libs.enrichment.EnrichmentRequest(username, api_key)
        self.whois = passivetotal.libs.whois.WhoisRequest(username, api_key)
        self.username = username
        self.api_key = api_key
