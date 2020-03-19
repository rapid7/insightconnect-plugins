import komand
from .schema import RemoveAccessRuleInput, RemoveAccessRuleOutput, Input, Output, Component
# Custom imports below
import string

class RemoveAccessRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_access_rule',
                description=Component.DESCRIPTION,
                input=RemoveAccessRuleInput(),
                output=RemoveAccessRuleOutput())

    def run(self, params={}):
        url = f"{self.connection.server_and_port}/web_api/v1.1/delete-access-rule"
        headers = self.connection.get_headers()
        payload = {
            "name": params.get(Input.ACCESS_RULE_NAME),
            "layer": params.get(Input.LAYER)
        }
        discard_other_sessions = params.get(Input.DISCARD_OTHER_SESSIONS, False)

        result = self.connection.post_and_publish(headers, discard_other_sessions, payload, url)

        message = result.json().get("message")
        success = 'OK' == message.upper()

        return {Output.SUCCESS: success, Output.MESSAGE: message}
