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

    def __normalize(self, result):
        formatted = {Output.FOUND: False, Output.THREATSCORE: 0, Output.REPORTS: []}
        if result and len(result) > 0:
            result = insightconnect_plugin_runtime.helper.clean(result)
            return {
                Output.FOUND: True,
                Output.REPORTS: result,
                Output.THREATSCORE: max(node.get("threat_score", 0) for node in result),
            }
        return formatted

    def run(self, params={}):
        """Run action"""
        hash_to_analise = params.get(Input.HASH)
        if validators.md5(hash_to_analise) or validators.sha256(hash_to_analise) or validators.sha1(hash_to_analise):
            return self.__normalize(self.connection.api.lookup_by_hash(hash_to_analise))
        else:
            raise PluginException(
                cause="Provided hash is not supported.",
                assistance="The API only supports MD5, SHA256, sha1 hashes. Please check the provided hash and try again.",
            )
