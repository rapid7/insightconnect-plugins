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
        if not frequency:
            frequency = 300

        if frequency <= 0:
            raise PluginException(
                cause="Input error.",
                assistance="Polling frequency should be a number greater than 0."
            )
        self.logger.info(f"Waiting for {frequency} seconds.")
        while True:
            data = []
            did = params.get(Input.DID, 0)
            minscore = params.get(Input.MINSCORE, 0)/100
            pbid = params.get(Input.PBID, 0)
            pid = params.get(Input.PID, 0)
            try:
                self.logger.info(f"Getting response for last {frequency} seconds.")
                data = self.connection.client.model_breaches({
                    "starttime": int((time.time() - frequency) * 1000),
                    "did": did if did != 0 else None,
                    "minscore": minscore if minscore != 0 else None,
                    "pbid": pbid if pbid != 0 else None,
                    "pid": pid if pid != 0 else None,
                    "uuid": params.get(Input.UUID)
                })
            except PluginException as e:
                self.logger.info(f"{e.cause} {e.assistance} {e.data}")
            except Exception as e:
                self.logger.info(f"{e}")

            if data:
                if isinstance(data, dict):
                    data = [data]

                self.send({
                    Output.RESULTS: data
                })
            else:
                self.logger.info(f"Empty response. Waiting for {frequency} seconds.")

            time.sleep(frequency)
