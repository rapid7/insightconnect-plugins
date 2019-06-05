import komand
from .schema import GetSubdomainsInput, GetSubdomainsOutput
# Custom imports below


class GetSubdomains(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_subdomains',
                description='Get subdomains https://api.passivetotal.org/api/docs/#api-Enrichment-GetV2EnrichmentSubdomains',
                input=GetSubdomainsInput(),
                output=GetSubdomainsOutput())

    def run(self, params={}):
        results = self.connection.enrichment.get_subdomains(query=[params["query"]])
        subdomains = results.get('subdomains') or []
        count = len(subdomains)
        return {'count': count, 'subdomains': subdomains}

    def test(self):
        """Test action"""
        results = self.connection.enrichment.get_subdomains(query=["*.passivetotal.org"])
        subdomains = results.get('subdomains') or []
        count = len(subdomains)
        return {'count': count, 'subdomains': subdomains}
