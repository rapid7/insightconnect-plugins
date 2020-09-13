import insightconnect_plugin_runtime
import time
from .schema import PullAlertsInput, PullAlertsOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class PullAlerts(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='pull_alerts',
                description=Component.DESCRIPTION,
                input=PullAlertsInput(),
                output=PullAlertsOutput())

    def run(self, params={}):
        frequency = params.get(Input.FREQUENCY, 300)
        start_time = int(time.time() * 1000)
        while True:
            data = {}
            try:
                data = self.connection.client.model_breaches(start_time)
            except PluginException as e:
                self.logger.info(f"{e.cause} {e.assistance} {e.data}")
            except Exception as e:
                self.logger.info(f"{e}")

            if data:
                self.send({
                    Output.RESULTS: data
                })
            else:
                self.logger.info(f"Empty response. Waiting for {frequency} seconds")

            start_time = int((time.time() - frequency) * 1000)
            time.sleep(frequency)
