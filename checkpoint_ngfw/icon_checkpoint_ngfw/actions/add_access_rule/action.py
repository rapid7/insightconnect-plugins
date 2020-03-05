import komand
from .schema import AddAccessRuleInput, AddAccessRuleOutput, Input, Output, Component
# Custom imports below
import requests


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
          "layer": params.get(Input.LAYER),
          "position": position,
          "name": params.get(Input.NAME),
          "action": params.get(Input.ACTION),
        }

        services = params.get(Input.LIST_OF_SERVICES, [])
        if len(services) > 0:  # Make sure it's not a blank list
            payload["services"] = services

        source = params.get(Input.SOURCE)
        if source:
            payload["source"] = source

        destination = params.get(Input.DESTINATION)
        if destination:
            payload["destination"] = destination

        discard_other_sessions = params.get(Input.DISCARD_OTHER_SESSIONS)

        headers = self.connection.get_headers()

        self.logger.info(f"Adding access rule at: {url}")
        result = self.connection.post_and_publish(headers, discard_other_sessions, payload, url)

        return {Output.ACCESS_RULE: result.json()}
