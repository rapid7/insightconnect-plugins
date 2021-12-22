"""Action: Get Ariel Search by Id."""
import insightconnect_plugin_runtime
import requests

from insightconnect_plugin_runtime.exceptions import ClientException

from icon_ibm_qradar.util.constants.constant import GET, SEARCH_ID, POLL_INTERVAL
from icon_ibm_qradar.util.constants.endpoints import GET_ARIEL_SEARCH_BY_ID_ENDPOINT
from icon_ibm_qradar.util.constants.messages import EMPTY_SEARCH_ID_FOUND
from icon_ibm_qradar.util.url import URL
from icon_ibm_qradar.util.utils import get_default_header, handle_response

from .schema import Component, GetArielSearchByIdInput, GetArielSearchByIdOutput


class GetArielSearchById(insightconnect_plugin_runtime.Action):
    """Action class : Get Ariel Search By Id."""

    def __init__(self):
        """Initialize the action."""
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
        search_id = params.get(SEARCH_ID, "")
        self.logger.info("Search Id provided: %s", search_id)

        if search_id == "":
            self.logger.info("Terminating: Search id provided as empty.")
            raise ClientException(Exception(EMPTY_SEARCH_ID_FOUND))

        poll_interval = params.get(POLL_INTERVAL, 0)
        self.logger.info("Poll Interval Provided: %s", poll_interval)

        url_obj = URL(self.connection.hostname, self.endpoint)
        basic_url = url_obj.get_basic_url()
        if search_id:
            basic_url = basic_url.format(search_id=search_id)

        auth = (self.connection.username, self.connection.password)
        headers = get_default_header()
        if poll_interval != 0:
            headers["Prefer"] = f"wait={poll_interval}"
        try:
            response = requests.request(GET, url=basic_url, headers=headers, data={}, auth=auth, verify=False)
        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError

        return handle_response(response)
