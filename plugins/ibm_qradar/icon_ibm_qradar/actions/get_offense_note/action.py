import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetOffenseNoteInput, GetOffenseNoteOutput, Component, Input, Output

from icon_ibm_qradar.util.url import URL
from icon_ibm_qradar.util.utils import prepare_request_params, handle_response
from icon_ibm_qradar.util.constants.endpoints import GET_OFFENSES_NOTES
from icon_ibm_qradar.util.constants.messages import EMPTY_OFFENSE_ID_FOUND


class GetOffenseNote(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="get_offense_note",
            description=Component.DESCRIPTION,
            input=GetOffenseNoteInput(),
            output=GetOffenseNoteOutput(),
        )
        self.endpoint = GET_OFFENSES_NOTES

    def run(self, params={}):
        """Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        offense_id = params.get(Input.OFFENSE_ID, "")
        self.logger.info("Offense ID provided: %s", offense_id)

        url_obj = URL(self.connection.host_url, self.endpoint)
        basic_url = url_obj.get_basic_url()
        if offense_id:
            basic_url = basic_url.format(offense_id=offense_id)

        url_obj.set_basic_url(basic_url)

        basic_url, headers = prepare_request_params(
            params, self.logger, url_obj, [Input.FILTER, Input.FIELDS, Input.RANGE]
        )

        auth = (self.connection.username, self.connection.password)
        try:
            self.logger.debug(f"Final URL: {basic_url}")
            response = requests.get(
                url=basic_url, headers=headers, data={}, auth=auth, verify=self.connection.verify_ssl
            )
        except requests.exceptions.ConnectionError:
            raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)

        return {Output.DATA: handle_response(response)}
