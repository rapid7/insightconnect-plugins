import insightconnect_plugin_runtime
from .schema import HashInput, HashOutput, Input, Output, Component
from insightconnect_plugin_runtime.exceptions import PluginException
# Custom imports below
import validators


class Hash(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='hash',
            description=Component.DESCRIPTION,
            input=HashInput(),
            output=HashOutput())

    @staticmethod
    def _is_not_valid_hash(hash):
        if validators.md5(hash) or validators.sha1(hash):
            return False

        return True

    def run(self, params={}):
        if self._is_not_valid_hash(params.get(Input.HASH)):
            raise PluginException(
                cause='An invalid or unsupported hash type was provided.',
                assistance='Please enter a MD5 or SHA1 hash.'
            )

        data = self.connection.client.search_hash(params.get(Input.HASH).lower())

        if int(data['response_code']) == 0:
            self.logger.info('ThreatCrowd API did not return any matches.')
            return {Output.FOUND: False}

        return {
            Output.DOMAINS: insightconnect_plugin_runtime.helper.clean_list(data['domains']),
            Output.HASHES: {'sha1': data['sha1'], 'md5': data['md5']},
            Output.IPS: insightconnect_plugin_runtime.helper.clean_list(data['ips']),
            Output.PERMALINK: data['permalink'],
            Output.REFERENCES: insightconnect_plugin_runtime.helper.clean_list(data['references']),
            Output.SCANS: insightconnect_plugin_runtime.helper.clean_list(data['scans']),
            Output.FOUND: True
        }
