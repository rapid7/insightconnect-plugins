import insightconnect_plugin_runtime
import requests
from .schema import ValidateOutput, ValidateInput, Input, Output


class Validate(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="validate",
            description="Validate a HTML file",
            input=ValidateInput(),
            output=ValidateOutput(),
        )

    def run(self, params={}):
        # Configure requests

        headers = {"Content-Type": "text/html; charset=utf-8"}
        api_call = "https://validator.w3.org/nu/?out=json"
        html_data = params.get(Input.HTML_CONTENTS).encode()
        try:
            response = requests.post(api_call, headers=headers, data=html_data)
            msgs = response.json()["messages"]
            if len(msgs) == 0:
                self.logger.info("Run: No response from web service, can't determine validity")
                return {Output.VALIDATED: False}
            status = msgs[0]["type"]
            return {Output.VALIDATED: (False if status == "error" else True)}
        except requests.exceptions.RequestException:
            return {"status": "Error"}
