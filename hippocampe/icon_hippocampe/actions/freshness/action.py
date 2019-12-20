import komand
from .schema import FreshnessInput, FreshnessOutput
# Custom imports below


class Freshness(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='freshness',
                description='Check if the feeds are up to date. A threshold can be defined in Hippocampe/core/conf/hippo/hippo.conf (by default 1 day)',
                input=FreshnessInput(),
                output=FreshnessOutput())

    def run(self, params={}):
        freshness = self.connection.api.freshness()
        return {'freshness_statuses': freshness}
