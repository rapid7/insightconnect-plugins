import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetJobDetailsInput, GetJobDetailsOutput, Input, Output, Component

# Custom imports below
from icon_cortex_v2.util.util import filter_job, filter_job_artifacts


class GetJobDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_job_details",
            description=Component.DESCRIPTION,
            input=GetJobDetailsInput(),
            output=GetJobDetailsOutput(),
        )

    def run(self, params={}):
        job_id = params.get(Input.JOB_ID)
        self.logger.info(f"Getting details for job {job_id}")
        try:
            result = filter_job(self.connection.API.get_job_by_id(job_id))
            result["artifacts"] = filter_job_artifacts(self.connection.API.get_job_artifacts(job_id))
            return {Output.JOB: result}
        except Exception as error:
            raise PluginException(cause="Failed to get job details.", assistance=f"{error}")
