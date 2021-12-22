"""Action: Start Ariel Search."""

import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import ClientException

from icon_ibm_qradar.util.constants.constant import AQL, POST
from icon_ibm_qradar.util.constants.endpoints import START_ARIEL_SEARCH_ENDPOINT
from icon_ibm_qradar.util.constants.messages import EMPTY_AQL_FOUND
from icon_ibm_qradar.util.url import URL
from icon_ibm_qradar.util.utils import get_default_header, handle_response

from .schema import Component, StartArielSearchInput, StartArielSearchOutput

# Custom imports below


class StartArielSearch(insightconnect_plugin_runtime.Action):
    """Action class : Start Ariel Search."""

    def __init__(self):
        """Initialize the action."""
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
        aql_search_query = params.get(AQL, "")
        self.logger.info("Aql provided: %s", aql_search_query)
        if aql_search_query == "":
            self.logger.info("Terminating: Aql query provided as empty.")
            raise ClientException(Exception(EMPTY_AQL_FOUND))

        url_obj = URL(self.connection.hostname, self.endpoint)
        basic_url = url_obj.get_basic_url()
        if aql_search_query:
            basic_url = f"{basic_url}?query_expression={aql_search_query}"

        auth = (self.connection.username, self.connection.password)
        headers = get_default_header()
        try:
            response = requests.request(POST, url=basic_url, headers=headers, data={}, auth=auth, verify=False)
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError

        return handle_response(response)
