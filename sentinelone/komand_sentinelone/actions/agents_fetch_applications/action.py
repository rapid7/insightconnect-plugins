import komand
from .schema import AgentsFetchApplicationsInput, AgentsFetchApplicationsOutput, Input, Output, Component
# Custom imports below


class AgentsFetchApplications(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_fetch_applications',
                description=Component.DESCRIPTION,
                input=AgentsFetchApplicationsInput(),
                output=AgentsFetchApplicationsOutput())

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.agents_action("fetch-installed-apps", params.get(Input.FILTER, None)).get("affected", 0)
        }
