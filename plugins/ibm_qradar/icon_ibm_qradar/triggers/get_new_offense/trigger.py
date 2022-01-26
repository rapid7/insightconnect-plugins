import insightconnect_plugin_runtime
import time
import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import GetNewOffenseInput, GetNewOffenseOutput, Component, Input, Output
from icon_ibm_qradar.util.url import URL
from icon_ibm_qradar.util.utils import prepare_request_params, handle_response
from icon_ibm_qradar.util.constants.endpoints import GET_OFFENSES_ENDPOINT


class GetNewOffense(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super().__init__(
            name="get_new_offense",
            description=Component.DESCRIPTION,
            input=GetNewOffenseInput(),
            output=GetNewOffenseOutput(),
        )
        self.endpoint = GET_OFFENSES_ENDPOINT

    def run(self, params={}):
        """Run the trigger."""
        auth = (self.connection.username, self.connection.password)
        current_epoch_time = int(time.time()) * 1000
        url_obj = URL(self.connection.host_url, self.endpoint)

        if Input.FILTER in params.keys() and params[Input.FILTER] != "":
            params[Input.FILTER] = params[Input.FILTER] + " and first_persisted_time>={current_epoch_time}"
        else:
            params[Input.FILTER] = "first_persisted_time>={current_epoch_time}"

        basic_url, headers = prepare_request_params(
            params,
            self.logger,
            url_obj,
            [Input.FILTER, Input.FIELDS, Input.RANGE, Input.SORT],
        )

        while True:
            try:
                final_url = basic_url.format(current_epoch_time=current_epoch_time)
                response = requests.get(
                    url=final_url, headers=headers, data={}, auth=auth, verify=self.connection.verify_ssl
                )
                new_offense = {Output.DATA: handle_response(response)}

                self.logger.debug(f"Number of new offenses found: {len(new_offense[Output.DATA])}")

                if len(new_offense[Output.DATA]) > 0:
                    self.send(new_offense)
                    current_epoch_time = int(time.time()) * 1000

            except requests.exceptions.ConnectionError:
                raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)

            time.sleep(params.get(Input.INTERVAL, 60))
