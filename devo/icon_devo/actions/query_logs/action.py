import insightconnect_plugin_runtime
from .schema import QueryLogsInput, QueryLogsOutput, Input, Output, Component
# Custom imports below


class QueryLogs(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='query_logs',
                description=Component.DESCRIPTION,
                input=QueryLogsInput(),
                output=QueryLogsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
