import insightconnect_plugin_runtime
from .schema import GetCveInput, GetCveOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_intelhub.util.api import IntelHubAPI
from komand_rapid7_intelhub.util.helpers import map_cve


class GetCve(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_cve",
            description=Component.DESCRIPTION,
            input=GetCveInput(),
            output=GetCveOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        cve_id = params.get(Input.CVE_ID)
        # END INPUT BINDING - DO NOT REMOVE

        api = IntelHubAPI(self.connection, self.logger)
        response = api.get_cve(cve_id=cve_id)

        if not response:
            return {
                Output.CVE: {},
                Output.FOUND: False,
            }

        return {
            Output.CVE: map_cve(response),
            Output.FOUND: True,
        }
