import komand
from .schema import ListActivityMonitorsInput, ListActivityMonitorsOutput
# Custom imports below


class ListActivityMonitors(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_activity_monitors',
                description='Fetches a list of activity monitors',
                input=ListActivityMonitorsInput(),
                output=ListActivityMonitorsOutput())

    def run(self, params={}):
        max_results = params.get('max_results', 100)
        activity_monitors = self.connection.api.list_activity_monitors(
            max_results
        )
        return {'activity_monitors': activity_monitors}
