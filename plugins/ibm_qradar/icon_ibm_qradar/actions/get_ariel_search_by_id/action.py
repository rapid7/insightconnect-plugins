import insightconnect_plugin_runtime
import requests

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_ibm_qradar.util.constants.endpoints import GET_ARIEL_SEARCH_BY_ID_ENDPOINT
from icon_ibm_qradar.util.constants.messages import NEGATIVE_POLL_INTERVAL_PROVIDED
from icon_ibm_qradar.util.url import URL
from icon_ibm_qradar.util.utils import get_default_header, handle_response

from .schema import (
    Component,
    GetArielSearchByIdInput,
    GetArielSearchByIdOutput,
    Input,
    Output,
)


class GetArielSearchById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="get_ariel_search_by_id",
            description=Component.DESCRIPTION,
            input=GetArielSearchByIdInput(),
            output=GetArielSearchByIdOutput(),
        )

        self.endpoint = GET_ARIEL_SEARCH_BY_ID_ENDPOINT

    def run(self, params={}):
        """
        Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        search_id = params.get(Input.SEARCH_ID)
        self.logger.info("Search ID provided: %s", search_id)

        poll_interval = params.get(Input.POLL_INTERVAL, 0)
        self.logger.info("Poll Interval Provided: %s", poll_interval)

        if poll_interval < 0:
            self.logger.info("Terminating: Poll interval provided as negative value.")
            raise PluginException(cause=NEGATIVE_POLL_INTERVAL_PROVIDED)

        url_obj = URL(self.connection.host_url, self.endpoint)
        basic_url = url_obj.get_basic_url()
        if search_id:
            basic_url = basic_url.format(search_id=search_id)

        auth = (self.connection.username, self.connection.password)
        headers = get_default_header()
        if poll_interval != 0:
            headers["Prefer"] = f"wait={poll_interval}"
        try:
            response = requests.get(
                url=basic_url, headers=headers, data={}, auth=auth, verify=self.connection.verify_ssl
            )
        except requests.exceptions.ConnectionError:
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)

        return {Output.DATA: handle_response(response)}
