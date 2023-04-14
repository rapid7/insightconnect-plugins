import insightconnect_plugin_runtime
from .schema import GetCvesForCyberTermInput, GetCvesForCyberTermOutput, Input, Output, Component

# Custom imports below
from icon_rapid7_intsights.util.helpers import clean, convert_dict_keys_to_camel_case


class GetCvesForCyberTerm(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_cves_for_cyber_term",
            description=Component.DESCRIPTION,
            input=GetCvesForCyberTermInput(),
            output=GetCvesForCyberTermOutput(),
        )

    def run(self, params={}):
        return {
            Output.CYBERTERMCVES: clean(
                convert_dict_keys_to_camel_case(
                    self.connection.client.get_cves_for_cyber_term(params.get(Input.CYBERTERMID)).get("content", [])
                )
            )
        }
