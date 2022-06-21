import insightconnect_plugin_runtime
from .schema import LookupDomainInput, LookupDomainOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_recorded_future.util.util import AvailableInputs
from komand_recorded_future.util.api import Endpoint
from urllib.parse import urlparse


class LookupDomain(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_domain",
            description=Component.DESCRIPTION,
            input=LookupDomainInput(),
            output=LookupDomainOutput(),
        )

    def run(self, params={}):
        comment = params.get(Input.COMMENT)
        if not comment:
            comment = None
        domain = params.get(Input.DOMAIN)
        try:
            self.logger.info(f"Looking up domain: {domain}")
            return {
                Output.DATA: insightconnect_plugin_runtime.helper.clean(
                    self.connection.client.make_request(
                        Endpoint.lookup_domain(self.get_domain(domain)),
                        {"fields": AvailableInputs.DomainFields, "comment": comment},
                    ).get("data")
                )
            }
        except AttributeError as e:
            raise PluginException(
                cause="Recorded Future returned an unexpected response.",
                assistance="Please check that the provided inputs are correct and try again.",
                data=e,
            )

    @staticmethod
    def get_domain(original_domain):
        stripped = urlparse(original_domain).netloc  # This returns null if it's not a URL
        if not stripped:
            stripped = original_domain.replace("https://", "").replace("http://", "").split("/")[0]
        return stripped
