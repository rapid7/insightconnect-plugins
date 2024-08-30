import insightconnect_plugin_runtime
from .schema import IsolateEndpointInput, IsolateEndpointOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from time import sleep


class IsolateEndpoint(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="isolate_endpoint",
            description=Component.DESCRIPTION,
            input=IsolateEndpointInput(),
            output=IsolateEndpointOutput(),
        )

    def run(self, params={}):
        endpoint = params.get(Input.ENDPOINT)
        isolation_string = params.get(Input.ISOLATION_STATE)
        isolation_state = True if isolation_string == "Isolate" else False
        whitelist = params.get(Input.WHITELIST)

        if whitelist and endpoint in whitelist and not isolation_state:
            raise PluginException(
                cause="Endpoint found in the whitelist.",
                assistance=f"If you would like to block this host, remove {endpoint} from the whitelist and try again.",
            )

        try:
            result = self.connection.xdr_api.isolate_endpoint(endpoint, isolation_state)
        except (
            PluginException
        ):  # This is usually the result of an isolate action being in progress, try again after 10 seconds
            self.logger.warning("Isolation action failed. Waiting 10 seconds and trying again.")
            sleep(10)
            result = self.connection.xdr_api.isolate_endpoint(endpoint, isolation_state)

        return {Output.RESULT: result}
