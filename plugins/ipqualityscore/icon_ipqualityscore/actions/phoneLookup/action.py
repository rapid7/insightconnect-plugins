import insightconnect_plugin_runtime
from .schema import PhoneLookupInput, PhoneLookupOutput, Input, Component
from icon_ipqualityscore.util.api import PHONE_ENDPOINT


class PhoneLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="phoneLookup",
            description=Component.DESCRIPTION,
            input=PhoneLookupInput(),
            output=PhoneLookupOutput(),
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
            "phone": params.get(Input.PHONE),
            "strictness": params.get(Input.STRICTNESS),
            "country": params.get(Input.COUNTRY, ""),
        }

        self.logger.info(f"[ACTION LOG] Getting information for Phone: {params.get(Input.PHONE)} \n")
        response = self.connection.ipqs_client.ipqs_lookup(PHONE_ENDPOINT, additional_params)
        return response
