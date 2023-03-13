import insightconnect_plugin_runtime
from .schema import SecurityInput, SecurityOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Security(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="security",
            description="Returns scores or security features",
            input=SecurityInput(),
            output=SecurityOutput(),
        )

    def run(self, params={}):
        domain = params.get(Input.DOMAIN)
        try:
            security = self.connection.investigate.security(domain)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        if not security:
            raise PluginException(
                cause="An empty response was given.",
                assistance="A security score for the domain may not exist, please try another query.",
            )

        founded = security.get("found")
        if founded:
            return security

        raise PluginException(preset=PluginException.Preset.UNKNOWN)
