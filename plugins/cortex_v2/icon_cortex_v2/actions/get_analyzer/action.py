import insightconnect_plugin_runtime
from .schema import GetAnalyzerInput, GetAnalyzerOutput

# Custom imports below
from icon_cortex_v2.util.convert import analyzers_to_dicts
from cortex4py.exceptions import ServiceUnavailableError, AuthenticationError, CortexException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class GetAnalyzer(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analyzer",
            description="List enabled analyzers within Cortex",
            input=GetAnalyzerInput(),
            output=GetAnalyzerOutput(),
        )

    def run(self, params={}):
        api = self.connection.api
        analyzer_id = params.get("analyzer_id")

        if analyzer_id:
            self.logger.info("User specified Analyzer ID: %s", analyzer_id)
            try:
                analyzers = [api.analyzers.get_by_id(analyzer_id)]
            except AuthenticationError as e:
                self.logger.error(e)
                raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
            except ServiceUnavailableError as e:
                self.logger.error(e)
                raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
            except CortexException as e:
                raise ConnectionTestException(cause="Failed to get analyzers.", assistance="{}.".format(e))
        else:
            try:
                analyzers = api.analyzers.find_all({}, range="all")
            except AuthenticationError as e:
                self.logger.error(e)
                raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
            except ServiceUnavailableError as e:
                self.logger.error(e)
                raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
            except CortexException as e:
                raise ConnectionTestException(cause="Failed to get analyzers.", assistance="{}.".format(e))

        return {"list": analyzers_to_dicts(analyzers)}
