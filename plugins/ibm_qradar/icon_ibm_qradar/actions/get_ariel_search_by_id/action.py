import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.util.constants.messages import NEGATIVE_POLL_INTERVAL_PROVIDED

from .schema import (
    Component,
    GetArielSearchByIdInput,
    GetArielSearchByIdOutput,
    Input,
    Output,
)
from icon_ibm_qradar.util.api import IBMQRadarAPI


class GetArielSearchById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="get_ariel_search_by_id",
            description=Component.DESCRIPTION,
            input=GetArielSearchByIdInput(),
            output=GetArielSearchByIdOutput(),
        )

    def run(self, params={}):
        """
        Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        search_id = params.get(Input.SEARCH_ID)
        self.logger.info(f"Search ID provided: {search_id}")

        poll_interval = params.get(Input.POLL_INTERVAL, 0)
        self.logger.info(f"Poll Interval Provided: {poll_interval}")

        if poll_interval < 0:
            self.logger.info("Terminating: Poll interval provided as negative value.")
            raise PluginException(cause=NEGATIVE_POLL_INTERVAL_PROVIDED)

        api = IBMQRadarAPI(connection=self.connection, logger=self.logger)
        response = api.get_ariel_request(search_id=search_id, poll_interval=poll_interval)
        return {Output.DATA: response}
