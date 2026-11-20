import insightconnect_plugin_runtime

from insightconnect_plugin_runtime.telemetry import auto_instrument

from .schema import GetQueryResultInput, GetQueryResultOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean

from icon_rapid7_surface_command.util.api_connection import DEFAULT_MAX_WAIT


class GetQueryResult(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_query_result",
            description=Component.DESCRIPTION,
            input=GetQueryResultInput(),
            output=GetQueryResultOutput(),
        )

    @auto_instrument
    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        job_id = params.get(Input.JOB_ID)
        max_wait = params.get(Input.MAX_WAIT)
        # END INPUT BINDING - DO NOT REMOVE

        # An unset Max Wait arrives as None; the runtime does not apply schema defaults
        if max_wait is None:
            max_wait = DEFAULT_MAX_WAIT

        job_id = (job_id or "").strip()
        if not job_id:
            raise PluginException(cause="A Job ID is required.", assistance="Use the Job ID returned by Start a Query.")

        result = self.connection.api.get_query_result(job_id=job_id, max_wait=max_wait)
        return {
            Output.STATUS: result["status"],
            Output.JOB_ID: result["job_id"],
            Output.ITEMS: clean(result["items"]),
        }
