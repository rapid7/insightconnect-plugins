import komand
from .schema import (
    DeactivateActivityMonitorInput, DeactivateActivityMonitorOutput
)
# Custom imports below


class DeactivateActivityMonitor(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='deactivate_activity_monitor',
                description='Deactivate an activity monitor',
                input=DeactivateActivityMonitorInput(),
                output=DeactivateActivityMonitorOutput())

    def run(self, params={}):
        activity_monitor_id = params.get('activity_monitor_id')
        activity_monitor = self.connection.api.deactivate_activity_monitor(
            activity_monitor_id
        )
        return {'activity_monitor': activity_monitor}
