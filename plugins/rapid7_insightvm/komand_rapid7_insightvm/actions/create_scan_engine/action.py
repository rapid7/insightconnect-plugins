import insightconnect_plugin_runtime
from .schema import CreateScanEngineInput, CreateScanEngineOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from insightconnect_plugin_runtime.exceptions import PluginException


class CreateScanEngine(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_scan_engine",
            description="Create a new scan engine with console -> engine connectivity",
            input=CreateScanEngineInput(),
            output=CreateScanEngineOutput(),
        )

    def run(self, params={}):
        # Note: ID is not a required payload parameter despite the API docs saying it is
        # Providing it actually causes the request to fail
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.ScanEngine.scan_engines(self.connection.console_url)
        payload = params

        self.logger.info("Creating scan engine...")
        try:
            response = resource_helper.resource_request(endpoint=endpoint, method="post", payload=payload)
        except Exception as e:
            if "An unexpected error occurred." in str(e):
                error = "Security console failed to connect to scan engine"
            elif "errors with the input or parameters supplied" in str(e):
                error = (
                    f"{str(e)} - "
                    f"This may be due to an engine with this IP or name already existing in the Security Console."
                )
            else:
                error = e
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

        return response
