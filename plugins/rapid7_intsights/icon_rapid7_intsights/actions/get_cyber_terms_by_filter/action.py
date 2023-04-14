import insightconnect_plugin_runtime
from .schema import GetCyberTermsByFilterInput, GetCyberTermsByFilterOutput, Input, Output, Component

# Custom imports below
from icon_rapid7_intsights.util.helpers import convert_dict_keys_to_camel_case, clean


class GetCyberTermsByFilter(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_cyber_terms_by_filter",
            description=Component.DESCRIPTION,
            input=GetCyberTermsByFilterInput(),
            output=GetCyberTermsByFilterOutput(),
        )

    def run(self, params={}):
        parameters = {
            "search": params.get(Input.SEARCH),
            "type": params.get(Input.TYPE),
            "severity": params.get(Input.SEVERITY),
            "target-sector": params.get(Input.TARGETSECTOR),
            "target-country": params.get(Input.TARGETCOUNTRY),
            "origin": params.get(Input.ORIGIN),
            "ttp": params.get(Input.TTP),
            "last-update-from": params.get(Input.LASTUPDATEFROM),
            "last-update-to": params.get(Input.LASTUPDATETO),
            "limit": params.get(Input.LIMIT),
            "offset": params.get(Input.OFFSET),
        }
        response = self.connection.client.get_cyber_terms_by_filter(clean(parameters))
        return clean(
            {
                Output.CYBERTERMS: convert_dict_keys_to_camel_case(response.get("content", [])),
                Output.NEXTOFFSET: response.get("nextOffset", ""),
            }
        )
