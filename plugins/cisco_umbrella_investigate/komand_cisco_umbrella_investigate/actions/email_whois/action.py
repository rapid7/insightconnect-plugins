import insightconnect_plugin_runtime
from .schema import EmailWhoisInput, EmailWhoisOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from validate_email import validate_email


class EmailWhois(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="email_whois",
            description="Returns the WHOIS information for the specified email address(es), nameserver(s) and domains",
            input=EmailWhoisInput(),
            output=EmailWhoisOutput(),
        )

    def run(self, params={}):
        email = params.get(Input.EMAIL)
        is_valid = validate_email(email)
        if not is_valid:
            raise PluginException(preset=PluginException.Preset.UNKNOWN)

        try:
            email_whois = self.connection.investigate.email_whois(email)
        except Exception as error:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        one_email_whois = email_whois.get(email)
        if not one_email_whois:
            raise PluginException(
                cause="Unable to return WHOIS data.",
                assistance="Please try submitting another query.",
            )

        return {
            Output.EMAIL_WHOIS: [
                {
                    "more_data_available": one_email_whois.get("moreDataAvailable"),
                    "limit": one_email_whois.get("limit"),
                    "domains": one_email_whois.get("domains"),
                    "total_results": one_email_whois.get("totalResults"),
                }
            ]
        }
