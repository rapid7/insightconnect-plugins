import insightconnect_plugin_runtime
from .schema import EmailLookupInput, EmailLookupOutput, Input, Component
from icon_ipqualityscore.util.api import EMAIL_ENDPOINT


class EmailLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="emailLookup",
            description=Component.DESCRIPTION,
            input=EmailLookupInput(),
            output=EmailLookupOutput(),
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
            "email": params.get(Input.EMAILADDRESS),
            "abuse_strictness": params.get(Input.ABUSE_STRICTNESS),
            "fast": params.get(Input.FAST),
            "timeout": params.get(Input.TIMEOUT),
            "suggest_domain": params.get(Input.SUGGEST_DOMAIN),
        }

        self.logger.info(f"[ACTION LOG] Getting information for Email address: {params.get(Input.EMAILADDRESS)} \n")
        response = self.connection.ipqs_client.ipqs_lookup(EMAIL_ENDPOINT, additional_params)
        return response
