import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import ExecuteResponseInput, ExecuteResponseOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.helper import clean

from ...util.validators import InputValidator
from ...util.resolver import IdentifierResolver
from ...util.orchestrator import ResponseOrchestrator
from ...util.constants import DEFAULT_MONITORING_TIMEOUT, DEFAULT_POLLING_INTERVAL


class ExecuteResponse(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="execute_response",
            description=Component.DESCRIPTION,
            input=ExecuteResponseInput(),
            output=ExecuteResponseOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        endpoint_identifier = params.get(Input.ENDPOINT_IDENTIFIER)
        intent = params.get(Input.INTENT)
        polling_interval = params.get(Input.POLLING_INTERVAL)
        timeout = params.get(Input.TIMEOUT)
        # END INPUT BINDING - DO NOT REMOVE

        # Apply defaults for optional fields
        timeout = timeout or DEFAULT_MONITORING_TIMEOUT
        polling_interval = polling_interval or DEFAULT_POLLING_INTERVAL

        # Validate inputs
        InputValidator.validate_execute_response_inputs(endpoint_identifier, intent, timeout, polling_interval)

        # Resolve and orchestrate
        resolver = IdentifierResolver(self.connection.client, self.logger)
        orchestrator = ResponseOrchestrator(self.connection.client, resolver, self.logger)
        report = orchestrator.execute(endpoint_identifier, intent, timeout, polling_interval)

        return {Output.REPORT: clean(report)}
