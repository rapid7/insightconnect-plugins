import insightconnect_plugin_runtime

from .schema import GetVerdictInput, GetVerdictOutput, Input, Output, Component


# Custom imports below


class GetVerdict(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_verdict",
            description=Component.DESCRIPTION,
            input=GetVerdictInput(),
            output=GetVerdictOutput(),
        )

    def run(self, params={}):
        return {Output.VERDICT: self.connection.client.get_verdicts(params.get(Input.HASH)).capitalize()}
