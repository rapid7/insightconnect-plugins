import insightconnect_plugin_runtime
from .schema import UrlLookupInput, UrlLookupOutput, Input, Component
from icon_ipqualityscore.util.api import URL_ENDPOINT


class UrlLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="urlLookup",
            description=Component.DESCRIPTION,
            input=UrlLookupInput(),
            output=UrlLookupOutput(),
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

        self.logger.info(f"[ACTION LOG] Getting information for URL: {params.get(Input.URL)} \n")

        response = self.connection.ipqs_client.ipqs_lookup(URL_ENDPOINT, additional_params)
        return response
