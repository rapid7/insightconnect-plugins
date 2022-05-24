import insightconnect_plugin_runtime
from .schema import DeleteJobInput, DeleteJobOutput

# Custom imports below
from cortex4py.exceptions import ServiceUnavailableError, AuthenticationError, CortexException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class DeleteJob(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_job",
            description="Delete an existing job, identified by its ID",
            input=DeleteJobInput(),
            output=DeleteJobOutput(),
        )

    def run(self, params={}):
        job_id = params.get("job_id")
        self.logger.info("Removing job {}".format(job_id))

        try:
            status = self.connection.api.jobs.delete(job_id)
        except AuthenticationError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        except ServiceUnavailableError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        except CortexException as e:
            self.logger.error("Failed to delete job: {}".format(e))
            status = False

        return {"status": status}
