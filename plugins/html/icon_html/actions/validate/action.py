import insightconnect_plugin_runtime
import requests
from .schema import ValidateOutput, ValidateInput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException


class Validate(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="validate",
            description=Component.DESCRIPTION,
            input=ValidateInput(),
            output=ValidateOutput(),
        )

    def run(self, params={}):
        # Configure requests

        headers = {"Content-Type": "text/html; charset=utf-8"}
        api_call = "https://validator.w3.org/nu/?out=json"
        html_data = params.get(Input.HTML_CONTENTS).encode()
        try:
            response = requests.post(api_call, headers=headers, data=html_data, timeout=10)
            msgs = response.json()["messages"]
            if len(msgs) == 0:
                self.logger.info("Run: No response from web service, can't determine validity")
                return {Output.VALIDATED: False}
            status = msgs[0]["type"]
            return {Output.VALIDATED: (not status == "error")}
        except requests.exceptions.RequestException:
            return PluginException(cause="Error validating input. ", assistance="Please check logs.")
