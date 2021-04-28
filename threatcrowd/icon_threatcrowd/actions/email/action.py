import insightconnect_plugin_runtime
from .schema import EmailInput, EmailOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
import validators


class Email(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="email", description=Component.DESCRIPTION, input=EmailInput(), output=EmailOutput()
        )

    def run(self, params={}):
        if not validators.email(params.get(Input.EMAIL)):
            self.logger.info("User input was not an email.")
            raise PluginException(
                cause="A valid e-mail address was not provided.",
                assistance="Update this action with valid e-mail input.",
            )

        data = self.connection.client.search_email(params.get(Input.EMAIL))
        if not data or int(data["response_code"]) == 0:
            self.logger.info("ThreatCrowd API did not return any matches.")
            return {Output.FOUND: False}

        return {
            Output.DOMAINS: insightconnect_plugin_runtime.helper.clean_list(data["domains"]),
            Output.PERMALINK: data["permalink"],
            Output.REFERENCES: insightconnect_plugin_runtime.helper.clean_list(data["references"]),
            Output.FOUND: True,
        }
