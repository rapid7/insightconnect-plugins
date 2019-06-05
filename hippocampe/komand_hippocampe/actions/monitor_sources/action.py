import komand
from .schema import MonitorSourcesInput, MonitorSourcesOutput
# Custom imports below


class MonitorSources(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='monitor_sources',
                description='Return merged results from: freshness, last_query, sched_report, size_by_source',
                input=MonitorSourcesInput(),
                output=MonitorSourcesOutput())

    def run(self, params={}):
        monitor_results = self.connection.api.monitor_sources()
        return {'monitor_results': monitor_results}
