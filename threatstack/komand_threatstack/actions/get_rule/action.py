import komand
from .schema import GetRuleInput, GetRuleOutput, Input, Output, Component
# Custom imports below


class GetRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_rule',
                description=Component.DESCRIPTION,
                input=GetRuleInput(),
                output=GetRuleOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
