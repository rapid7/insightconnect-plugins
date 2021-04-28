import insightconnect_plugin_runtime
from .schema import LookupAlertInput, LookupAlertOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_recorded_future.util.api import Endpoint


class LookupAlert(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_alert",
            description=Component.DESCRIPTION,
            input=LookupAlertInput(),
            output=LookupAlertOutput(),
        )

    def run(self, params={}):
        try:
            return {
                Output.ALERT: insightconnect_plugin_runtime.helper.clean(
                    self.connection.client.make_request(Endpoint.lookup_alert(params.get(Input.ALERT_ID))).get("data")
                )
            }
        except AttributeError as e:
            raise PluginException(
                cause="Recorded Future returned unexpected response.",
                assistance="Please check that the provided input is correct and try again.",
                data=e,
            )
