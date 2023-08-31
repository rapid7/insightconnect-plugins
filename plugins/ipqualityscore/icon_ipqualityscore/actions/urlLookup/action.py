import insightconnect_plugin_runtime
from .schema import UrlLookupInput, UrlLookupOutput, Input, Output, Component
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
        return {
            Output.ADULT: response.get("adult") or False,
            Output.CATEGORY: response.get("category") or "N/A",
            Output.DNS_VALID: response.get("dns_valid") or False,
            Output.DOMAIN: response.get("domain") or "N/A",
            Output.DOMAIN_AGE: response.get("domain_age") or {},
            Output.DOMAIN_RANK: response.get("domain_rank") or 0,
            Output.IP_ADDRESS: response.get("ip_address") or "N/A",
            Output.MALWARE: response.get("malware") or False,
            Output.PARKING: response.get("parking") or False,
            Output.PHISHING: response.get("phishing") or False,
            Output.RISK_SCORE: response.get("risk_score") or 0,
            Output.SERVER: response.get("server") or "N/A",
            Output.SPAMMING: response.get("spamming") or False,
            Output.SUSPICIOUS: response.get("suspicious") or False,
            Output.UNSAFE: response.get("unsafe") or False,
        }
