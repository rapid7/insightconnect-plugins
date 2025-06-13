import insightconnect_plugin_runtime
from .schema import SearchAccountsInput, SearchAccountsOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from komand_rapid7_insightidr.util.endpoints import Accounts
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper
from komand_rapid7_insightidr.util.util import get_logging_context
import json


class SearchAccounts(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_accounts",
            description=Component.DESCRIPTION,
            input=SearchAccountsInput(),
            output=SearchAccountsOutput(),
        )

    def run(self, params={}):
        parameters = clean({"size": params.get(Input.SIZE), "index": params.get(Input.INDEX)})

        data = {
            "search": params.get(Input.SEARCH, []),
            "sort": params.get(Input.SORT, []),
        }

        self.connection.session.headers["Accept-version"] = "strong-force-preview "
        request = ResourceHelper(self.connection.session, self.logger)
        endpoint = Accounts.search_accounts(self.connection.url)
        response = request.resource_request(endpoint, "post", payload=data, params=parameters)

        try:
            result = json.loads(response.get("resource"))
        except json.decoder.JSONDecodeError:
            self.logger.error(f"InsightIDR response: {response}", **get_logging_context())
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )

        try:
            data = clean(result.get("data", []))
            metadata = result.get("metadata", {})
            return {Output.DATA: data, Output.METADATA: metadata}
        except KeyError:
            self.logger.error(result)
            raise PluginException(
                cause="The response from InsightIDR was not in the correct format.",
                assistance="Contact support for help. See log for more details",
            )
