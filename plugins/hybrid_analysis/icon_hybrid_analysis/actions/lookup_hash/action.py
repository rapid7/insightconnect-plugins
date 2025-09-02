import validators

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

# Custom imports below
from .schema import LookupHashInput, LookupHashOutput, Input, Output


class LookupHash(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="lookup_hash",
            description="Lookup By Hash",
            input=LookupHashInput(),
            output=LookupHashOutput(),
        )

    def _normalize(self, result):
        formatted = {Output.FOUND: False, Output.REPORTS: []}
        if result and isinstance(result, dict):
            result = insightconnect_plugin_runtime.helper.clean(result)
            return {
                Output.FOUND: True,
                Output.REPORTS: result.get("reports", []),
            }
        return formatted

    def run(self, params={}):
        """Run action"""
        hash_to_analyze = params.get(Input.HASH)
        if validators.md5(hash_to_analyze) or validators.sha256(hash_to_analyze) or validators.sha1(hash_to_analyze):
            return self._normalize(self.connection.api.lookup_by_hash(hash_to_analyze))
        else:
            raise PluginException(
                cause="Provided hash is not supported.",
                assistance="The API only supports MD5, SHA256, SHA1 hashes. Please check the provided hash and try again.",
            )
