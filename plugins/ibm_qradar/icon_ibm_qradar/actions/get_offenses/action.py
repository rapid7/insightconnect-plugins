import insightconnect_plugin_runtime
import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetOffensesInput, GetOffensesOutput, Component, Input, Output
from icon_ibm_qradar.util.constants.endpoints import GET_OFFENSES_ENDPOINT
from icon_ibm_qradar.util.url import URL
from icon_ibm_qradar.util.utils import prepare_request_params, handle_response


class GetOffenses(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super().__init__(
            name="get_offenses",
            description=Component.DESCRIPTION,
            input=GetOffensesInput(),
            output=GetOffensesOutput(),
        )

        self.endpoint = GET_OFFENSES_ENDPOINT

    def run(self, params={}):
        """
        Run Method to execute action.

        :param params: Input Param config required for the Action
        :return: None
        """
        url_obj = URL(self.connection.host_url, self.endpoint)
        basic_url, headers = prepare_request_params(
            params,
            self.logger,
            url_obj,
            [Input.RANGE, Input.FILTER, Input.FIELDS, Input.SORT],
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
