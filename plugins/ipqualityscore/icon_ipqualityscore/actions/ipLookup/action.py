import insightconnect_plugin_runtime
from .schema import IpLookupInput, IpLookupOutput, Input, Component
from icon_ipqualityscore.util.api import IP_ENDPOINT


class IpLookup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="ipLookup",
            description=Component.DESCRIPTION,
            input=IpLookupInput(),
            output=IpLookupOutput(),
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
            "ip": params.get(Input.IPADDRESS),
            "strictness": params.get(Input.STRICTNESS),
            "user_agent": params.get(Input.USER_AGENT, " "),
            "user_language": params.get(Input.USER_LANGUAGE, " "),
            "fast": params.get(Input.FAST),
            "mobile": params.get(Input.MOBILE),
            "allow_public_access_points": params.get(Input.ALLOW_PUBLIC_ACCESS_POINTS),
            "lighter_penalties": params.get(Input.LIGHTER_PENALTIES),
        }
        self.logger.info(f"[ACTION LOG] Getting information for IP address: {params.get(Input.IPADDRESS)} \n")
        response = self.connection.ipqs_client.ipqs_lookup(IP_ENDPOINT, additional_params)
        return response
