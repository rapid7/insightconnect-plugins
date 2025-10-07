import insightconnect_plugin_runtime
from .schema import LookupIpAddressInput, LookupIpAddressOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_recorded_future.util.util import AvailableInputs
from komand_recorded_future.util.api import Endpoint


class LookupIpAddress(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_ip_address",
            description=Component.DESCRIPTION,
            input=LookupIpAddressInput(),
            output=LookupIpAddressOutput(),
        )

    def run(self, params={}):
        comment = params.get(Input.COMMENT)
        if not comment:
            comment = None

        try:
            return {
                Output.RESULT_FOUND: True,
                Output.DATA: insightconnect_plugin_runtime.helper.clean(
                    self.connection.client.make_request(
                        Endpoint.lookup_ip_address(params.get(Input.IP_ADDRESS)),
                        {"fields": AvailableInputs.IpFields, "comment": comment},
                    ).get("data")
                ),
            }
        except AttributeError as error:
            raise PluginException(
                cause="Recorded Future returned unexpected response.",
                assistance="Please check that the provided inputs are correct and try again.",
                data=error,
            )
        except PluginException as error:
            if "No results found." in error.cause:
                return {Output.RESULT_FOUND: False, Output.DATA: {}}
            raise error
