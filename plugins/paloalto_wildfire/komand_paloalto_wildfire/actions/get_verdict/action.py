import insightconnect_plugin_runtime

from .schema import GetVerdictInput, GetVerdictOutput, Input, Output


# Custom imports below


class GetVerdict(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_verdict",
            description="Query for a files classification",
            input=GetVerdictInput(),
            output=GetVerdictOutput(),
        )

    def run(self, params={}):
        out = self.connection.client.get_verdicts(params.get(Input.HASH))

        return {Output.VERDICT: out.capitalize()}
