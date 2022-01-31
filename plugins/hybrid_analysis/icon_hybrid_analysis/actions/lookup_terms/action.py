import validators

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from .schema import LookupTermsInput, LookupTermsOutput, Input, Output, Component


class LookupTerms(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_terms", description=Component.DESCRIPTION, input=LookupTermsInput(), output=LookupTermsOutput()
        )
        self.verdict_mapping = {
            "whitelisted": 1,
            "no verdict": 2,
            "no specific threat": 3,
            "suspicious": 4,
            "malicious": 5,
        }

    def run(self, params={}):
        cleaned_params = insightconnect_plugin_runtime.helper.clean_dict(params)
        cleaned_params[Input.VERDICT] = self.verdict_mapping.get(cleaned_params.get(Input.VERDICT))

        if cleaned_params.get(Input.URL) and not validators.url(cleaned_params.get(Input.URL)):
            raise PluginException(
                cause="The entered URL has the wrong format.",
                assistance="Please check URL and try again. "
                "In its most common form, a URL starts with http:// or https:// followed by www, then the "
                "website name.",
            )
        if cleaned_params.get(Input.DOMAIN) and not validators.domain(cleaned_params.get(Input.DOMAIN)):
            raise PluginException(
                cause="The entered domain has the wrong format.",
                assistance="Please check domain in input and try again.",
            )
        if cleaned_params.get(Input.HOST) and not validators.ipv4(cleaned_params.get(Input.HOST)):
            raise PluginException(
                cause="Invalid IP address.",
                assistance="Check address input and try again. Allowed kind are: IPv4 Address",
            )

        response_json = insightconnect_plugin_runtime.helper.clean(self.connection.api.lookup_by_terms(cleaned_params))
        return {
            Output.SEARCHTERMS: response_json.get("search_terms"),
            Output.COUNT: response_json.get("count"),
            Output.RESULT: response_json.get("result"),
        }
