import insightconnect_plugin_runtime
from .schema import (
    CreateIocThreatInput,
    CreateIocThreatOutput,
    Input,
    Output,
    Component,
)

# Custom imports below
from komand_sentinelone.util.helper import clean


class CreateIocThreat(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_ioc_threat",
            description=Component.DESCRIPTION,
            input=CreateIocThreatInput(),
            output=CreateIocThreatOutput(),
        )

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.client.create_ioc_threat(
                clean(
                    {
                        "data": [
                            {
                                "hash": params.get(Input.HASH),
                                "groupId": params.get(Input.GROUPID),
                                "path": params.get(Input.PATH),
                                "agentId": params.get(Input.AGENTID),
                                "note": params.get(Input.NOTE),
                            }
                        ]
                    }
                )
            )
            .get("data", {})
            .get("affected", 0)
        }
