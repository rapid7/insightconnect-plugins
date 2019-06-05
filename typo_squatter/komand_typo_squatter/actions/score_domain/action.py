import komand
from .schema import ScoreDomainInput, ScoreDomainOutput
# Custom imports below
from komand_typo_squatter.util import utils


class ScoreDomain(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='score_domain',
                description='Get phishing score for domain',
                input=ScoreDomainInput(),
                output=ScoreDomainOutput())

    def run(self, params={}):
        domain = params.get('domain')
        return {'score': utils.score_domain(domain) }

    def test(self, params={}):
        return {'score': 0 }
