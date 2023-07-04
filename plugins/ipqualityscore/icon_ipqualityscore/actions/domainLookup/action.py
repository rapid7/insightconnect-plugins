import insightconnect_plugin_runtime
from .schema import DomainLookupInput, DomainLookupOutput, Input, Component
from icon_ipqualityscore.util.api import URL_ENDPOINT


class DomainLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="domainLookup",
            description=Component.DESCRIPTION,
            input=DomainLookupInput(),
            output=DomainLookupOutput(),
        )

    def run(self, params={}) -> dict:
        """
        This function creates a dictionary of the arguments sent to the IPQS
        API based on the ip_additional_params.
        Args:
            params(dict):User Inputs

        Returns:
            response: returns JSON response from the API

        """

        additional_params = {
            "url": params.get(Input.URL),
            "strictness": params.get(Input.STRICTNESS),
            "fast": params.get(Input.FAST),
        }

        self.logger.info(f"[ACTION LOG] Getting information for Domain: {params.get(Input.URL)} \n")

        response = self.connection.ipqs_client.ipqs_lookup(URL_ENDPOINT, additional_params)
        return response
