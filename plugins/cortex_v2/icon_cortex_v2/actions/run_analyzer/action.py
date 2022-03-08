import insightconnect_plugin_runtime
from .schema import RunAnalyzerInput, RunAnalyzerOutput

# Custom imports below
from icon_cortex_v2.util.convert import job_to_dict
from cortex4py.exceptions import ServiceUnavailableError, AuthenticationError, CortexException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class RunAnalyzer(insightconnect_plugin_runtime.Action):
    tlp = {"WHITE": 0, "GREEN": 1, "AMBER": 2, "RED": 3}

    def __init__(self):
        super(self.__class__, self).__init__(
            name="run_analyzer",
            description="Run analyzers on an observable",
            input=RunAnalyzerInput(),
            output=RunAnalyzerOutput(),
        )

    def run(self, params={}):
        api = self.connection.api

        analyzer_name = params.get("analyzer_id")
        observable = params.get("observable")
        data_type = params.get("attributes").get("dataType")
        tlp_num = params.get("attributes").get("tlp")

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
            raise ConnectionTestException(cause="Failed to run analyzer.", assistance="{}.".format(e))
        except Exception as e:
            # A bad analyzer returns: AttributeError: 'NoneType' object has no attribute 'id'
            raise ConnectionTestException(
                cause="Failed to run analyzer.",
                assistance="The selected analyzer may not exist in Cortex!",
            )

        return {"job": job}
