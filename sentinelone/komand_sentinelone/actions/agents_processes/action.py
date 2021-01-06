import insightconnect_plugin_runtime
from .schema import AgentsProcessesInput, AgentsProcessesOutput, Input, Output, Component
from komand_sentinelone.util.helper import Helper
from insightconnect_plugin_runtime.exceptions import PluginException


class AgentsProcesses(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='agents_processes',
                description=Component.DESCRIPTION,
                input=AgentsProcessesInput(),
                output=AgentsProcessesOutput())

    def run(self, params={}):
        # response = self.connection.agents_processes(Helper.join_or_empty(params.get(Input.IDS, [])))
        #
        # data = []
        # if "data" in response:
        #     for i in response.get("data"):
        #         data.append(insightconnect_plugin_runtime.helper.clean_dict(i))
        #
        # return {
        #     Output.AGENTS_PROCESSES: data
        # }

        raise PluginException(cause="This action is obsolete. The associated SentinelOne endpoint for this action is not supported.",
                              assistance="Please use the 'Agents Applications' action instead. The endpoint used in"
                                         " 'Agent Applications' has replaced said endpoint.")

