import insightconnect_plugin_runtime
import time
from .schema import NewAlertInput, NewAlertOutput, Input, Output, Component
# Custom imports below


class NewAlert(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='new_alert',
                description=Component.DESCRIPTION,
                input=NewAlertInput(),
                output=NewAlertOutput())

    def run(self, params={}):
        """Run the trigger"""
        while True:
            # TODO: Implement trigger functionality
            self.send({})
            time.sleep(params.get("interval", 5))
