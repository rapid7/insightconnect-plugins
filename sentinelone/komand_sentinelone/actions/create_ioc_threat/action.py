import insightconnect_plugin_runtime
from .schema import CreateIocThreatInput, CreateIocThreatOutput, Input, Output

# Custom imports below


class CreateIocThreat(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ioc_threat",
            description="Create an IOC threat",
            input=CreateIocThreatInput(),
            output=CreateIocThreatOutput(),
        )

    def run(self, params={}):
        hash_ = params.get(Input.HASH)
        agent_id = params.get(Input.AGENTID)
        group_id = params.get(Input.GROUPID, "")
        path = params.get(Input.PATH, "")
        note = params.get(Input.NOTE, "")

        affected = self.connection.create_ioc_threat(hash_, group_id, path, agent_id, note)
        return {Output.AFFECTED: affected}
