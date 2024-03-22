import insightconnect_plugin_runtime

from .schema import (
    Component,
    StartArielSearchInput,
    StartArielSearchOutput,
    Input,
    Output,
)
from icon_ibm_qradar.util.api import IBMQRadarAPI

# Custom imports below


class StartArielSearch(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="start_ariel_search",
            description=Component.DESCRIPTION,
            input=StartArielSearchInput(),
            output=StartArielSearchOutput(),
        )

    def run(self, params={}):
        """
        Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        aql_search_query = params.get(Input.AQL, "")
        self.logger.info(f"AQL provided: {aql_search_query}")

        query_params = {"query_expression": aql_search_query}

        api = IBMQRadarAPI(connection=self.connection, logger=self.logger)
        response = api.start_ariel_request(params=params, query_params=query_params, fields=[])
        return {Output.DATA: response}
