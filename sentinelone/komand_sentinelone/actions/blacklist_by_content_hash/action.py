import insightconnect_plugin_runtime
from .schema import BlacklistByContentHashInput, BlacklistByContentHashOutput, Input, Output

# Custom imports below


class BlacklistByContentHash(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="blacklist_by_content_hash",
            description="Add hashed content to global blacklist",
            input=BlacklistByContentHashInput(),
            output=BlacklistByContentHashOutput(),
        )

    def run(self, params={}):
        hash_value = params.get(Input.HASH)
        result = self.connection.blacklist_by_content_hash(hash_value)
        affected = result.get("data", {}).get("affected", 0)

        return {Output.AFFECTED: affected}
