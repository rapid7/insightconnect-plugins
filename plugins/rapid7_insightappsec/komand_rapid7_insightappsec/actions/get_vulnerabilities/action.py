import insightconnect_plugin_runtime
from .schema import GetVulnerabilitiesInput, GetVulnerabilitiesOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Vulnerabilities
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
from komand_rapid7_insightappsec.util.helpers import clean, convert_dict_keys_to_camel_case
import json


class GetVulnerabilities(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_vulnerabilities",
            description=Component.DESCRIPTION,
            input=GetVulnerabilitiesInput(),
            output=GetVulnerabilitiesOutput(),
        )

    def run(self, params={}):
        self.logger.info("Getting Vulnerabilities...")
        request = ResourceHelper(self.connection.session, self.logger)

        parameters = {
            "index": params.get(Input.INDEX),
            "size": params.get(Input.SIZE),
            "sort": params.get(Input.SORT),
            "page-token": params.get(Input.PAGETOKEN),
        }

        response = request.resource_request(
            Vulnerabilities.vulnerabilities(self.connection.url), "get", params=clean(parameters)
        )
        result = json.loads(response.get("resource"))

        return convert_dict_keys_to_camel_case(
            {
                Output.DATA: result.get("data"),
                Output.LINKS: result.get("links"),
                Output.METADATA: result.get("metadata"),
            }
        )
