import insightconnect_plugin_runtime
from .schema import GetRelatedMachinesInput, GetRelatedMachinesOutput, Input, Output, Component

# Custom imports below
import validators


class GetRelatedMachines(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_related_machines",
            description=Component.DESCRIPTION,
            input=GetRelatedMachinesInput(),
            output=GetRelatedMachinesOutput(),
        )

    def run(self, params={}):
        self.logger.info("Running...")
        indicator = params.get(Input.INDICATOR)
        if validators.domain(indicator):
            indicator_type = "domains"
        elif validators.sha1(indicator):
            indicator_type = "files"
        else:
            indicator_type = "users"
        return {
            Output.MACHINES: insightconnect_plugin_runtime.helper.clean(
                self.connection.client.get_related_machines(indicator, indicator_type).get("value")
            )
        }
