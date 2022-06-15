import insightconnect_plugin_runtime
from .schema import GetJobDetailsInput, GetJobDetailsOutput, Input, Output, Component

# Custom imports below
from icon_cortex_v2.util.convert import job_to_dict
from cortex4py.exceptions import ServiceUnavailableError, AuthenticationError
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class GetJobDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_job_details",
            description=Component.DESCRIPTION,
            input=GetJobDetailsInput(),
            output=GetJobDetailsOutput(),
        )

    def run(self, params={}):
        api = self.connection.api

        job_id = params.get(Input.JOB_ID)
        self.logger.info(f"Getting details for job {job_id}")

        try:
            job = api.jobs.get_by_id(job_id)
            job = job_to_dict(job, api)
        except AuthenticationError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        except ServiceUnavailableError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        except Exception as e:
            raise ConnectionTestException(cause="Unable to retrieve job details.", assistance=f"{e}.")

        return {Output.JOB: job}
