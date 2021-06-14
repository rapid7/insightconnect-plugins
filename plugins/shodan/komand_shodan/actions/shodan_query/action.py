import insightconnect_plugin_runtime
from .schema import ShodanQueryInput, ShodanQueryOutput, Output, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import shodan


class ShodanQuery(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="shodan_query",
            description="Search Shodan Using the Query Syntax",
            input=ShodanQueryInput(),
            output=ShodanQueryOutput(),
        )

    def run(self, params={}):
        try:
            response = shodan.Shodan(self.connection.token).search(params.get(Input.QUERY))
        except shodan.exception.APIError as e:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=e)

        if response["total"] == 0:
            self.logger.info("No results found for query")

        ip_str = []
        org = []

        for item in response["matches"]:
            ip_str.append(item["ip_str"])
            org.append(item["org"])

        return insightconnect_plugin_runtime.helper.clean_dict(
            {Output.IP_STR: ip_str, Output.ORG: org, Output.TOTAL: response.get("total")}
        )
