import insightconnect_plugin_runtime
from .schema import GetSandboxReportForHashInput, GetSandboxReportForHashOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import validators


class GetSandboxReportForHash(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_sandbox_report_for_hash',
                description=Component.DESCRIPTION,
                input=GetSandboxReportForHashInput(),
                output=GetSandboxReportForHashOutput())

    def run(self, params={}):
        hash_to_analyze = params.get(Input.HASH)
        if not validators.md5(hash_to_analyze):
            raise PluginException(
                cause="Provided hash is not supported.",
                assistance="The API only supports MD5 hashes. Please check the provided hash and try again."
            )
        return {
            Output.FULL_REPORT: self.connection.client.get_hash_report(hash_to_analyze)
        }
