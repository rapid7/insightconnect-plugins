import insightconnect_plugin_runtime
import requests
from .schema import ValidateOutput, ValidateInput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_html.util.constants import REQUESTS_TIMEOUT


class Validate(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="validate",
            description=Component.DESCRIPTION,
            input=ValidateInput(),
            output=ValidateOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        html_contents = params.get(Input.HTML_CONTENTS, "").encode()
        # END INPUT BINDING - DO NOT REMOVE

        try:
            response = requests.post(
                "https://validator.w3.org/nu/?out=json",
                headers={"Content-Type": "text/html; charset=utf-8"},
                data=html_contents,
                timeout=REQUESTS_TIMEOUT,
            )
            messages = response.json()["messages"]
            if not messages:
                self.logger.info(
                    "Run: No response from web service, can't determine validity"
                )
                return {Output.VALIDATED: False}
            status = messages[0]["type"]
            return {Output.VALIDATED: (not status == "error")}
        except requests.exceptions.RequestException as error:
            raise PluginException(
                cause="Error validating input.",
                assistance="Please check logs.",
                data=error,
            )
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)
