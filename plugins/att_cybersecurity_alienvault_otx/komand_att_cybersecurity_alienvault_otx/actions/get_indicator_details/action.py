import insightconnect_plugin_runtime
from .schema import GetIndicatorDetailsInput, GetIndicatorDetailsOutput, Input, Output, Component

# Custom imports below
from komand_att_cybersecurity_alienvault_otx.util.utils import get_indicator_type


class GetIndicatorDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_indicator_details",
            description=Component.DESCRIPTION,
            input=GetIndicatorDetailsInput(),
            output=GetIndicatorDetailsOutput(),
        )

    def run(self, params={}):
        # for results that are not retrieving full details
        results = {
            "general": {},
            "geo": {},
            "reputation": {},
            "url_list": {},
            "passive_dns": {},
            "malware": {},
            "nids_list": {},
            "http_scans": {},
        }

        indicator_type = get_indicator_type(params.get(Input.INDICATOR_TYPE))
        indicator = params.get(Input.INDICATOR)
        section = params.get(Input.SECTION)

        if section == "full":
            return {
                Output.RESULTS: insightconnect_plugin_runtime.helper.clean(
                    self.connection.client.get_indicator_details_full(
                        indicator_type=indicator_type, indicator=indicator
                    )
                )
            }

        results[section] = self.connection.client.get_indicator_details_by_section(
            indicator_type=indicator_type, indicator=indicator, section=section
        )

        return {Output.RESULTS: insightconnect_plugin_runtime.helper.clean(results)}
