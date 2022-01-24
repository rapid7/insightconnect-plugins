import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.util.constants.endpoints import START_ARIEL_SEARCH_ENDPOINT
from icon_ibm_qradar.util.url import URL
from icon_ibm_qradar.util.utils import (
    get_default_header,
    handle_response,
    prepare_request_params,
)

from .schema import (
    Component,
    StartArielSearchInput,
    StartArielSearchOutput,
    Input,
    Output,
)

# Custom imports below


class StartArielSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="start_ariel_search",
            description=Component.DESCRIPTION,
            input=StartArielSearchInput(),
            output=StartArielSearchOutput(),
        )
        self.endpoint = START_ARIEL_SEARCH_ENDPOINT

    def run(self, params={}):
        """
        Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        aql_search_query = params.get(Input.AQL, "")
        self.logger.info("AQL provided: %s", aql_search_query)

        query_params = {"query_expression": aql_search_query}

        url_obj = URL(self.connection.host_url, self.endpoint)
        basic_url, headers = prepare_request_params(params, self.logger, url_obj, [], query_params)

        auth = (self.connection.username, self.connection.password)
        headers = get_default_header()
        try:
            response = requests.post(
                url=basic_url, headers=headers, data={}, auth=auth, verify=self.connection.verify_ssl
            )
        except requests.exceptions.ConnectionError:
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)

        return {Output.DATA: handle_response(response)}
