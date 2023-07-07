import insightconnect_plugin_runtime
from .schema import IpLookupInput, IpLookupOutput, Input, Output, Component
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
        return {
            Output.FRAUD_SCORE: response.get("fraud_score") or 1,
            Output.COUNTRY_CODE: response.get("country_code") or "none",
            Output.REGION: response.get("region") or "none",
            Output.CITY: response.get("city") or "none",
            Output.ZIP_CODE: response.get("zip_code") or "none",
            Output.ISP: response.get("ISP") or "none",
            Output.ASN: response.get("ASN") or 0,
            Output.ORGANIZATION: response.get("organization") or "none",
            Output.IS_CRAWLER: response.get("is_crawler") or False,
            Output.TIMEZONE: response.get("timezone") or "none",
            Output.MOBILE: response.get("mobile") or False,
            Output.HOST: response.get("host") or "none",
            Output.PROXY: response.get("proxy") or False,
            Output.VPN: response.get("vpn") or False,
            Output.TOR: response.get("tor") or False,
            Output.ACTIVE_VPN: response.get("active_vpn") or False,
            Output.ACTIVE_TOR: response.get("active_tor") or False,
            Output.RECENT_ABUSE: response.get("recent_abuse") or False,
            Output.BOT_STATUS: response.get("bot_status") or False,
            Output.CONNECTION_TYPE: response.get("connection_type") or "none",
            Output.ABUSE_VELOCITY: response.get("abuse_velocity") or "none",
            Output.LATITUDE: response.get("latitude") or 0.0,
            Output.LONGITUDE: response.get("longitude") or 0.0,
        }
