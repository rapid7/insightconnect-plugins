import komand
from .schema import GetActivityMonitorInput, GetActivityMonitorOutput
# Custom imports below


class GetActivityMonitor(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_activity_monitor',
                description='Fetches a specific activity monitor '
                'by unique identifier',
                input=GetActivityMonitorInput(),
                output=GetActivityMonitorOutput())

    def run(self, params={}):
        activity_monitor_id = params.get('activity_monitor_id')
        activity_monitor = self.connection.api.get_activity_monitor(
            activity_monitor_id
        )
        return {'activity_monitor': activity_monitor}
