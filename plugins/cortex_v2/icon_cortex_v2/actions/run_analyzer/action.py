import insightconnect_plugin_runtime
from .schema import RunAnalyzerInput, RunAnalyzerOutput, Input, Output, Component

# Custom imports below
from icon_cortex_v2.util.convert import job_to_dict
from cortex4py.exceptions import ServiceUnavailableError, AuthenticationError, CortexException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class RunAnalyzer(insightconnect_plugin_runtime.Action):
    tlp = {"WHITE": 0, "GREEN": 1, "AMBER": 2, "RED": 3}

    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_analyzer",
            description=Component.DESCRIPTION,
            input=RunAnalyzerInput(),
            output=RunAnalyzerOutput(),
        )

    def run(self, params={}):
        api = self.connection.api

        analyzer_name = params.get(Input.ANALYZER_ID)
        observable = params.get(Input.OBSERVABLE)
        data_type = params.get(Input.ATTRIBUTES).get("dataType")
        tlp_num = params.get(Input.ATTRIBUTES).get("tlp")

        try:
            job = api.analyzers.run_by_name(
                analyzer_name, {"data": observable, "dataType": data_type, "tlp": tlp_num}, force=1
            )
            job = job_to_dict(job, api)
        except AuthenticationError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        except ServiceUnavailableError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        except CortexException as e:
            raise ConnectionTestException(cause="Failed to run analyzer.", assistance=f"{e}.")
        except Exception as e:
            # A bad analyzer returns: AttributeError: 'NoneType' object has no attribute 'id'
            raise ConnectionTestException(
                cause="Failed to run analyzer.",
                assistance="The selected analyzer may not exist in Cortex!",
            )

        return {Output.JOB: job}
