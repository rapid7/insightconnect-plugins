import komand
from .schema import AddAccessRuleInput, AddAccessRuleOutput, Input, Output, Component
# Custom imports below
import requests
from komand.exceptions import PluginException

class AddAccessRule(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_access_rule',
                description=Component.DESCRIPTION,
                input=AddAccessRuleInput(),
                output=AddAccessRuleOutput())

    def run(self, params={}):
        url = f"https://{self.connection.server_ip}:{self.connection.server_port}/web_api/add-access-rule"

        # Position will accept an int or string like "top" or "bottom"
        position_string = params.get(Input.POSITION)
        try:
            position = int(position_string)
        except Exception:
            position = position_string

        payload = {
          "layer" : params.get(Input.LAYER),
          "position" : position,
          "name" : params.get(Input.NAME),
          "service" : params.get(Input.LIST_OF_SERVICES),
          "action" : params.get(Input.ACTION)
        }

        headers = self.connection.get_headers()
        self.logger.info(f"Adding access rule at: {url}")
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

        self.connection.publish() # You need to do this to save changes to the server

        return {Output.ACCESS_RULE: result.json()}
