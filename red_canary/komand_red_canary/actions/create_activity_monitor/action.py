import komand
from .schema import CreateActivityMonitorInput, CreateActivityMonitorOutput
# Custom imports below


class CreateActivityMonitor(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_activity_monitor',
                description='Creates a new activity monitor',
                input=CreateActivityMonitorInput(),
                output=CreateActivityMonitorOutput())

    def run(self, params={}):
        activity_monitor = self.connection.api.create_activity_monitor(
            params.get('name'),
            params.get('type', 'file_modification'),
            params.get('active', True),
            params.get('file_modification_types_monitored', []),
            params.get('file_paths_monitored', []),
            params.get('usernames_matched', []),
            params.get('usernames_excluded', []),
        )
        return {'activity_monitor': activity_monitor}
