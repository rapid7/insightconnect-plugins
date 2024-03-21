import insightconnect_plugin_runtime

from .schema import (
    GetOffenseClosingReasonsInput,
    GetOffenseClosingReasonsOutput,
    Component,
    Input,
    Output,
)
from icon_ibm_qradar.util.constants.endpoints import GET_CLOSING_REASON_ENDPOINT
from icon_ibm_qradar.util.api import IBMQRadarAPI


class GetOffenseClosingReasons(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="get_offense_closing_reasons",
            description=Component.DESCRIPTION,
            input=GetOffenseClosingReasonsInput(),
            output=GetOffenseClosingReasonsOutput(),
        )

        self.endpoint = GET_CLOSING_REASON_ENDPOINT

    def run(self, params={}):
        """Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        include_deleted = params.get(Input.INCLUDE_DELETED, False)
        self.logger.info(f"Include_deleted provided: {include_deleted}")

        include_reserved = params.get(Input.INCLUDE_RESERVED, False)
        self.logger.info(f"Include_reserved provided: {include_reserved}")

        query_params = {
            "include_deleted": "true" if include_deleted else "false",
            "include_reserved": "true" if include_reserved else "false",
        }

        api = IBMQRadarAPI(connection=self.connection, logger=self.logger)
        response = api.get_offense_closing_reasons_request(
            params=params, query_params=query_params, fields=[Input.RANGE, Input.FILTER, Input.FIELDS]
        )
        return {Output.DATA: response}
