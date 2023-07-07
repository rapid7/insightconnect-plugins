import insightconnect_plugin_runtime
from .schema import PhoneLookupInput, PhoneLookupOutput, Input, Output, Component
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

        return {
            Output.ACTIVE: response.get("active") or False,
            Output.ACTIVE_STATUS: response.get("active_status") or "N/A",
            Output.CARRIER: response.get("carrier") or "N/A",
            Output.CITY: response.get("city") or "N/A",
            Output.COUNTRY: response.get("country") or "N/A",
            Output.DIALING_CODE: response.get("dialing_code") or 0,
            Output.DO_NOT_CALL: response.get("do_not_call") or False,
            Output.FORMATTED: response.get("formatted") or "null",
            Output.FRAUD_SCORE: response.get("fraud_score") or 0,
            Output.LEAKED: response.get("leaked") or False,
            Output.LINE_TYPE: response.get("line_type") or "Unknown",
            Output.LOCAL_FORMAT: response.get("local_format") or "null",
            Output.NAME: response.get("name") or "N/A",
            Output.PREPAID: response.get("prepaid") or False,
            Output.RECENT_ABUSE: response.get("recent_abuse") or False,
            Output.REGION: response.get("region") or "N/A",
            Output.RISKY: response.get("risky") or False,
            Output.TIMEZONE: response.get("timezone") or "N/A",
            Output.VALID: response.get("valid") or False,
            Output.VOIP: response.get("VOIP") or False,
            Output.ZIP_CODE: response.get("zip_code") or "N/A",
        }
