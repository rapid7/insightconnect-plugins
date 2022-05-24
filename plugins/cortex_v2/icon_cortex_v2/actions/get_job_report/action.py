import insightconnect_plugin_runtime
from .schema import GetJobReportInput, GetJobReportOutput

# Custom imports below
from icon_cortex_v2.util.convert import report_to_dict
from cortex4py.exceptions import ServiceUnavailableError, AuthenticationError, CortexException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class GetJobReport(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_job_report",
            description="List report of a given job, identified by its ID",
            input=GetJobReportInput(),
            output=GetJobReportOutput(),
        )

    def run(self, params={}):
        job_id = params.get("job_id")
        self.logger.info("Getting report for job {}".format(job_id))

        try:
            report = self.connection.api.jobs.get_report(job_id)
        except AuthenticationError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        except ServiceUnavailableError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        except CortexException as e:
            raise ConnectionTestException(cause="Failed to get job report.", assistance="{}.".format(e))

        return {"report": report_to_dict(report)}
