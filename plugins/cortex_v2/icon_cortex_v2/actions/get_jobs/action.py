import insightconnect_plugin_runtime
from .schema import GetJobsInput, GetJobsOutput

# Custom imports below
from cortex4py.query import And, Eq
from icon_cortex_v2.util.convert import jobs_to_dicts
from cortex4py.exceptions import ServiceUnavailableError, AuthenticationError
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


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

        start = params.get("start", 0)
        limit = params.get("limit", 10)
        data_type_filter = params.get("dataTypeFilter")
        data_filter = params.get("dataFilter")
        analyzer_filter = params.get("analyzerFilter")

        if data_type_filter:
            query_params.append(Eq("dataType", data_type_filter))
        if data_filter:
            query_params.append(Eq("data", data_filter))
        if analyzer_filter:
            query_params.append(Eq("analyzerId", analyzer_filter))

        query = And(*query_params)
        self.logger.info("Query: {}".format(query))

        range_ = "{}-{}".format(start, start + limit)
        self.logger.info("Range: {}".format(range_))

        try:
            jobs = api.jobs.find_all(query, range=range_, sort="-createdAt")
            jobs = jobs_to_dicts(jobs, api)
        except AuthenticationError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        except ServiceUnavailableError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        except Exception as e:
            raise ConnectionTestException(cause="Failed to obtain the list of jobs.", assistance="{}.".format(e))

        return {"list": jobs}
