import insightconnect_plugin_runtime
import time
import datetime
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
        while True:
            try:
                url_obj = URL(self.connection.hostname, self.endpoint)
                copy_params = params.copy()
                if Input.FILTER in copy_params.keys() and copy_params[Input.FILTER] != "":
                    copy_params[
                        Input.FILTER
                    ] = f"{copy_params[Input.FILTER]},first_persisted_time>={current_epoch_time}"
                else:
                    copy_params[Input.FILTER] = f"first_persisted_time>={current_epoch_time}"

                basic_url, headers = prepare_request_params(
                    copy_params,
                    self.logger,
                    url_obj,
                    [Input.FILTER, Input.FIELDS, Input.RANGE, Input.SORT],
                )

                self.logger.debug(f"current_epoch_time : {current_epoch_time}")
                self.logger.debug(f"Final Url: {basic_url}")
                response = requests.get(url=basic_url, headers=headers, data={}, auth=auth)
                new_offence = {Output.DATA: handle_response(response)}

                self.logger.debug(f"New Offence: {len(new_offence[Output.DATA])}")

                if len(new_offence[Output.DATA]) > 0:
                    self.send(new_offence)
                    current_epoch_time = int(time.time()) * 1000

            except requests.exceptions.ConnectionError:
                raise PluginException(preset=PluginException.Preset.SERVICE_UNAVAILABLE)

            time.sleep(params.get(Input.INTERVAL, 60))
