import insightconnect_plugin_runtime
from .schema import RunWakeUpInput, RunWakeUpOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import re


class RunWakeUp(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='run_wake_up',
            description=Component.DESCRIPTION,
            input=RunWakeUpInput(),
            output=RunWakeUpOutput())

    def run(self, params=None):
        if params is None:
            params = {}

        try:
            wake_up_response = self.connection.client(
                'system.wakeupAgent',
                params.get(Input.SYSTEM_NAME)
            )

            return {
                Output.COMPLETED: int(re.search(r'completed: (\d+)', wake_up_response).group(1)),
                Output.FAILED: int(re.search(r'failed: (\d+)', wake_up_response).group(1)),
                Output.EXPIRED: int(re.search(r'expired: (\d+)', wake_up_response).group(1)),
            }
        except Exception as e:
            raise PluginException(
                cause="Error",
                assistance=f"Could not wake up a system. Error: {e}"
            )
