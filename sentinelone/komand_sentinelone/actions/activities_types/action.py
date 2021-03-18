import insightconnect_plugin_runtime
from .schema import ActivitiesTypesInput, ActivitiesTypesOutput, Input, Output, Component

# Custom imports below


class ActivitiesTypes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="activities_types",
            description=Component.DESCRIPTION,
            input=ActivitiesTypesInput(),
            output=ActivitiesTypesOutput(),
        )

    def run(self, params={}):
        response = self.connection.activities_types()

        data = []
        if "data" in response:
            for i in response.get("data"):
                data.append(insightconnect_plugin_runtime.helper.clean_dict(i))

        return {Output.ACTIVITY_TYPES: data}
