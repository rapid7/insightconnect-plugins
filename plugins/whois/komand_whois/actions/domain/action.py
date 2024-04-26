import insightconnect_plugin_runtime
from .schema import DomainInput, DomainOutput, Input, Output

# Custom imports below
import whois
import validators
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean


class Domain(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domain",
            description="Whois Domain Lookup",
            input=DomainInput(),
            output=DomainOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain = params.get(Input.DOMAIN, "")
        # END INPUT BINDING - DO NOT REMOVE

        if not validators.domain(domain):
            raise PluginException(
                cause="Invalid domain as input.",
                assistance="Ensure the domain is not prefixed with a protocol.",
            )

        try:
            self.logger.info(f"Getting whois information for {domain}")
            lookup_results = whois.query(domain, ignore_returncode=1)  # ignore_returncode required for plugin
        except Exception as error:
            self.logger.error(f"Error occurred: {error}")
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        if not lookup_results:
            raise PluginException(
                cause="Error: Request did not return any data.",
                assistance="Please check provided domain and try again.",
            )

        return clean(lookup_results.get_json_serializable())
