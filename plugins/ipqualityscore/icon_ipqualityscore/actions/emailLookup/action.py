import insightconnect_plugin_runtime
from .schema import EmailLookupInput, EmailLookupOutput, Input, Output, Component
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
        return {
            Output.CATCH_ALL: response.get("catch_all") or False,
            Output.COMMON: response.get("common") or False,
            Output.DELIVERABILITY: response.get("deliverability") or "N/A",
            Output.DISPOSABLE: response.get("disposable") or False,
            Output.DNS_VALID: response.get("dns_valid") or False,
            Output.DOMAIN_AGE: response.get("domain_age") or {},
            Output.FIRST_NAME: response.get("first_name") or "none",
            Output.FIRST_SEEN: response.get("first_seen") or {},
            Output.FRAUD_SCORE: response.get("fraud_score") or 0,
            Output.FREQUENT_COMPLAINER: response.get("frequent_complainer") or False,
            Output.GENERIC: response.get("generic") or False,
            Output.HONEYPOT: response.get("honeypot") or False,
            Output.LEAKED: response.get("leaked") or False,
            Output.OVERALL_SCORE: response.get("overall_score") or 0,
            Output.RECENT_ABUSE: response.get("recent_abuse") or False,
            Output.SANITIZED_EMAIL: response.get("sanitized_email") or "N/A",
            Output.SMTP_SCORE: response.get("smtp_score") or 0,
            Output.SPAM_TRAP_SCORE: response.get("spam_trap_score") or "none",
            Output.SUGGESTED_DOMAIN: response.get("suggested_domain") or "none",
            Output.SUSPECT: response.get("suspect") or False,
            Output.TIMED_OUT: response.get("timed_out") or False,
            Output.VALID: response.get("valid") or False,
        }
