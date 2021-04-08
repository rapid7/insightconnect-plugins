import insightconnect_plugin_runtime
import time
from .schema import NewScansInput, NewScansOutput, Input, Output, Component
# Custom imports below


class NewScans(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='new_scans',
                description=Component.DESCRIPTION,
                input=NewScansInput(),
                output=NewScansOutput())

    def run(self, params={}):
        """Run the trigger"""
        while True:
            # TODO: Implement trigger functionality
            self.send({})
            time.sleep(params.get("interval", 5))
