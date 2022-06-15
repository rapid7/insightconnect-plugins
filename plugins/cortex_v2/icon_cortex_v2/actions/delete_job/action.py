import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import DeleteJobInput, DeleteJobOutput, Input, Output, Component

# Custom imports below


class DeleteJob(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_job",
            description=Component.DESCRIPTION,
            input=DeleteJobInput(),
            output=DeleteJobOutput(),
        )

    def run(self, params={}):
        job_id = params.get(Input.JOB_ID)
        self.logger.info(f"Removing job {job_id}")
        try:
            return {Output.STATUS: self.connection.API.delete_job_by_id(job_id)}
        except Exception as e:
            raise PluginException("Failed to delete job.", assistance=f"{e}")
