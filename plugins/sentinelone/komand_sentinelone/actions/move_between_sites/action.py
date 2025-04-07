import insightconnect_plugin_runtime
from .schema import (
    MoveBetweenSitesInput,
    MoveBetweenSitesOutput,
    Input,
    Output,
    Component,
)

# Custom imports below


class MoveBetweenSites(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="move_between_sites",
            description=Component.DESCRIPTION,
            input=MoveBetweenSitesInput(),
            output=MoveBetweenSitesOutput(),
        )

    def run(self, params={}):
        agents_filter = params.get(Input.FILTER, {})
        data = {"targetSiteId": (params.get(Input.TARGETSITEID, ""))}

        return {
            Output.AFFECTED: self.connection.client.agents_action_move_agent_to_new_site(
                agents_filter, data, "move-to-site"
            )
            .get("data", {})
            .get("affected", 0)
        }
