import insightconnect_plugin_runtime
from .schema import GetIocsForCyberTermInput, GetIocsForCyberTermOutput, Input, Output, Component

# Custom imports below
from icon_rapid7_intsights.util.helpers import convert_dict_keys_to_camel_case, clean


class GetIocsForCyberTerm(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_iocs_for_cyber_term",
            description=Component.DESCRIPTION,
            input=GetIocsForCyberTermInput(),
            output=GetIocsForCyberTermOutput(),
        )

    def run(self, params={}):
        cyber_term_id = params.get("cyberTermId")
        self.logger.info(f"Getting IOCs for cyber term id: {cyber_term_id}")

        parameters = {
            "iocType": params.get(Input.IOCTYPE),
            "limit": params.get(Input.LIMIT),
            "offset": params.get(Input.OFFSET),
        }

        response = self.connection.client.get_iocs_for_cyber_term(cyber_term_id, clean(parameters)).get("content", [])

        return clean(
            {
                Output.IOCS: convert_dict_keys_to_camel_case(response.get("iocs", [])),
                Output.NEXTOFFSET: response.get("nextOffset", ""),
            }
        )
