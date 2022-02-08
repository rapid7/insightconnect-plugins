import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetJobsInput, GetJobsOutput, Input, Output, Component

# Custom imports below
from icon_cortex_v2.util.util import filter_jobs, filter_job_artifacts, eq_, and_


class GetJobs(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_jobs",
            description=Component.DESCRIPTION,
            input=GetJobsInput(),
            output=GetJobsOutput(),
        )

    def run(self, params={}):
        api = self.connection.API
        query_params = []

        start = params.get(Input.START, 0)
        limit = params.get(Input.LIMIT, 10)
        data_type_filter = params.get(Input.DATATYPEFILTER)
        data_filter = params.get(Input.DATAFILTER)
        analyzer_filter = params.get(Input.ANALYZERFILTER)

        if data_type_filter:
            query_params.append(eq_("dataType", data_type_filter))
        if data_filter:
            query_params.append(eq_("data", data_filter))
        if analyzer_filter:
            query_params.append(eq_("analyzerId", analyzer_filter))

        query = and_(query_params)
        self.logger.info(f"Query: {query}")

        range_ = f"{start}-{start + limit}"
        self.logger.info(f"Range: {range_}")

        try:
            jobs = filter_jobs(api.search_for_all_jobs(query, range_=range_, sort_="-createdAt"))
            for job in jobs:
                job["artifacts"] = filter_job_artifacts(api.get_job_artifacts(job["id"]))
        except Exception as e:
            raise PluginException(cause="Failed to obtain the list of jobs.", assistance=f"{e}.")

        return {Output.LIST: jobs}
