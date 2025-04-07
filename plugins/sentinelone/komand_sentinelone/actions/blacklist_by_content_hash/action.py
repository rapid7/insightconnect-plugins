import insightconnect_plugin_runtime
from .schema import (
    BlacklistByContentHashInput,
    BlacklistByContentHashOutput,
    Component,
    Input,
    Output,
)

# Custom imports below


class BlacklistByContentHash(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="blacklist_by_content_hash",
            description=Component.DESCRIPTION,
            input=BlacklistByContentHashInput(),
            output=BlacklistByContentHashOutput(),
        )

    def run(self, params={}):
        return {
            Output.AFFECTED: self.connection.client.blacklist_by_content_hash(params.get(Input.HASH))
            .get("data", {})
            .get("affected", 0)
        }
