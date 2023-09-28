import insightconnect_plugin_runtime
from .schema import ActivitiesTypesInput, ActivitiesTypesOutput, Output, Component

# Custom imports below
from komand_sentinelone.util.helper import clean


class ActivitiesTypes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="activities_types",
            description=Component.DESCRIPTION,
            input=ActivitiesTypesInput(),
            output=ActivitiesTypesOutput(),
        )

    def run(self, params={}):
        return {Output.ACTIVITYTYPES: clean(self.connection.client.get_activity_types().get("data", []))}
