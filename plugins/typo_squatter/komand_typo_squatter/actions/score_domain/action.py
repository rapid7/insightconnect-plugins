import insightconnect_plugin_runtime
from .schema import ScoreDomainInput, ScoreDomainOutput, Input, Output, Component

# Custom imports below
from komand_typo_squatter.util import utils


class ScoreDomain(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="score_domain",
            description=Component.DESCRIPTION,
            input=ScoreDomainInput(),
            output=ScoreDomainOutput(),
        )

    def run(self, params={}):
        return {Output.SCORE: utils.score_domain(params.get(Input.DOMAIN))}
