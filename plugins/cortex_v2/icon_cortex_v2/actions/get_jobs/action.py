import insightconnect_plugin_runtime
from .schema import GetJobsInput, GetJobsOutput, Input, Output

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class GetJobs(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_jobs",
            description="List of analysis jobs",
            input=GetJobsInput(),
            output=GetJobsOutput(),
        )

    def run(self, params={}):
        api = self.connection.api
        query_params = []

        start = params.get(Input.START, 0)
        limit = params.get(Input.LIMIT, 10)
        data_type_filter = params.get(Input.DATATYPEFILTER)
        data_filter = params.get(Input.DATAFILTER)
        analyzer_filter = params.get(Input.ANALYZERFILTER)

        if data_type_filter:
            query_params.append(self._eq("dataType", data_type_filter))
        if data_filter:
            query_params.append(self._eq("data", data_filter))
        if analyzer_filter:
            query_params.append(self._eq("analyzerId", analyzer_filter))

        # Based on https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/query.py#L22
        query = {"_and": query_params}
        self.logger.info(f"Query: {query}")

        range_ = f"{start}-{start + limit}"
        self.logger.info(f"Range: {range_}")

        try:
            jobs = api.find_all(query, range=range_, sort="-createdAt")
        except Exception as e:
            raise PluginException(cause="Failed to obtain the list of jobs.", assistance=f"{e}.")

        return {Output.LIST: jobs}

    @staticmethod
    def _eq(field, value):
        # Based on https://github.com/TheHive-Project/Cortex4py/blob/2.1.0/cortex4py/query.py#L2
        return {'_field': field, '_value': value}
