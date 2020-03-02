import komand
from .schema import RemoveAccessRuleInput, RemoveAccessRuleOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException

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

        result = requests.post(url, headers=headers, json=payload, verify=self.connection.ssl_verify)

        # This gets odd. If you try to publish a change while someone else is working on a change it will fail
        # I give the user an option to discard all sessions, however, I don't want to do that unless I have to
        # as it's an expensive operation (could take a couple minutes)
        # So, try to make the change, if it's locked, see if we need to discard all sessions and try to make the
        # call again.
        try:
            result.raise_for_status()
        except Exception as e:
            self.logger.warning(result.text)
            if "object is locked" in result.text:
                if params.get(Input.DISCARD_OTHER_SESSIONS):
                    self.connection.discard_all_sessions()
                    result = requests.post(url, headers=headers, json=payload, verify=self.connection.ssl_verify)

            # try to see if we still have a bad request
            try:
                result.raise_for_status()
            except Exception as e:
                raise PluginException(cause=f"Create rule {params.get(Input.NAME)} failed.",
                                      assistance=result.text,
                                      data=e)

        self.connection.publish()
        message = result.json().get("message")
        success = 'OK' == message

        return {Output.SUCCESS: success, Output.MESSAGE: message}
