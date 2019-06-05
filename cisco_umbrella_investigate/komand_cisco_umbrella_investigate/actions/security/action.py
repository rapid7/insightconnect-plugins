import komand
from .schema import SecurityInput, SecurityOutput
# Custom imports below


class Security(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='security',
                description='Returns scores or security features',
                input=SecurityInput(),
                output=SecurityOutput())

    def run(self, params={}):
        domain = params.get('domain')
        try:
            security = self.connection.investigate.security(domain)
        except Exception as e:
            self.logger.error("Security: Run: Problem with request")
            raise e

        if not security:
            self.logger.error("Security: Run: Empty response")
            raise Exception("Security: Run: Empty response")

        founded = security.get('found')
        if founded:
            return security

        self.logger.error("Security: Run: Empty response")
        raise Exception("Security: Run: Empty response")

    def test(self):
        return {"perplexity": 0.7094969698613228, "rip_score": 0.0, "pagerank": 26.562752, "ks_test": 0.08091062281942614, "prefix_score": -0.08946425298980197, "attack": "", "popularity": 100.0, "dga_score": 0.0, "entropy": 1.9182958340544893, "asn_score": -0.038553127375745636, "found": True, "securerank2": 72.88158945368073, "threat_type": "", "geodiversity_normalized": [["BQ", 6.74413149488837e-08]], "geoscore": 0.0006307167215251743, "geodiversity": [["BD", 0.00010912265], ["GI", 0.00010912265]], "fastflux": False, "tld_geodiversity": [["SE", 0.010081927958847051]]}
