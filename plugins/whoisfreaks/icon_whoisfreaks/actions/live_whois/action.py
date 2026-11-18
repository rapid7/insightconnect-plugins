import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import LiveWhoisInput, LiveWhoisOutput, Input, Output, Component

# Custom imports below
from icon_whoisfreaks.util import constants, outputs, validators


class LiveWhois(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="live_whois",
            description=Component.DESCRIPTION,
            input=LiveWhoisInput(),
            output=LiveWhoisOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        domain = params.get(Input.DOMAIN)
        # END INPUT BINDING - DO NOT REMOVE

        result = self.connection.client.lookup(
            "Live WHOIS", "GET", constants.PATH_LIVE_WHOIS, {"domainName": validators.domain(domain)}
        )
        data = result.data_dict
        # Thin registries such as .com return the registrar and status codes only in registry_data
        registry = outputs.get_path(data, "registry_data")

        def field(*path):
            value = outputs.get_path(data, *path)
            return value if value not in (None, "", []) else outputs.get_path(registry, *path)

        return outputs.single(
            result,
            {
                Output.REGISTERED: outputs.to_bool(field("domain_registered")),
                Output.CREATE_DATE: outputs.to_str(field("create_date")),
                Output.UPDATE_DATE: outputs.to_str(field("update_date")),
                Output.EXPIRY_DATE: outputs.to_str(field("expiry_date")),
                Output.REGISTRAR_NAME: outputs.to_str(field("domain_registrar", "registrar_name")),
                Output.NAME_SERVERS: outputs.to_str_list(field("name_servers")),
                Output.DOMAIN_STATUS: outputs.to_str_list(field("domain_status")),
            },
        )
