import insightconnect_plugin_runtime
from .schema import ListLocationsAndBranchesInput, ListLocationsAndBranchesOutput, Input, Output, Component

# Custom imports below
from icon_topdesk.util.helpers import clean


class ListLocationsAndBranches(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="listLocationsAndBranches",
            description=Component.DESCRIPTION,
            input=ListLocationsAndBranchesInput(),
            output=ListLocationsAndBranchesOutput(),
        )

    def run(self, params={}):
        return {
            Output.LOCATIONSANDBRANCHES: self.connection.api_client.list_locations_and_branches(clean(params.copy()))
        }
