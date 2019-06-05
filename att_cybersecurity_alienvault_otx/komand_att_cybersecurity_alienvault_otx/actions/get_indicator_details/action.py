import komand
from .schema import GetIndicatorDetailsInput, GetIndicatorDetailsOutput, Input, Output
# Custom imports below
from komand_att_cybersecurity_alienvault_otx.util.utils import get_indicatortypes


class GetIndicatorDetails(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_indicator_details',
                description='Returns details about an indicator',
                input=GetIndicatorDetailsInput(),
                output=GetIndicatorDetailsOutput())

    def run(self, params={}):
        # for results that are not retrieving full details
        output_template = {
            "general":{},
            "geo": {},
            "reputation": {},
            "url_list": {},
            "passive_dns": {},
            "malware": {},
            "nids_list": {},
            "http_scans": {}
        }

        indicator_type = get_indicatortypes(params.get(Input.INDICATOR_TYPE))
        indicator = params.get(Input.INDICATOR)
        section = params.get(Input.SECTION)
        if section == "full":
            results = self.connection.client.get_indicator_details_full(
                indicator_type=indicator_type,
                indicator=indicator)
            clean_results = komand.helper.clean(results)
            return {Output.RESULTS: clean_results}

        results = self.connection.client.get_indicator_details_by_section(
            indicator_type=indicator_type,
            indicator=indicator,
            section=section)
        output_template[section] = results

        clean_results = komand.helper.clean(output_template)

        return {Output.RESULTS: clean_results}
