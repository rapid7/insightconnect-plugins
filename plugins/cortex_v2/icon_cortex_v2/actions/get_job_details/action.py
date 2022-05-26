import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetJobDetailsInput, GetJobDetailsOutput, Input, Output, Component

# Custom imports below


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
            return {Output.JOB: self.connection.API.get_job_by_id(job_id)}
        except Exception as e:
            raise PluginException(cause="Failed to get job details.", assistance=f"{e}")
