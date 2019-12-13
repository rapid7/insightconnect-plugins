import komand
from .schema import AppsByAgentIdsInput, AppsByAgentIdsOutput, Input, Output, Component
from komand_sentinelone.util.helper import Helper


class AppsByAgentIds(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='apps_by_agent_ids',
                description=Component.DESCRIPTION,
                input=AppsByAgentIdsInput(),
                output=AppsByAgentIdsOutput())

    def run(self, params={}):
        response = self.connection.apps_by_agent_ids(Helper.join_or_empty(params.get(Input.IDS, [])))

        data = []
        if Output.DATA in response:
            for i in response.get(Output.DATA):
                data.append(komand.helper.clean_dict(i))

        return {
            Output.DATA: data
        }
