import insightconnect_plugin_runtime
from .schema import GetThreatActorInput, GetThreatActorOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_intelhub.util.api import IntelHubAPI


class GetThreatActor(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_threat_actor",
            description=Component.DESCRIPTION,
            input=GetThreatActorInput(),
            output=GetThreatActorOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE
        uuid = params.get(Input.UUID)
        # END INPUT BINDING - DO NOT REMOVE

        api = IntelHubAPI(self.connection, self.logger)
        response = api.get_threat_actor(uuid)

        if not response:
            return {
                Output.THREAT_ACTOR: {},
                Output.FOUND: False,
            }

        return {
            Output.THREAT_ACTOR: response,
            Output.FOUND: True,
        }
