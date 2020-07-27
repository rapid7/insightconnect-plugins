import komand
from .schema import GetRuleInput, GetRuleOutput, Input, Output, Component
# Custom imports below
from komand.helper import clean
from threatstack.errors import ThreatStackAPIError, ThreatStackClientError, APIRateLimitError
from komand.exceptions import PluginException


class GetRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_rule',
                description=Component.DESCRIPTION,
                input=GetRuleInput(),
                output=GetRuleOutput())

    def run(self, params={}):
        rule_id, ruleset_id = params.get(Input.RULE_ID), params.get(Input.RULESET_ID)

        try:
            rule = clean(self.connection.client.rulesets.rules(ruleset_id=ruleset_id, rule_id=rule_id))
        except (ThreatStackAPIError, ThreatStackClientError, APIRateLimitError) as e:
            raise PluginException(cause="An error occurred!",
                                  assistance=e)

        return {Output.RULE: rule}
